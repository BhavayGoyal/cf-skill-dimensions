# D2 - Skill-axis table (resid)

20 of 20 components are significant against the permutation null.

Sign of each axis is arbitrary. `+` rows = highest loading problems, `-` rows = lowest.
Tag enrichment z > 0 means problems with the tag load positively on the axis.
`corr(loading, rating)` close to +-1 means the axis is mostly *difficulty* (or the division the
problem was set for), not a topic; look for axes with low |corr| and strong tag enrichment.

## Axis 1  (sigma = 97.13)

- enriched at `+` end: implementation (z=+3.7), strings (z=+3.7), greedy (z=+2.0), constructive algorithms (z=+1.8), games (z=+0.7)
- enriched at `-` end: dp (z=-16.5), dfs and similar (z=-15.2), data structures (z=-15.0), binary search (z=-14.2), trees (z=-13.7)
- corr(loading, problem rating) = -0.36; mean rating of `+` end 840, of `-` end 1387
- user scores: std 0.401

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.0726 | 1857A Array Coloring | 800 | greedy;math |
| + | +0.0725 | 1692A Marathon | 800 | implementation |
| + | +0.0693 | 1918A Brick Wall | 800 | constructive algorithms;greedy;implementation;math |
| + | +0.0692 | 1742A Sum | 800 | implementation |
| + | +0.0677 | 1731A Joey Takes Money | 800 | greedy;math |
| + | +0.0677 | 1849A Morning Sandwich | 800 | implementation;math |
| + | +0.0677 | 1728A Colored Balls: Revisited | 800 | brute force;greedy;implementation;sortings |
| + | +0.0676 | 1999D Slavic's Exam | 1100 | greedy;implementation;strings |
| + | +0.0676 | 1768A Greatest Convex | 800 | greedy;math;number theory |
| + | +0.0668 | 1742B Increasing | 800 | greedy;implementation;sortings |
| + | +0.0663 | 1729A Two Elevators | 800 | math |
| + | +0.0642 | 1792A GamingForces | 800 | greedy;sortings |
| + | +0.0638 | 1721A Image | 800 | greedy;implementation |
| + | +0.0635 | 1878A How Much Does Daytona Cost? | 800 | greedy |
| + | +0.0630 | 1986C Update Queries | 1100 | data structures;greedy;sortings |
| - | -0.0671 | 1807E Interview | 1300 | binary search;implementation;interactive |
| - | -0.0618 | 1850E Cardboard for Pictures | 1100 | binary search;geometry;implementation;math |
| - | -0.0601 | 1873F Money Trees | 1300 | binary search;greedy;math;two pointers |
| - | -0.0587 | 1703E Mirror Grid | 1200 | implementation |
| - | -0.0577 | 1850G The Morning Star | 1500 | combinatorics;data structures;geometry;implementation;math;sortings |
| - | -0.0568 | 1742D Coprime | 1100 | brute force;greedy;number theory |
| - | -0.0550 | 1791F Range Update Point Query | 1500 | binary search;brute force;data structures |
| - | -0.0549 | 1927E Klever Permutation | 1400 | constructive algorithms;math;two pointers |
| - | -0.0527 | 1873G ABBC or BACB | 1500 | constructive algorithms;greedy |
| - | -0.0508 | 1921D Very Different Array | 1100 | data structures;greedy;sortings;two pointers |
| - | -0.0474 | 1850F We Were Both Children | 1300 | brute force;implementation;math;number theory |
| - | -0.0451 | 1850H The Third Letter | 1700 | dfs and similar;dsu;graphs;greedy;implementation |
| - | -0.0450 | 1985G D-Function | 1600 | combinatorics;math;number theory |
| - | -0.0449 | 1873H Mad City | 1700 | dfs and similar;dsu;games;graphs;shortest paths;trees |
| - | -0.0446 | 1760F Quests | 1500 | binary search;greedy;sortings |

_Plain-language reading:_ TODO

## Axis 2  (sigma = 80.97)

- enriched at `+` end: combinatorics (z=+2.9), dp (z=+2.8), data structures (z=+2.6), binary search (z=+2.3), trees (z=+1.7)
- enriched at `-` end: constructive algorithms (z=-2.9), meet-in-the-middle (z=-1.9), flows (z=-1.8), graph matchings (z=-1.6), strings (z=-1.4)
- corr(loading, problem rating) = +0.03; mean rating of `+` end 800, of `-` end 880
- user scores: std 0.423

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.0725 | 1692A Marathon | 800 | implementation |
| + | +0.0716 | 1644A Doors and Keys | 800 | implementation |
| + | +0.0708 | 1651A Playoff | 800 | implementation |
| + | +0.0689 | 1624A Plus One on the Subset | 800 | math |
| + | +0.0670 | 1650A Deletions of Two Adjacent Letters | 800 | implementation;strings |
| + | +0.0660 | 1669A Division? | 800 | implementation |
| + | +0.0649 | 1676B Equal Candies | 800 | greedy;math;sortings |
| + | +0.0648 | 1676A Lucky? | 800 | implementation |
| + | +0.0646 | 1632A ABC | 800 | implementation |
| + | +0.0638 | 1660A Vasya and Coins | 800 | greedy;math |
| + | +0.0616 | 1646A Square Counting | 800 | math |
| + | +0.0609 | 1701A Grass Field | 800 | implementation |
| + | +0.0609 | 1607A Linear Keyboard | 800 | implementation;strings |
| + | +0.0608 | 1579A Casimir's String Solitaire | 800 | math;strings |
| + | +0.0602 | 1698A XOR Mixup | 800 | bitmasks;brute force |
| - | -0.0705 | 1918A Brick Wall | 800 | constructive algorithms;greedy;implementation;math |
| - | -0.0662 | 1703E Mirror Grid | 1200 | implementation |
| - | -0.0652 | 1927A Make it White | 800 | greedy;strings |
| - | -0.0647 | 1999D Slavic's Exam | 1100 | greedy;implementation;strings |
| - | -0.0638 | 1980A Problem Generator | 800 | math |
| - | -0.0621 | 1676G White-Black Balanced Subtrees | 1300 | dfs and similar;dp;graphs;trees |
| - | -0.0611 | 1933A Turtle Puzzle: Rearrange and Negate | 800 | greedy;math;sortings |
| - | -0.0587 | 1926A Vlad and the Best of Five | 800 | implementation |
| - | -0.0586 | 1985A Creating Words | 800 | implementation;strings |
| - | -0.0555 | 1985B Maximum Multiple Sum | 800 | brute force;math;number theory |
| - | -0.0555 | 1983A Array Divisibility | 800 | constructive algorithms;math |
| - | -0.0554 | 2001A Make All Equal | 800 | greedy;implementation |
| - | -0.0549 | 1929A Sasha and the Beautiful Array | 800 | constructive algorithms;greedy;math;sortings |
| - | -0.0544 | 1955A Yogurt Sale | 800 | math |
| - | -0.0539 | 1976A Verify Password | 800 | implementation;sortings;strings |

_Plain-language reading:_ TODO

## Axis 3  (sigma = 68.62)

- enriched at `+` end: greedy (z=+3.9), two pointers (z=+3.8), binary search (z=+3.6), dp (z=+3.3), bitmasks (z=+2.7)
- enriched at `-` end: math (z=-2.0), string suffix structures (z=-1.4), hashing (z=-1.0), games (z=-0.7), strings (z=-0.7)
- corr(loading, problem rating) = +0.06; mean rating of `+` end 1307, of `-` end 800
- user scores: std 0.359

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.0887 | 1980C Sofia and the Lost Operations | 1300 | constructive algorithms;greedy |
| + | +0.0821 | 2000D Right Left Wrong | 1200 | greedy;implementation;two pointers |
| + | +0.0707 | 1996C Sort | 1200 | dp;greedy;sortings;strings |
| + | +0.0673 | 1955C Inhabitant of the Deep Sea | 1300 | greedy;implementation;math |
| + | +0.0649 | 2025C New Game | 1300 | binary search;brute force;greedy;implementation;sortings;two pointers |
| + | +0.0605 | 1927D Find the Different Ones! | 1300 | binary search;brute force;data structures;dp;dsu;greedy;two pointers |
| + | +0.0589 | 2008F Sakurako's Box | 1400 | combinatorics;math;number theory |
| + | +0.0588 | 2091E Interesting Ratio | 1300 | brute force;math;number theory;two pointers |
| + | +0.0578 | 2044E Insane Problem | 1300 | binary search;greedy;implementation;math;number theory |
| + | +0.0567 | 2072E Do You Love Your Hero and His Two-Hit Multi-Target Attacks? | 1500 | binary search;brute force;constructive algorithms;dp;geometry;greedy;math |
| + | +0.0566 | 2027C Add Zeros | 1500 | brute force;data structures;dfs and similar;dp;graphs;greedy |
| + | +0.0564 | 2137E Mexification | 1500 | brute force;implementation;math |
| + | +0.0562 | 1931C Make Equal Again | 1000 | brute force;greedy;math |
| + | +0.0559 | 1935B Informatics in MAC | 1200 | constructive algorithms |
| + | +0.0545 | 1999E Triple Operations | 1300 | dp;implementation;math |
| - | -0.0724 | 2072A New World, New Me, New Array | 800 | greedy;implementation;math |
| - | -0.0609 | 1579A Casimir's String Solitaire | 800 | math;strings |
| - | -0.0604 | 1624A Plus One on the Subset | 800 | math |
| - | -0.0600 | 1567A Domino Disaster | 800 | implementation;strings |
| - | -0.0594 | 2065A Skibidus and Amog'u | 800 | brute force;constructive algorithms;greedy;implementation;strings |
| - | -0.0593 | 2033A Sakurako and Kosuke | 800 | constructive algorithms;implementation;math |
| - | -0.0580 | 1607A Linear Keyboard | 800 | implementation;strings |
| - | -0.0548 | 1560A Dislike of Threes | 800 | implementation |
| - | -0.0543 | 2055A Two Frogs | 800 | constructive algorithms;games;greedy;math |
| - | -0.0542 | 1611A Make Even | 800 | constructive algorithms;math |
| - | -0.0537 | 2050A Line Breaks | 800 | implementation |
| - | -0.0536 | 1650A Deletions of Two Adjacent Letters | 800 | implementation;strings |
| - | -0.0535 | 2086A Cloudberry Jam | 800 | math |
| - | -0.0533 | 1644A Doors and Keys | 800 | implementation |
| - | -0.0533 | 1569A Balanced Substring | 800 | implementation |

_Plain-language reading:_ TODO

## Axis 4  (sigma = 63.71)

- enriched at `+` end: trees (z=+8.5), dp (z=+8.0), combinatorics (z=+7.1), dfs and similar (z=+7.0), divide and conquer (z=+6.9)
- enriched at `-` end: greedy (z=-7.1), constructive algorithms (z=-3.5), sortings (z=-3.0), games (z=-1.0), geometry (z=-0.4)
- corr(loading, problem rating) = +0.23; mean rating of `+` end 800, of `-` end 1167
- user scores: std 0.315

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.0804 | 1791A Codeforces Checking | 800 | implementation;strings |
| + | +0.0741 | 1790A Polycarp and the Day of Pi | 800 | implementation;math;strings |
| + | +0.0721 | 1791B Following Directions | 800 | geometry;implementation |
| + | +0.0705 | 1742A Sum | 800 | implementation |
| + | +0.0683 | 1829A Love Story | 800 | implementation;strings |
| + | +0.0677 | 1742B Increasing | 800 | greedy;implementation;sortings |
| + | +0.0657 | 1791C Prepend and Append | 800 | implementation;two pointers |
| + | +0.0647 | 1829B Blank Space | 800 | implementation |
| + | +0.0629 | 1741A Compare T-Shirt Sizes | 800 | implementation;strings |
| + | +0.0626 | 1807A Plus or Minus | 800 | implementation |
| + | +0.0599 | 1760A Medium Number | 800 | implementation;sortings |
| + | +0.0594 | 1760B Atilla's Favorite Problem | 800 | greedy;implementation;strings |
| + | +0.0580 | 1729A Two Elevators | 800 | math |
| + | +0.0576 | 1857A Array Coloring | 800 | greedy;math |
| + | +0.0565 | 1807B Grab the Candies | 800 | greedy |
| - | -0.0818 | 1742E Scuza | 1200 | binary search;greedy;math |
| - | -0.0799 | 2000D Right Left Wrong | 1200 | greedy;implementation;two pointers |
| - | -0.0740 | 1722D Line | 1100 | greedy;sortings |
| - | -0.0721 | 1791G1 Teleporters (Easy Version) | 1100 | greedy;sortings |
| - | -0.0719 | 1760E Binary Inversions | 1100 | data structures;greedy;math |
| - | -0.0670 | 1993B Parity and Sum | 1100 | constructive algorithms;greedy |
| - | -0.0640 | 1791D Distinct Split | 1000 | brute force;greedy;strings |
| - | -0.0638 | 1741D Masha and a Beautiful Tree | 1300 | dfs and similar;divide and conquer;graphs;sortings;trees |
| - | -0.0631 | 1676E Eating Queries | 1100 | binary search;greedy;sortings |
| - | -0.0612 | 1850E Cardboard for Pictures | 1100 | binary search;geometry;implementation;math |
| - | -0.0594 | 1741C Minimize the Thickness | 1100 | brute force;greedy;math;two pointers |
| - | -0.0590 | 2118C Make It Beautiful | 1300 | bitmasks;data structures;greedy;math |
| - | -0.0589 | 1843D Apple Tree | 1200 | combinatorics;dfs and similar;dp;math;trees |
| - | -0.0588 | 2086C Disappearing Permutation | 1300 | dfs and similar;dp;dsu;graphs;greedy;implementation |
| - | -0.0588 | 2049B pspspsps | 1300 | brute force;constructive algorithms;graph matchings;implementation |

_Plain-language reading:_ TODO

## Axis 5  (sigma = 57.74)

- enriched at `+` end: trees (z=+7.9), dp (z=+6.6), graphs (z=+6.0), divide and conquer (z=+5.9), data structures (z=+5.6)
- enriched at `-` end: greedy (z=-5.4), constructive algorithms (z=-2.3), sortings (z=-2.1), math (z=-2.1), games (z=-1.3)
- corr(loading, problem rating) = +0.18; mean rating of `+` end 1013, of `-` end 1227
- user scores: std 0.298

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.0931 | 1883F You Are So Beautiful | 1400 | data structures |
| + | +0.0724 | 1883G1 Dances (Easy version) | 1400 | binary search;greedy;two pointers |
| + | +0.0627 | 1927A Make it White | 800 | greedy;strings |
| + | +0.0601 | 2123E MEX Count | 1400 | binary search;data structures;greedy;sortings;two pointers |
| + | +0.0590 | 1567A Domino Disaster | 800 | implementation;strings |
| + | +0.0582 | 1579A Casimir's String Solitaire | 800 | math;strings |
| + | +0.0577 | 1857F Sum and Product | 1600 | binary search;data structures;math |
| + | +0.0572 | 2164B Even Modulo Pair | 1000 | brute force;math;number theory |
| + | +0.0564 | 2094E Boneca Ambalabu | 1200 | bitmasks |
| + | +0.0561 | 1846B Rudolph and Tic-Tac-Toe | 800 | brute force;implementation;strings |
| + | +0.0549 | 1624A Plus One on the Subset | 800 | math |
| + | +0.0541 | 1560A Dislike of Threes | 800 | implementation |
| + | +0.0539 | 1551A Polycarp and Coins | 800 | greedy;math |
| + | +0.0538 | 1872A Two Vessels | 800 | brute force;greedy;math |
| + | +0.0531 | 1535A Fair Playoff | 800 | brute force;implementation |
| - | -0.1063 | 1927D Find the Different Ones! | 1300 | binary search;brute force;data structures;dp;dsu;greedy;two pointers |
| - | -0.0843 | 1931E Anna and the Valentine's Day Gift | 1400 | games;greedy;math;sortings |
| - | -0.0790 | 1872D Plus Minus Permutation | 1200 | math |
| - | -0.0784 | 1955D Inaccurate Subsequence Search | 1400 | data structures;two pointers |
| - | -0.0727 | 1923C Find B | 1400 | constructive algorithms;greedy |
| - | -0.0684 | 2132A Homework | 800 | brute force;implementation;strings |
| - | -0.0680 | 1862D Ice Cream Balls | 1300 | binary search;combinatorics;constructive algorithms;math |
| - | -0.0673 | 1941D Rudolf and the Ball Game | 1200 | dfs and similar;dp;implementation |
| - | -0.0662 | 1935B Informatics in MAC | 1200 | constructive algorithms |
| - | -0.0655 | 2126C I Will Definitely Make It | 1100 | greedy;sortings |
| - | -0.0647 | 1857C Assembly via Minimums | 1200 | greedy;sortings |
| - | -0.0616 | 1933E Turtle vs. Rabbit Race: Optimal Trainings | 1500 | binary search;implementation;math;ternary search |
| - | -0.0612 | 1883C Raspberries | 1000 | dp;math |
| - | -0.0600 | 1873E Building an Aquarium | 1100 | binary search;sortings |
| - | -0.0591 | 1968D Permutation Game | 1300 | brute force;dfs and similar;games;graphs;greedy;math |

_Plain-language reading:_ TODO

## Axis 6  (sigma = 55.09)

- enriched at `+` end: trees (z=+3.0), string suffix structures (z=+2.7), bitmasks (z=+2.2), geometry (z=+2.2), dfs and similar (z=+2.2)
- enriched at `-` end: strings (z=-2.4), implementation (z=-1.3), brute force (z=-1.1), ternary search (z=-0.9), sortings (z=-0.3)
- corr(loading, problem rating) = +0.08; mean rating of `+` end 980, of `-` end 1033
- user scores: std 0.283

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.0664 | 1692A Marathon | 800 | implementation |
| + | +0.0640 | 1850E Cardboard for Pictures | 1100 | binary search;geometry;implementation;math |
| + | +0.0624 | 2059B Cost of the Array | 1300 | brute force;constructive algorithms;greedy;math |
| + | +0.0556 | 1850F We Were Both Children | 1300 | brute force;implementation;math;number theory |
| + | +0.0555 | 2043B Digits | 1100 | math;number theory |
| + | +0.0548 | 2118C Make It Beautiful | 1300 | bitmasks;data structures;greedy;math |
| + | +0.0545 | 2162D Beautiful Permutation | 1400 | binary search;interactive |
| + | +0.0542 | 1703A YES or YES? | 800 | brute force;implementation;strings |
| + | +0.0542 | 1703B ICPC Balloons | 800 | data structures;implementation |
| + | +0.0526 | 1676A Lucky? | 800 | implementation |
| + | +0.0526 | 1676B Equal Candies | 800 | greedy;math;sortings |
| + | +0.0523 | 1669A Division? | 800 | implementation |
| + | +0.0521 | 1741B Funny Permutation | 800 | constructive algorithms;math |
| + | +0.0517 | 1741A Compare T-Shirt Sizes | 800 | implementation;strings |
| + | +0.0516 | 1729A Two Elevators | 800 | math |
| - | -0.0743 | 1741D Masha and a Beautiful Tree | 1300 | dfs and similar;divide and conquer;graphs;sortings;trees |
| - | -0.0743 | 1703F Yet Another Problem About Pairs Satisfying an Inequality | 1300 | binary search;data structures;dp;greedy;sortings |
| - | -0.0715 | 1650C Weight of the System of Nested Segments | 1200 | greedy;hashing;implementation;sortings |
| - | -0.0684 | 1657C Bracket Sequence Deletion | 1200 | greedy;implementation |
| - | -0.0665 | 1857A Array Coloring | 800 | greedy;math |
| - | -0.0645 | 1849A Morning Sandwich | 800 | implementation;math |
| - | -0.0625 | 1622B Berland Music | 1000 | data structures;greedy;math;sortings |
| - | -0.0613 | 1701C Schedule Management | 1400 | binary search;greedy;implementation;two pointers |
| - | -0.0612 | 1692F 3SUM | 1300 | brute force;math |
| - | -0.0600 | 1535A Fair Playoff | 800 | brute force;implementation |
| - | -0.0586 | 1850A To My Critics | 800 | implementation;sortings |
| - | -0.0578 | 1537A Arithmetic Array | 800 | greedy;math |
| - | -0.0561 | 1542A Odd Set | 800 | math |
| - | -0.0561 | 1681C Double Sort | 1200 | implementation;sortings |
| - | -0.0560 | 1844A Subtraction Game | 800 | constructive algorithms;games |

_Plain-language reading:_ TODO

## Axis 7  (sigma = 49.38)

- enriched at `+` end: greedy (z=+2.5), ternary search (z=+1.9), strings (z=+1.6), implementation (z=+1.2), sortings (z=+1.2)
- enriched at `-` end: divide and conquer (z=-2.3), number theory (z=-2.3), meet-in-the-middle (z=-2.3), flows (z=-1.4), bitmasks (z=-1.3)
- corr(loading, problem rating) = -0.03; mean rating of `+` end 1093, of `-` end 1060
- user scores: std 0.257

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.0737 | 1929A Sasha and the Beautiful Array | 800 | constructive algorithms;greedy;math;sortings |
| + | +0.0730 | 1918A Brick Wall | 800 | constructive algorithms;greedy;implementation;math |
| + | +0.0708 | 1846E1 Rudolf and Snowflakes (simple version) | 1300 | brute force;implementation;math |
| + | +0.0685 | 1843D Apple Tree | 1200 | combinatorics;dfs and similar;dp;math;trees |
| + | +0.0661 | 1846D Rudolph and Christmas Tree | 1200 | constructive algorithms;geometry;math |
| + | +0.0654 | 1933A Turtle Puzzle: Rearrange and Negate | 800 | greedy;math;sortings |
| + | +0.0649 | 1862D Ice Cream Balls | 1300 | binary search;combinatorics;constructive algorithms;math |
| + | +0.0634 | 1857D Strong Vertices | 1300 | math;sortings;trees |
| + | +0.0630 | 1833D Flipper | 1400 | brute force;constructive algorithms;greedy |
| + | +0.0627 | 1926A Vlad and the Best of Five | 800 | implementation |
| + | +0.0589 | 1950A Stair, Peak, or Neither? | 800 | implementation |
| + | +0.0584 | 1985A Creating Words | 800 | implementation;strings |
| + | +0.0577 | 1927A Make it White | 800 | greedy;strings |
| + | +0.0576 | 1872E Data Structures Fan | 1500 | binary search;bitmasks;data structures;dp |
| + | +0.0575 | 2125D Segments Covering | 1600 | dp;math;probabilities |
| - | -0.0908 | 2061B Kevin and Geometry | 1100 | binary search;geometry |
| - | -0.0800 | 1998A Find K Distinct Points with Fixed Center | 800 | constructive algorithms;implementation;math |
| - | -0.0754 | 1800A Is It a Cat? | 800 | implementation;strings |
| - | -0.0711 | 2127B Hamiiid, Haaamid... Hamid? | 1300 | games;greedy |
| - | -0.0698 | 1883F You Are So Beautiful | 1400 | data structures |
| - | -0.0698 | 2131E Adjacent XOR | 1400 | brute force;greedy |
| - | -0.0671 | 1551A Polycarp and Coins | 800 | greedy;math |
| - | -0.0655 | 2075B Array Recoloring | 1300 | constructive algorithms;greedy |
| - | -0.0648 | 2179D Blackslex and Penguin Civilization | 1300 | bitmasks;constructive algorithms;greedy;math |
| - | -0.0642 | 1535A Fair Playoff | 800 | brute force;implementation |
| - | -0.0624 | 1921D Very Different Array | 1100 | data structures;greedy;sortings;two pointers |
| - | -0.0622 | 1542A Odd Set | 800 | math |
| - | -0.0614 | 1560A Dislike of Threes | 800 | implementation |
| - | -0.0612 | 2162D Beautiful Permutation | 1400 | binary search;interactive |
| - | -0.0600 | 1567A Domino Disaster | 800 | implementation;strings |

_Plain-language reading:_ TODO

## Axis 8  (sigma = 48.84)

- enriched at `+` end: binary search (z=+4.2), two pointers (z=+3.2), implementation (z=+2.9), data structures (z=+2.3), greedy (z=+2.1)
- enriched at `-` end: math (z=-3.4), probabilities (z=-3.3), combinatorics (z=-3.1), fft (z=-2.9), meet-in-the-middle (z=-2.8)
- corr(loading, problem rating) = -0.01; mean rating of `+` end 1420, of `-` end 1267
- user scores: std 0.249

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.0688 | 1920C Partitioning the Array | 1600 | brute force;math;number theory |
| + | +0.0668 | 2153C Symmetrical Polygons | 1500 | constructive algorithms;geometry;greedy;implementation;sortings |
| + | +0.0665 | 1706C Qpwoeirut And The City | 1400 | dp;flows;greedy;implementation |
| + | +0.0662 | 2131E Adjacent XOR | 1400 | brute force;greedy |
| + | +0.0646 | 2133C The Nether | 1400 | graphs;interactive |
| + | +0.0632 | 2162D Beautiful Permutation | 1400 | binary search;interactive |
| + | +0.0614 | 1791A Codeforces Checking | 800 | implementation;strings |
| + | +0.0604 | 2118C Make It Beautiful | 1300 | bitmasks;data structures;greedy;math |
| + | +0.0598 | 2119C A Good Problem | 1300 | bitmasks;constructive algorithms;math |
| + | +0.0587 | 1553C Penalty | 1200 | bitmasks;brute force;dp;greedy |
| + | +0.0571 | 1795C Tea Tasting | 1500 | binary search;data structures;implementation |
| + | +0.0570 | 1778C Flexible String | 1600 | bitmasks;brute force;strings |
| + | +0.0564 | 2195E Idiot First Search | 1500 | dfs and similar;dp;trees |
| + | +0.0553 | 1923D Slimes | 1800 | binary search;constructive algorithms;data structures;greedy;two pointers |
| + | +0.0552 | 1775C Interesting Sequence | 1600 | bitmasks;math |
| - | -0.0914 | 1684C Column Swapping | 1400 | brute force;constructive algorithms;greedy;implementation;sortings |
| - | -0.0821 | 1738B Prefix Sum Addicts | 1200 | constructive algorithms;greedy;math;sortings |
| - | -0.0818 | 1783B Matrix of Differences | 1100 | constructive algorithms;math |
| - | -0.0807 | 1983B Corner Twist | 1200 | constructive algorithms;greedy;implementation;math |
| - | -0.0778 | 1909I Short Permutation Problem | 1900 | combinatorics;dp;fft;math |
| - | -0.0769 | 1987C Basil's Garden | 1200 | dp;greedy |
| - | -0.0721 | 1979C Earning on Bets | 1200 | binary search;combinatorics;constructive algorithms;number theory |
| - | -0.0713 | 1761B Elimination of a Ring | 1000 | constructive algorithms;greedy;implementation |
| - | -0.0679 | 1774B Coloring | 1500 | constructive algorithms;greedy;math |
| - | -0.0662 | 2164B Even Modulo Pair | 1000 | brute force;math;number theory |
| - | -0.0602 | 1991C Absolute Zero | 1300 | constructive algorithms;greedy;math |
| - | -0.0598 | 1996D Fun | 1500 | binary search;brute force;combinatorics;math;number theory |
| - | -0.0593 | 1980C Sofia and the Lost Operations | 1300 | constructive algorithms;greedy |
| - | -0.0590 | 2061B Kevin and Geometry | 1100 | binary search;geometry |
| - | -0.0568 | 1807G2 Subsequence Addition (Hard Version) | 1100 | bitmasks;dp;greedy;implementation;sortings |

_Plain-language reading:_ TODO

## Axis 9  (sigma = 47.41)

- enriched at `+` end: dfs and similar (z=+6.5), data structures (z=+5.4), graphs (z=+5.4), dp (z=+5.0), trees (z=+4.7)
- enriched at `-` end: math (z=-3.9), geometry (z=-2.1), number theory (z=-1.7), sortings (z=-1.6), greedy (z=-1.2)
- corr(loading, problem rating) = +0.13; mean rating of `+` end 1127, of `-` end 1113
- user scores: std 0.248

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.0813 | 1980C Sofia and the Lost Operations | 1300 | constructive algorithms;greedy |
| + | +0.0727 | 1846B Rudolph and Tic-Tac-Toe | 800 | brute force;implementation;strings |
| + | +0.0721 | 1807E Interview | 1300 | binary search;implementation;interactive |
| + | +0.0671 | 1983C Have Your Cake and Eat It Too | 1400 | binary search;brute force;greedy;implementation |
| + | +0.0665 | 1955C Inhabitant of the Deep Sea | 1300 | greedy;implementation;math |
| + | +0.0638 | 1974D Ingenuity-2 | 1400 | constructive algorithms;greedy;implementation |
| + | +0.0634 | 2025C New Game | 1300 | binary search;brute force;greedy;implementation;sortings;two pointers |
| + | +0.0630 | 1650A Deletions of Two Adjacent Letters | 800 | implementation;strings |
| + | +0.0619 | 1669A Division? | 800 | implementation |
| + | +0.0584 | 1986D Mathematical Problem | 1400 | brute force;dp;greedy;implementation;math;two pointers |
| + | +0.0572 | 1999E Triple Operations | 1300 | dp;implementation;math |
| + | +0.0566 | 1669B Triple | 800 | implementation;sortings |
| + | +0.0556 | 1669C Odd/Even Increments | 800 | greedy;implementation;math |
| + | +0.0551 | 1631A Min Max Swap | 800 | greedy |
| + | +0.0544 | 2013C Password Cracking | 1400 | constructive algorithms;interactive;strings |
| - | -0.0938 | 2061B Kevin and Geometry | 1100 | binary search;geometry |
| - | -0.0923 | 2164B Even Modulo Pair | 1000 | brute force;math;number theory |
| - | -0.0845 | 1844C Particles | 1300 | dp;greedy;implementation;math |
| - | -0.0787 | 2119B Line Segments | 1200 | geometry;greedy;math |
| - | -0.0708 | 1983B Corner Twist | 1200 | constructive algorithms;greedy;implementation;math |
| - | -0.0650 | 2118B Make It Permutation | 1200 | constructive algorithms |
| - | -0.0625 | 1921D Very Different Array | 1100 | data structures;greedy;sortings;two pointers |
| - | -0.0602 | 1731A Joey Takes Money | 800 | greedy;math |
| - | -0.0600 | 1650C Weight of the System of Nested Segments | 1200 | greedy;hashing;implementation;sortings |
| - | -0.0593 | 1840B Binary Cafe | 1100 | bitmasks;combinatorics;math |
| - | -0.0592 | 1579B Shifting Sort | 1100 | implementation;sortings |
| - | -0.0586 | 2117D Retaliation | 1200 | binary search;math;number theory |
| - | -0.0584 | 1914E2 Game with Marbles (Hard Version) | 1400 | games;greedy;sortings |
| - | -0.0569 | 1768A Greatest Convex | 800 | greedy;math;number theory |
| - | -0.0564 | 1567B MEXor Mixup | 1000 | bitmasks;greedy |

_Plain-language reading:_ TODO

## Axis 10  (sigma = 44.09)

- enriched at `+` end: data structures (z=+3.8), brute force (z=+2.4), dsu (z=+2.1), trees (z=+2.0), dfs and similar (z=+1.8)
- enriched at `-` end: math (z=-3.9), games (z=-3.9), geometry (z=-2.3), constructive algorithms (z=-1.9), meet-in-the-middle (z=-1.3)
- corr(loading, problem rating) = +0.04; mean rating of `+` end 1233, of `-` end 1187
- user scores: std 0.230

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.1207 | 2000D Right Left Wrong | 1200 | greedy;implementation;two pointers |
| + | +0.1092 | 1980C Sofia and the Lost Operations | 1300 | constructive algorithms;greedy |
| + | +0.0860 | 1986C Update Queries | 1100 | data structures;greedy;sortings |
| + | +0.0777 | 1996C Sort | 1200 | dp;greedy;sortings;strings |
| + | +0.0757 | 2003C Turtle and Good Pairs | 1200 | constructive algorithms;greedy;sortings;strings |
| + | +0.0694 | 1615B And It's Non-Zero | 1300 | bitmasks;greedy;math |
| + | +0.0690 | 1850F We Were Both Children | 1300 | brute force;implementation;math;number theory |
| + | +0.0673 | 1999E Triple Operations | 1300 | dp;implementation;math |
| + | +0.0673 | 1553C Penalty | 1200 | bitmasks;brute force;dp;greedy |
| + | +0.0648 | 1976B Increase/Decrease/Copy | 1100 | greedy;implementation |
| + | +0.0647 | 1555C Coin Rows | 1300 | brute force;constructive algorithms;dp;implementation |
| + | +0.0645 | 2025C New Game | 1300 | binary search;brute force;greedy;implementation;sortings;two pointers |
| + | +0.0605 | 1873E Building an Aquarium | 1100 | binary search;sortings |
| + | +0.0598 | 1999D Slavic's Exam | 1100 | greedy;implementation;strings |
| + | +0.0594 | 1646C Factorials and Powers of Two | 1500 | bitmasks;brute force;constructive algorithms;dp;math |
| - | -0.0959 | 1684C Column Swapping | 1400 | brute force;constructive algorithms;greedy;implementation;sortings |
| - | -0.0735 | 1738B Prefix Sum Addicts | 1200 | constructive algorithms;greedy;math;sortings |
| - | -0.0694 | 1767D Playoff | 1500 | combinatorics;constructive algorithms;dp;greedy;math |
| - | -0.0670 | 1849A Morning Sandwich | 800 | implementation;math |
| - | -0.0656 | 1997D Maximize the Root | 1500 | binary search;dfs and similar;dp;greedy;trees |
| - | -0.0622 | 1929C Sasha and the Casino | 1400 | binary search;brute force;constructive algorithms;games;greedy;math |
| - | -0.0621 | 2117D Retaliation | 1200 | binary search;math;number theory |
| - | -0.0596 | 1873A Short Sort | 800 | brute force;implementation |
| - | -0.0594 | 1986E Beautiful Array | 1700 | greedy;math;number theory;sortings |
| - | -0.0586 | 1927E Klever Permutation | 1400 | constructive algorithms;math;two pointers |
| - | -0.0580 | 1850A To My Critics | 800 | implementation;sortings |
| - | -0.0554 | 1873B Good Kid | 800 | brute force;greedy;math |
| - | -0.0550 | 1792B Stand-up Comedian | 1200 | greedy;math |
| - | -0.0547 | 1878A How Much Does Daytona Cost? | 800 | greedy |
| - | -0.0543 | 1553B Reverse String | 1300 | brute force;dp;hashing;implementation;strings |

_Plain-language reading:_ TODO

## Axis 11  (sigma = 43.76)

- enriched at `+` end: trees (z=+8.6), data structures (z=+7.1), probabilities (z=+6.1), divide and conquer (z=+6.0), dfs and similar (z=+5.6)
- enriched at `-` end: math (z=-3.6), greedy (z=-3.4), constructive algorithms (z=-2.5), games (z=-2.4), number theory (z=-1.3)
- corr(loading, problem rating) = +0.23; mean rating of `+` end 1213, of `-` end 1320
- user scores: std 0.227

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.0943 | 1872D Plus Minus Permutation | 1200 | math |
| + | +0.0858 | 1927D Find the Different Ones! | 1300 | binary search;brute force;data structures;dp;dsu;greedy;two pointers |
| + | +0.0772 | 1741C Minimize the Thickness | 1100 | brute force;greedy;math;two pointers |
| + | +0.0738 | 1857C Assembly via Minimums | 1200 | greedy;sortings |
| + | +0.0699 | 1931E Anna and the Valentine's Day Gift | 1400 | games;greedy;math;sortings |
| + | +0.0696 | 1742E Scuza | 1200 | binary search;greedy;math |
| + | +0.0639 | 1873E Building an Aquarium | 1100 | binary search;sortings |
| + | +0.0616 | 1851C Tiles Comeback | 1000 | greedy |
| + | +0.0613 | 1862D Ice Cream Balls | 1300 | binary search;combinatorics;constructive algorithms;math |
| + | +0.0591 | 1703D Double Strings | 1100 | brute force;data structures;strings |
| + | +0.0587 | 1760E Binary Inversions | 1100 | data structures;greedy;math |
| + | +0.0579 | 1684C Column Swapping | 1400 | brute force;constructive algorithms;greedy;implementation;sortings |
| + | +0.0574 | 1933E Turtle vs. Rabbit Race: Optimal Trainings | 1500 | binary search;implementation;math;ternary search |
| + | +0.0572 | 1882B Sets and Union | 1300 | bitmasks;brute force;constructive algorithms;greedy |
| + | +0.0566 | 1800B Count the Number of Pairs | 1000 | greedy;strings |
| - | -0.1028 | 1929C Sasha and the Casino | 1400 | binary search;brute force;constructive algorithms;games;greedy;math |
| - | -0.0961 | 1979C Earning on Bets | 1200 | binary search;combinatorics;constructive algorithms;number theory |
| - | -0.0951 | 1983B Corner Twist | 1200 | constructive algorithms;greedy;implementation;math |
| - | -0.0923 | 1987C Basil's Garden | 1200 | dp;greedy |
| - | -0.0903 | 1996D Fun | 1500 | binary search;brute force;combinatorics;math;number theory |
| - | -0.0880 | 1883F You Are So Beautiful | 1400 | data structures |
| - | -0.0861 | 1977B Binary Colouring | 1100 | bitmasks;constructive algorithms;greedy;math |
| - | -0.0861 | 2007C Dora and C++ | 1500 | math;number theory |
| - | -0.0798 | 1991C Absolute Zero | 1300 | constructive algorithms;greedy;math |
| - | -0.0795 | 1985E Secret Box | 1200 | brute force;combinatorics;math |
| - | -0.0774 | 2000E Photoshoot for Gorillas | 1400 | combinatorics;data structures;greedy;math |
| - | -0.0750 | 1774C Ice and Fire | 1300 | constructive algorithms;dp;greedy |
| - | -0.0741 | 1993C Light Switches | 1400 | implementation;math |
| - | -0.0714 | 1883G1 Dances (Easy version) | 1400 | binary search;greedy;two pointers |
| - | -0.0694 | 1984C1 Magnitude (Easy Version) | 1300 | dp;greedy;math |

_Plain-language reading:_ TODO

## Axis 12  (sigma = 42.76)

- enriched at `+` end: string suffix structures (z=+1.5), greedy (z=+1.3), fft (z=+1.3), games (z=+0.7), graph matchings (z=+0.6)
- enriched at `-` end: dfs and similar (z=-2.8), math (z=-2.7), trees (z=-2.0), binary search (z=-1.8), two pointers (z=-1.7)
- corr(loading, problem rating) = +0.00; mean rating of `+` end 1100, of `-` end 1033
- user scores: std 0.224

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.1211 | 2061B Kevin and Geometry | 1100 | binary search;geometry |
| + | +0.0931 | 1722D Line | 1100 | greedy;sortings |
| + | +0.0892 | 2000C Numeric String Template | 1000 | data structures;strings |
| + | +0.0761 | 1742E Scuza | 1200 | binary search;greedy;math |
| + | +0.0711 | 2118B Make It Permutation | 1200 | constructive algorithms |
| + | +0.0674 | 1931C Make Equal Again | 1000 | brute force;greedy;math |
| + | +0.0650 | 1712C Sort Zero | 1100 | greedy;sortings |
| + | +0.0626 | 1918B Minimize Inversions | 900 | constructive algorithms;data structures;greedy;implementation;sortings |
| + | +0.0625 | 1791G1 Teleporters (Easy Version) | 1100 | greedy;sortings |
| + | +0.0618 | 1790E Vlad and a Pair of Numbers | 1400 | bitmasks;constructive algorithms |
| + | +0.0597 | 1759C Thermostat | 1100 | greedy;math;shortest paths |
| + | +0.0596 | 1927C Choose the Different Ones! | 1000 | brute force;greedy;math |
| + | +0.0577 | 1926C Vlad and a Sum of Sum of Digits | 1200 | dp;implementation |
| + | +0.0577 | 1762B Make Array Good | 1100 | constructive algorithms;implementation;number theory;sortings |
| + | +0.0575 | 1721B Deadly Laser | 1000 | implementation |
| - | -0.0945 | 1800A Is It a Cat? | 800 | implementation;strings |
| - | -0.0799 | 1551A Polycarp and Coins | 800 | greedy;math |
| - | -0.0792 | 1579A Casimir's String Solitaire | 800 | math;strings |
| - | -0.0790 | 1927E Klever Permutation | 1400 | constructive algorithms;math;two pointers |
| - | -0.0762 | 1567A Domino Disaster | 800 | implementation;strings |
| - | -0.0756 | 1560A Dislike of Threes | 800 | implementation |
| - | -0.0685 | 1931E Anna and the Valentine's Day Gift | 1400 | games;greedy;math;sortings |
| - | -0.0667 | 2075C Two Colors | 1500 | binary search;combinatorics;math |
| - | -0.0653 | 2061D Kevin and Numbers | 1600 | bitmasks;data structures |
| - | -0.0644 | 1535A Fair Playoff | 800 | brute force;implementation |
| - | -0.0643 | 1542A Odd Set | 800 | math |
| - | -0.0637 | 1552A Subsequence Permutation | 800 | sortings;strings |
| - | -0.0634 | 1611A Make Even | 800 | constructive algorithms;math |
| - | -0.0627 | 1553A Digits Sum | 800 | math;number theory |
| - | -0.0626 | 1766D Lucky Chains | 1600 | math;number theory |

_Plain-language reading:_ TODO

## Axis 13  (sigma = 41.60)

- enriched at `+` end: dfs and similar (z=+4.0), graphs (z=+3.2), trees (z=+3.2), shortest paths (z=+2.8), meet-in-the-middle (z=+2.6)
- enriched at `-` end: two pointers (z=-3.1), number theory (z=-2.7), binary search (z=-2.6), math (z=-2.0), combinatorics (z=-1.3)
- corr(loading, problem rating) = +0.03; mean rating of `+` end 1280, of `-` end 1273
- user scores: std 0.214

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.1544 | 1684C Column Swapping | 1400 | brute force;constructive algorithms;greedy;implementation;sortings |
| + | +0.1293 | 1633C Kill the Monster | 1100 | brute force;math |
| + | +0.1029 | 1738B Prefix Sum Addicts | 1200 | constructive algorithms;greedy;math;sortings |
| + | +0.0904 | 1774B Coloring | 1500 | constructive algorithms;greedy;math |
| + | +0.0903 | 1909I Short Permutation Problem | 1900 | combinatorics;dp;fft;math |
| + | +0.0721 | 1932B Chaya Calendar | 1100 | number theory |
| + | +0.0704 | 2075B Array Recoloring | 1300 | constructive algorithms;greedy |
| + | +0.0617 | 2128B Deque Process | 1100 | constructive algorithms;greedy;sortings;two pointers |
| + | +0.0613 | 2127B Hamiiid, Haaamid... Hamid? | 1300 | games;greedy |
| + | +0.0608 | 1778B The Forbidden Permutation | 1300 | greedy;math |
| + | +0.0604 | 1739B Array Recovery | 1100 | constructive algorithms;greedy;math |
| + | +0.0600 | 1792B Stand-up Comedian | 1200 | greedy;math |
| + | +0.0594 | 2153C Symmetrical Polygons | 1500 | constructive algorithms;geometry;greedy;implementation;sortings |
| + | +0.0594 | 2013C Password Cracking | 1400 | constructive algorithms;interactive;strings |
| + | +0.0537 | 1741A Compare T-Shirt Sizes | 800 | implementation;strings |
| - | -0.0888 | 1996D Fun | 1500 | binary search;brute force;combinatorics;math;number theory |
| - | -0.0826 | 2119B Line Segments | 1200 | geometry;greedy;math |
| - | -0.0825 | 1927D Find the Different Ones! | 1300 | binary search;brute force;data structures;dp;dsu;greedy;two pointers |
| - | -0.0825 | 2117D Retaliation | 1200 | binary search;math;number theory |
| - | -0.0728 | 2118B Make It Permutation | 1200 | constructive algorithms |
| - | -0.0690 | 1873E Building an Aquarium | 1100 | binary search;sortings |
| - | -0.0638 | 1921D Very Different Array | 1100 | data structures;greedy;sortings;two pointers |
| - | -0.0622 | 1915E Romantic Glasses | 1300 | data structures;greedy;math |
| - | -0.0606 | 2122C Manhattan Pairs | 1700 | constructive algorithms;geometry;greedy;math;sortings |
| - | -0.0593 | 1932C LR-remainders | 1400 | brute force;data structures;implementation;math;two pointers |
| - | -0.0591 | 1931D Divisible Pairs | 1300 | combinatorics;math;number theory |
| - | -0.0590 | 1907C Removal of Unattractive Pairs | 1200 | constructive algorithms;greedy;math;strings |
| - | -0.0586 | 1980D GCD-sequence | 1400 | greedy;implementation;math;number theory |
| - | -0.0583 | 1858C Yet Another Permutation Problem | 1000 | constructive algorithms;greedy;math;number theory |
| - | -0.0581 | 1987C Basil's Garden | 1200 | dp;greedy |

_Plain-language reading:_ TODO

## Axis 14  (sigma = 40.03)

- enriched at `+` end: sortings (z=+2.4), constructive algorithms (z=+2.2), string suffix structures (z=+1.7), greedy (z=+1.5), strings (z=+1.5)
- enriched at `-` end: 2-sat (z=-2.7), math (z=-2.5), dp (z=-2.5), data structures (z=-2.1), dfs and similar (z=-1.9)
- corr(loading, problem rating) = -0.02; mean rating of `+` end 1080, of `-` end 1247
- user scores: std 0.209

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.0826 | 2000D Right Left Wrong | 1200 | greedy;implementation;two pointers |
| + | +0.0763 | 1999D Slavic's Exam | 1100 | greedy;implementation;strings |
| + | +0.0762 | 1844C Particles | 1300 | dp;greedy;implementation;math |
| + | +0.0742 | 1921D Very Different Array | 1100 | data structures;greedy;sortings;two pointers |
| + | +0.0688 | 1997B Make Three Regions | 1100 | constructive algorithms;two pointers |
| + | +0.0654 | 1762C Binary Strings are Fun | 1400 | combinatorics;math |
| + | +0.0643 | 1807A Plus or Minus | 800 | implementation |
| + | +0.0628 | 1914E2 Game with Marbles (Hard Version) | 1400 | games;greedy;sortings |
| + | +0.0615 | 1829A Love Story | 800 | implementation;strings |
| + | +0.0602 | 1829B Blank Space | 800 | implementation |
| + | +0.0601 | 1985C Good Prefixes | 1000 | greedy |
| + | +0.0599 | 2072C Creating Keys for StORages Has Become My Main Skill | 1200 | bitmasks;constructive algorithms;greedy |
| + | +0.0599 | 1807B Grab the Candies | 800 | greedy |
| + | +0.0598 | 2128B Deque Process | 1100 | constructive algorithms;greedy;sortings;two pointers |
| + | +0.0596 | 2004C Splitting Items | 1100 | games;greedy;sortings |
| - | -0.1039 | 2000E Photoshoot for Gorillas | 1400 | combinatorics;data structures;greedy;math |
| - | -0.0902 | 2117D Retaliation | 1200 | binary search;math;number theory |
| - | -0.0774 | 2119B Line Segments | 1200 | geometry;greedy;math |
| - | -0.0718 | 1807G2 Subsequence Addition (Hard Version) | 1100 | bitmasks;dp;greedy;implementation;sortings |
| - | -0.0688 | 2126E G-C-D, Unlucky! | 1400 | math;number theory |
| - | -0.0670 | 1829E The Lakes | 1100 | dfs and similar;dsu;graphs;implementation |
| - | -0.0666 | 1843D Apple Tree | 1200 | combinatorics;dfs and similar;dp;math;trees |
| - | -0.0659 | 1850F We Were Both Children | 1300 | brute force;implementation;math;number theory |
| - | -0.0655 | 1980D GCD-sequence | 1400 | greedy;implementation;math;number theory |
| - | -0.0654 | 1807G1 Subsequence Addition (Easy Version) | 1100 | brute force;data structures;dp;greedy;implementation;sortings |
| - | -0.0653 | 1791D Distinct Split | 1000 | brute force;greedy;strings |
| - | -0.0637 | 1829F Forever Winter | 1300 | dfs and similar;graphs;math |
| - | -0.0611 | 1997D Maximize the Root | 1500 | binary search;dfs and similar;dp;greedy;trees |
| - | -0.0589 | 1986D Mathematical Problem | 1400 | brute force;dp;greedy;implementation;math;two pointers |
| - | -0.0578 | 1791G1 Teleporters (Easy Version) | 1100 | greedy;sortings |

_Plain-language reading:_ TODO

## Axis 15  (sigma = 39.41)

- enriched at `+` end: dp (z=+6.0), data structures (z=+4.6), divide and conquer (z=+3.2), binary search (z=+2.3), trees (z=+2.3)
- enriched at `-` end: constructive algorithms (z=-2.1), implementation (z=-1.5), meet-in-the-middle (z=-1.4), probabilities (z=-0.9), games (z=-0.9)
- corr(loading, problem rating) = +0.07; mean rating of `+` end 1227, of `-` end 1260
- user scores: std 0.206

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.1301 | 1807G1 Subsequence Addition (Easy Version) | 1100 | brute force;data structures;dp;greedy;implementation;sortings |
| + | +0.1266 | 1807G2 Subsequence Addition (Hard Version) | 1100 | bitmasks;dp;greedy;implementation;sortings |
| + | +0.1196 | 1844C Particles | 1300 | dp;greedy;implementation;math |
| + | +0.0981 | 1811C Restore the Array | 1100 | constructive algorithms;greedy |
| + | +0.0837 | 1857D Strong Vertices | 1300 | math;sortings;trees |
| + | +0.0764 | 1844D Row Major | 1400 | constructive algorithms;greedy;math;number theory;strings |
| + | +0.0750 | 1800C2 Powering the Hero (hard version) | 1100 | data structures;greedy |
| + | +0.0676 | 1840B Binary Cafe | 1100 | bitmasks;combinatorics;math |
| + | +0.0615 | 1996D Fun | 1500 | binary search;brute force;combinatorics;math;number theory |
| + | +0.0607 | 1791E Negatives and Positives | 1100 | dp;greedy;sortings |
| + | +0.0599 | 1846D Rudolph and Christmas Tree | 1200 | constructive algorithms;geometry;math |
| + | +0.0589 | 2137D Replace with Occurrences | 1200 | constructive algorithms |
| + | +0.0575 | 1800C1 Powering the Hero (easy version) | 1000 | data structures;greedy |
| + | +0.0573 | 2059D Graph and Graph | 1900 | data structures;graphs;greedy;shortest paths |
| + | +0.0572 | 1809B Points on Plane | 1000 | binary search;greedy;math |
| - | -0.1057 | 1846B Rudolph and Tic-Tac-Toe | 800 | brute force;implementation;strings |
| - | -0.1019 | 1807E Interview | 1300 | binary search;implementation;interactive |
| - | -0.0735 | 2164B Even Modulo Pair | 1000 | brute force;math;number theory |
| - | -0.0730 | 2061B Kevin and Geometry | 1100 | binary search;geometry |
| - | -0.0718 | 2059B Cost of the Array | 1300 | brute force;constructive algorithms;greedy;math |
| - | -0.0717 | 1998A Find K Distinct Points with Fixed Center | 800 | constructive algorithms;implementation;math |
| - | -0.0705 | 1931E Anna and the Valentine's Day Gift | 1400 | games;greedy;math;sortings |
| - | -0.0687 | 1909I Short Permutation Problem | 1900 | combinatorics;dp;fft;math |
| - | -0.0677 | 1800E1 Unforgivable Curse (easy version) | 1400 | brute force;constructive algorithms;dsu;graphs;greedy;strings |
| - | -0.0665 | 1920B Summation Game | 1100 | games;greedy;math;sortings |
| - | -0.0633 | 1927E Klever Permutation | 1400 | constructive algorithms;math;two pointers |
| - | -0.0626 | 1800E2 Unforgivable Curse (hard version) | 1500 | brute force;constructive algorithms;dfs and similar;dsu;graphs;greedy;strings |
| - | -0.0597 | 2049B pspspsps | 1300 | brute force;constructive algorithms;graph matchings;implementation |
| - | -0.0565 | 1556B Take Your Places! | 1300 | implementation |
| - | -0.0561 | 1931D Divisible Pairs | 1300 | combinatorics;math;number theory |

_Plain-language reading:_ TODO

## Axis 16  (sigma = 38.88)

- enriched at `+` end: two pointers (z=+2.5), graph matchings (z=+2.4), 2-sat (z=+2.2), binary search (z=+2.1), meet-in-the-middle (z=+1.7)
- enriched at `-` end: greedy (z=-2.4), constructive algorithms (z=-2.2), probabilities (z=-1.1), trees (z=-1.1), dp (z=-1.1)
- corr(loading, problem rating) = +0.02; mean rating of `+` end 1180, of `-` end 1127
- user scores: std 0.203

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.1046 | 1684C Column Swapping | 1400 | brute force;constructive algorithms;greedy;implementation;sortings |
| + | +0.1005 | 1807A Plus or Minus | 800 | implementation |
| + | +0.0915 | 1807B Grab the Candies | 800 | greedy |
| + | +0.0905 | 1996D Fun | 1500 | binary search;brute force;combinatorics;math;number theory |
| + | +0.0846 | 1807E Interview | 1300 | binary search;implementation;interactive |
| + | +0.0763 | 2119B Line Segments | 1200 | geometry;greedy;math |
| + | +0.0737 | 1878E Iva & Pav | 1400 | binary search;bitmasks;data structures;greedy |
| + | +0.0717 | 2008F Sakurako's Box | 1400 | combinatorics;math;number theory |
| + | +0.0716 | 1991C Absolute Zero | 1300 | constructive algorithms;greedy;math |
| + | +0.0697 | 1996C Sort | 1200 | dp;greedy;sortings;strings |
| + | +0.0691 | 1633C Kill the Monster | 1100 | brute force;math |
| + | +0.0686 | 1987C Basil's Garden | 1200 | dp;greedy |
| + | +0.0686 | 1811A Insert Digit | 800 | greedy;math;strings |
| + | +0.0679 | 2118B Make It Permutation | 1200 | constructive algorithms |
| + | +0.0662 | 1739B Array Recovery | 1100 | constructive algorithms;greedy;math |
| - | -0.2049 | 1807G2 Subsequence Addition (Hard Version) | 1100 | bitmasks;dp;greedy;implementation;sortings |
| - | -0.1840 | 1807G1 Subsequence Addition (Easy Version) | 1100 | brute force;data structures;dp;greedy;implementation;sortings |
| - | -0.1148 | 1783B Matrix of Differences | 1100 | constructive algorithms;math |
| - | -0.1135 | 1811C Restore the Array | 1100 | constructive algorithms;greedy |
| - | -0.0961 | 1791E Negatives and Positives | 1100 | dp;greedy;sortings |
| - | -0.0941 | 1844C Particles | 1300 | dp;greedy;implementation;math |
| - | -0.0889 | 1809B Points on Plane | 1000 | binary search;greedy;math |
| - | -0.0879 | 1774C Ice and Fire | 1300 | constructive algorithms;dp;greedy |
| - | -0.0809 | 2075B Array Recoloring | 1300 | constructive algorithms;greedy |
| - | -0.0779 | 1747C Swap Game | 1200 | games |
| - | -0.0725 | 1758B XOR = Average | 900 | constructive algorithms |
| - | -0.0696 | 1761B Elimination of a Ring | 1000 | constructive algorithms;greedy;implementation |
| - | -0.0676 | 1840B Binary Cafe | 1100 | bitmasks;combinatorics;math |
| - | -0.0673 | 1791G1 Teleporters (Easy Version) | 1100 | greedy;sortings |
| - | -0.0621 | 1907C Removal of Unattractive Pairs | 1200 | constructive algorithms;greedy;math;strings |

_Plain-language reading:_ TODO

## Axis 17  (sigma = 37.38)

- enriched at `+` end: data structures (z=+3.7), brute force (z=+3.2), dp (z=+3.1), sortings (z=+2.7), string suffix structures (z=+2.4)
- enriched at `-` end: geometry (z=-3.1), math (z=-2.7), constructive algorithms (z=-2.1), ternary search (z=-1.7), interactive (z=-1.5)
- corr(loading, problem rating) = +0.01; mean rating of `+` end 1273, of `-` end 1193
- user scores: std 0.196

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.1575 | 1633C Kill the Monster | 1100 | brute force;math |
| + | +0.1246 | 1684C Column Swapping | 1400 | brute force;constructive algorithms;greedy;implementation;sortings |
| + | +0.1065 | 1807G2 Subsequence Addition (Hard Version) | 1100 | bitmasks;dp;greedy;implementation;sortings |
| + | +0.1019 | 1807G1 Subsequence Addition (Easy Version) | 1100 | brute force;data structures;dp;greedy;implementation;sortings |
| + | +0.0908 | 1883F You Are So Beautiful | 1400 | data structures |
| + | +0.0835 | 1921D Very Different Array | 1100 | data structures;greedy;sortings;two pointers |
| + | +0.0821 | 1840D Wooden Toy Festival | 1400 | binary search;greedy;sortings |
| + | +0.0784 | 2091E Interesting Ratio | 1300 | brute force;math;number theory;two pointers |
| + | +0.0762 | 1980D GCD-sequence | 1400 | greedy;implementation;math;number theory |
| + | +0.0712 | 1883G1 Dances (Easy version) | 1400 | binary search;greedy;two pointers |
| + | +0.0698 | 1926C Vlad and a Sum of Sum of Digits | 1200 | dp;implementation |
| + | +0.0623 | 1857F Sum and Product | 1600 | binary search;data structures;math |
| + | +0.0606 | 1846B Rudolph and Tic-Tac-Toe | 800 | brute force;implementation;strings |
| + | +0.0604 | 2061D Kevin and Numbers | 1600 | bitmasks;data structures |
| + | +0.0601 | 1985E Secret Box | 1200 | brute force;combinatorics;math |
| - | -0.1501 | 2061B Kevin and Geometry | 1100 | binary search;geometry |
| - | -0.0913 | 1857C Assembly via Minimums | 1200 | greedy;sortings |
| - | -0.0902 | 1881C Perfect Square | 1200 | brute force;implementation |
| - | -0.0889 | 1846D Rudolph and Christmas Tree | 1200 | constructive algorithms;geometry;math |
| - | -0.0872 | 1792B Stand-up Comedian | 1200 | greedy;math |
| - | -0.0864 | 1862D Ice Cream Balls | 1300 | binary search;combinatorics;constructive algorithms;math |
| - | -0.0762 | 2118B Make It Permutation | 1200 | constructive algorithms |
| - | -0.0761 | 2123D Binary String Battle | 1200 | constructive algorithms;games;greedy |
| - | -0.0720 | 1886B Fear of the Dark | 1200 | binary search;geometry;math |
| - | -0.0718 | 1927E Klever Permutation | 1400 | constructive algorithms;math;two pointers |
| - | -0.0697 | 1736B Playing with GCD | 1200 | math;number theory |
| - | -0.0673 | 1862C Flower City Fence | 1100 | binary search;data structures;implementation;sortings |
| - | -0.0670 | 1883C Raspberries | 1000 | dp;math |
| - | -0.0670 | 1872D Plus Minus Permutation | 1200 | math |
| - | -0.0645 | 1983B Corner Twist | 1200 | constructive algorithms;greedy;implementation;math |

_Plain-language reading:_ TODO

## Axis 18  (sigma = 36.91)

- enriched at `+` end: math (z=+2.6), probabilities (z=+2.4), geometry (z=+1.5), strings (z=+1.3), matrices (z=+1.3)
- enriched at `-` end: sortings (z=-4.2), trees (z=-3.2), fft (z=-2.9), divide and conquer (z=-2.3), graph matchings (z=-1.9)
- corr(loading, problem rating) = -0.02; mean rating of `+` end 1233, of `-` end 1200
- user scores: std 0.193

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.1402 | 1980C Sofia and the Lost Operations | 1300 | constructive algorithms;greedy |
| + | +0.1159 | 1955C Inhabitant of the Deep Sea | 1300 | greedy;implementation;math |
| + | +0.0928 | 1691C Sum of Substrings | 1400 | brute force;constructive algorithms;greedy;math;strings |
| + | +0.0900 | 1935B Informatics in MAC | 1200 | constructive algorithms |
| + | +0.0875 | 1927D Find the Different Ones! | 1300 | binary search;brute force;data structures;dp;dsu;greedy;two pointers |
| + | +0.0857 | 1955D Inaccurate Subsequence Search | 1400 | data structures;two pointers |
| + | +0.0838 | 1792B Stand-up Comedian | 1200 | greedy;math |
| + | +0.0814 | 2119B Line Segments | 1200 | geometry;greedy;math |
| + | +0.0808 | 1637C Andrew and Stones | 1200 | greedy;implementation |
| + | +0.0795 | 1837D Bracket Coloring | 1400 | constructive algorithms;greedy |
| + | +0.0716 | 2164B Even Modulo Pair | 1000 | brute force;math;number theory |
| + | +0.0714 | 1555A PizzaForces | 900 | brute force;math |
| + | +0.0704 | 2118B Make It Permutation | 1200 | constructive algorithms |
| + | +0.0674 | 1656B Subtract Operation | 1100 | data structures;greedy;math;two pointers |
| + | +0.0652 | 1634B Fortune Telling | 1400 | bitmasks;math |
| - | -0.0943 | 1979C Earning on Bets | 1200 | binary search;combinatorics;constructive algorithms;number theory |
| - | -0.0861 | 1914E2 Game with Marbles (Hard Version) | 1400 | games;greedy;sortings |
| - | -0.0824 | 1914E1 Game with Marbles (Easy Version) | 1400 | brute force;games;greedy;sortings |
| - | -0.0794 | 1703D Double Strings | 1100 | brute force;data structures;strings |
| - | -0.0774 | 1551B2 Wonderful Coloring - 2 | 1400 | binary search;constructive algorithms;data structures;greedy |
| - | -0.0714 | 1741C Minimize the Thickness | 1100 | brute force;greedy;math;two pointers |
| - | -0.0687 | 1844C Particles | 1300 | dp;greedy;implementation;math |
| - | -0.0686 | 1987C Basil's Garden | 1200 | dp;greedy |
| - | -0.0675 | 1742E Scuza | 1200 | binary search;greedy;math |
| - | -0.0673 | 1742D Coprime | 1100 | brute force;greedy;number theory |
| - | -0.0671 | 1998A Find K Distinct Points with Fixed Center | 800 | constructive algorithms;implementation;math |
| - | -0.0630 | 2055C The Trail | 1400 | brute force;constructive algorithms;greedy;math;two pointers |
| - | -0.0622 | 1557B Moamen and k-subarrays | 1100 | greedy;sortings |
| - | -0.0609 | 1807G1 Subsequence Addition (Easy Version) | 1100 | brute force;data structures;dp;greedy;implementation;sortings |
| - | -0.0590 | 1553C Penalty | 1200 | bitmasks;brute force;dp;greedy |

_Plain-language reading:_ TODO

## Axis 19  (sigma = 36.32)

- enriched at `+` end: geometry (z=+2.4), math (z=+2.4), implementation (z=+1.9), interactive (z=+1.7), constructive algorithms (z=+1.7)
- enriched at `-` end: dp (z=-2.8), sortings (z=-2.4), shortest paths (z=-2.1), graphs (z=-1.9), games (z=-1.9)
- corr(loading, problem rating) = -0.02; mean rating of `+` end 1207, of `-` end 1280
- user scores: std 0.190

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.1694 | 2059B Cost of the Array | 1300 | brute force;constructive algorithms;greedy;math |
| + | +0.1599 | 2061B Kevin and Geometry | 1100 | binary search;geometry |
| + | +0.1248 | 1998A Find K Distinct Points with Fixed Center | 800 | constructive algorithms;implementation;math |
| + | +0.1195 | 1983B Corner Twist | 1200 | constructive algorithms;greedy;implementation;math |
| + | +0.1105 | 1846D Rudolph and Christmas Tree | 1200 | constructive algorithms;geometry;math |
| + | +0.0891 | 1862D Ice Cream Balls | 1300 | binary search;combinatorics;constructive algorithms;math |
| + | +0.0821 | 2043B Digits | 1100 | math;number theory |
| + | +0.0816 | 1977B Binary Colouring | 1100 | bitmasks;constructive algorithms;greedy;math |
| + | +0.0790 | 1846E1 Rudolf and Snowflakes (simple version) | 1300 | brute force;implementation;math |
| + | +0.0759 | 1979C Earning on Bets | 1200 | binary search;combinatorics;constructive algorithms;number theory |
| + | +0.0696 | 2048C Kevin and Binary Strings | 1200 | bitmasks;brute force;greedy;implementation;strings |
| + | +0.0696 | 2075B Array Recoloring | 1300 | constructive algorithms;greedy |
| + | +0.0677 | 2049B pspspsps | 1300 | brute force;constructive algorithms;graph matchings;implementation |
| + | +0.0674 | 1986D Mathematical Problem | 1400 | brute force;dp;greedy;implementation;math;two pointers |
| + | +0.0654 | 1703F Yet Another Problem About Pairs Satisfying an Inequality | 1300 | binary search;data structures;dp;greedy;sortings |
| - | -0.1139 | 1633C Kill the Monster | 1100 | brute force;math |
| - | -0.1046 | 1846B Rudolph and Tic-Tac-Toe | 800 | brute force;implementation;strings |
| - | -0.0956 | 1921D Very Different Array | 1100 | data structures;greedy;sortings;two pointers |
| - | -0.0940 | 2000D Right Left Wrong | 1200 | greedy;implementation;two pointers |
| - | -0.0903 | 1999D Slavic's Exam | 1100 | greedy;implementation;strings |
| - | -0.0850 | 1684C Column Swapping | 1400 | brute force;constructive algorithms;greedy;implementation;sortings |
| - | -0.0815 | 2060E Graph Composition | 1500 | dfs and similar;dsu;graphs;greedy |
| - | -0.0803 | 1931D Divisible Pairs | 1300 | combinatorics;math;number theory |
| - | -0.0763 | 2069C Beautiful Sequence | 1500 | combinatorics;dp;greedy;two pointers |
| - | -0.0740 | 2059D Graph and Graph | 1900 | data structures;graphs;greedy;shortest paths |
| - | -0.0651 | 2061C Kevin and Puzzle | 1600 | 2-sat;combinatorics;dp |
| - | -0.0643 | 1986C Update Queries | 1100 | data structures;greedy;sortings |
| - | -0.0569 | 2149D A and B | 1200 | strings |
| - | -0.0557 | 2050E Three Strings | 1500 | dp;implementation;strings |
| - | -0.0555 | 1985D Manhattan Circle | 900 | implementation;math |

_Plain-language reading:_ TODO

## Axis 20  (sigma = 36.06)

- enriched at `+` end: constructive algorithms (z=+3.1), brute force (z=+2.0), greedy (z=+1.8), 2-sat (z=+1.8), math (z=+1.7)
- enriched at `-` end: combinatorics (z=-2.2), implementation (z=-1.8), data structures (z=-1.5), geometry (z=-1.4), meet-in-the-middle (z=-1.3)
- corr(loading, problem rating) = -0.01; mean rating of `+` end 1227, of `-` end 1227
- user scores: std 0.188

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.1084 | 1929C Sasha and the Casino | 1400 | binary search;brute force;constructive algorithms;games;greedy;math |
| + | +0.0976 | 2000C Numeric String Template | 1000 | data structures;strings |
| + | +0.0948 | 2059B Cost of the Array | 1300 | brute force;constructive algorithms;greedy;math |
| + | +0.0880 | 1739B Array Recovery | 1100 | constructive algorithms;greedy;math |
| + | +0.0842 | 1791G1 Teleporters (Easy Version) | 1100 | greedy;sortings |
| + | +0.0740 | 1983B Corner Twist | 1200 | constructive algorithms;greedy;implementation;math |
| + | +0.0694 | 1792B Stand-up Comedian | 1200 | greedy;math |
| + | +0.0690 | 1778B The Forbidden Permutation | 1300 | greedy;math |
| + | +0.0679 | 2030C A TRUE Battle | 1100 | brute force;games;greedy |
| + | +0.0670 | 1984C2 Magnitude (Hard Version) | 1700 | combinatorics;dp;greedy;math |
| + | +0.0668 | 1942C2 Bessie's Birthday Cake (Hard Version) | 1700 | geometry;greedy;math |
| + | +0.0667 | 1791D Distinct Split | 1000 | brute force;greedy;strings |
| + | +0.0605 | 1833D Flipper | 1400 | brute force;constructive algorithms;greedy |
| + | +0.0600 | 1849A Morning Sandwich | 800 | implementation;math |
| + | +0.0579 | 1760E Binary Inversions | 1100 | data structures;greedy;math |
| - | -0.1043 | 2000E Photoshoot for Gorillas | 1400 | combinatorics;data structures;greedy;math |
| - | -0.0934 | 1846C Rudolf and the Another Competition | 1200 | constructive algorithms;data structures;dp;greedy;sortings |
| - | -0.0903 | 1684C Column Swapping | 1400 | brute force;constructive algorithms;greedy;implementation;sortings |
| - | -0.0892 | 2061B Kevin and Geometry | 1100 | binary search;geometry |
| - | -0.0808 | 1909I Short Permutation Problem | 1900 | combinatorics;dp;fft;math |
| - | -0.0774 | 1850E Cardboard for Pictures | 1100 | binary search;geometry;implementation;math |
| - | -0.0726 | 1873F Money Trees | 1300 | binary search;greedy;math;two pointers |
| - | -0.0703 | 1850F We Were Both Children | 1300 | brute force;implementation;math;number theory |
| - | -0.0700 | 1637C Andrew and Stones | 1200 | greedy;implementation |
| - | -0.0664 | 1883F You Are So Beautiful | 1400 | data structures |
| - | -0.0640 | 1721C Min-Max Array Transformation | 1400 | binary search;greedy;two pointers |
| - | -0.0639 | 1980C Sofia and the Lost Operations | 1300 | constructive algorithms;greedy |
| - | -0.0627 | 1791A Codeforces Checking | 800 | implementation;strings |
| - | -0.0607 | 1791B Following Directions | 800 | geometry;implementation |
| - | -0.0605 | 1800A Is It a Cat? | 800 | implementation;strings |

_Plain-language reading:_ TODO
