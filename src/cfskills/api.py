"""Thin, polite Codeforces API client.

* enforces the 1 request / 2 s limit the API asks for
* retries transient failures ("Call limit exceeded", 5xx, timeouts) with backoff
* raises ``CFError`` for genuine FAILED responses (e.g. rating changes
  unavailable for an unrated contest) so callers can decide what to do
"""

from __future__ import annotations

import logging
import random
import time
from typing import Any

import requests

log = logging.getLogger(__name__)

BASE_URL = "https://codeforces.com/api/"


class CFError(RuntimeError):
    """The API answered with status=FAILED (not transient)."""


class CFTransient(RuntimeError):
    """Something worth retrying."""


class CFClient:
    def __init__(
        self,
        min_interval: float = 2.0,
        max_retries: int = 8,
        timeout: float = 90.0,
        session: requests.Session | None = None,
    ) -> None:
        self.min_interval = min_interval
        self.max_retries = max_retries
        self.timeout = timeout
        self.session = session or requests.Session()
        self.session.headers["User-Agent"] = "cs328-cfskills/0.1 (student project)"
        self._last_call = 0.0
        self.n_calls = 0

    def _throttle(self) -> None:
        wait = self.min_interval - (time.monotonic() - self._last_call)
        if wait > 0:
            time.sleep(wait)

    def get(self, method: str, **params: Any) -> Any:
        """Call ``method`` and return the ``result`` payload."""
        url = BASE_URL + method
        for attempt in range(self.max_retries):
            self._throttle()
            try:
                resp = self.session.get(url, params=params, timeout=self.timeout)
                self._last_call = time.monotonic()
                self.n_calls += 1
                if resp.status_code == 429 or resp.status_code >= 500:
                    raise CFTransient(f"HTTP {resp.status_code}")
                data = resp.json()
            except (requests.RequestException, ValueError, CFTransient) as exc:
                backoff = min(60.0, 2.0 * 2**attempt) + random.uniform(0, 1)
                log.warning("%s %s: %s -> retry in %.0fs", method, params, exc, backoff)
                time.sleep(backoff)
                continue

            if data.get("status") == "OK":
                return data["result"]

            comment = str(data.get("comment", ""))
            if "limit exceeded" in comment.lower():
                backoff = 5.0 + random.uniform(0, 2)
                log.warning("rate limited on %s -> sleeping %.0fs", method, backoff)
                time.sleep(backoff)
                continue
            raise CFError(comment)
        raise CFTransient(f"gave up on {method} {params} after {self.max_retries} attempts")

    # convenience wrappers -------------------------------------------------
    def contest_list(self) -> list[dict]:
        return self.get("contest.list", gym="false")

    def problemset_problems(self) -> dict:
        return self.get("problemset.problems")

    def contest_standings(self, contest_id: int) -> dict:
        # The API only serves non-gym standings to anonymous callers when contestId is
        # the *only* parameter; the default is showUnofficial=false, which is what we want.
        return self.get("contest.standings", contestId=contest_id)

    def contest_rating_changes(self, contest_id: int) -> list[dict]:
        return self.get("contest.ratingChanges", contestId=contest_id)
