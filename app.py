"""D5 demo as a tiny Streamlit app.

    pip install streamlit
    streamlit run app.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

import pandas as pd  # noqa: E402
import streamlit as st  # noqa: E402

from cfskills.demo import Explorer  # noqa: E402
from cfskills import paths  # noqa: E402

st.set_page_config(page_title="Codeforces skill fingerprint", layout="wide")
st.title("Is one number enough?")
st.caption("Skill fingerprint beyond the rating, and your skill twins. CS 328 - Vishnu Sinha & Bhavay Goyal")


@st.cache_resource
def get_explorer() -> Explorer:
    return Explorer()


try:
    ex = get_explorer()
except FileNotFoundError as exc:
    st.error(f"Pipeline outputs missing ({exc}). Run `make all` first.")
    st.stop()

handle = st.text_input("Codeforces handle", value=ex.users.sort_values("n_participations", ascending=False)["handle"].iloc[0])
k = st.slider("number of twins", 3, 25, 10)

if handle:
    try:
        fp = ex.query(handle, k)
    except KeyError as exc:
        st.warning(str(exc))
        st.stop()

    c1, c2, c3 = st.columns(3)
    c1.metric("rating (last in sample)", fp.rating)
    c2.metric("rated rounds in sample", fp.n_participations)
    c3.metric("significant axes", len(fp.axes))

    st.subheader("Skill fingerprint")
    axes = pd.DataFrame(fp.axes)
    axes["label"] = axes.apply(lambda r: f"axis {r.axis}: {r.minus_tags}  <->  {r.plus_tags}", axis=1)
    st.bar_chart(axes.set_index("label")["z"], horizontal=True)
    st.dataframe(axes[["axis", "z", "percentile", "plus_tags", "minus_tags"]].round(2), hide_index=True, use_container_width=True)

    st.subheader("Skill twins")
    if fp.twins:
        st.dataframe(pd.DataFrame(fp.twins), hide_index=True, use_container_width=True)
    else:
        st.info("No twins above threshold.")

    with st.expander("Project figures"):
        for name in ["D1_spectrum.png", "D3_heatmap.png", "D4_lsh_eval.png"]:
            p = paths.OUT / name
            if p.exists():
                st.image(str(p), caption=name)
