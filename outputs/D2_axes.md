# D2 - Skill-axis table

20 of 20 components are significant against the permutation null.

Sign of each axis is arbitrary. `+` rows = highest loading problems, `-` rows = lowest.
Tag enrichment z > 0 means problems with the tag load positively on the axis.
`corr(loading, rating)` close to +-1 means the axis is mostly *difficulty* (or the division the
problem was set for), not a topic; look for axes with low |corr| and strong tag enrichment.

## Axis 1  (sigma = 113.12)

- enriched at `+` end: implementation (z=+5.8), strings (z=+4.2), greedy (z=+3.4), sortings (z=+1.6), games (z=+0.4)
- enriched at `-` end: dfs and similar (z=-22.6), trees (z=-21.4), divide and conquer (z=-20.9), dp (z=-19.8), graphs (z=-19.7)
- corr(loading, problem rating) = -0.47; mean rating of `+` end 840, of `-` end 1200
- user scores: std 0.420

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.0880 | 1986C Update Queries | 1100 | data structures;greedy;sortings |
| + | +0.0842 | 1999D Slavic's Exam | 1100 | greedy;implementation;strings |
| + | +0.0821 | 1850A To My Critics | 800 | implementation;sortings |
| + | +0.0791 | 1791A Codeforces Checking | 800 | implementation;strings |
| + | +0.0788 | 1850C Word on the Paper | 800 | implementation;strings |
| + | +0.0770 | 1873A Short Sort | 800 | brute force;implementation |
| + | +0.0767 | 1850B Ten Words of Wisdom | 800 | implementation;sortings |
| + | +0.0749 | 1873B Good Kid | 800 | brute force;greedy;math |
| + | +0.0742 | 1791B Following Directions | 800 | geometry;implementation |
| + | +0.0740 | 1807A Plus or Minus | 800 | implementation |
| + | +0.0737 | 1918A Brick Wall | 800 | constructive algorithms;greedy;implementation;math |
| + | +0.0732 | 1927A Make it White | 800 | greedy;strings |
| + | +0.0730 | 1742A Sum | 800 | implementation |
| + | +0.0725 | 1872A Two Vessels | 800 | brute force;greedy;math |
| + | +0.0717 | 1915A Odd One Out | 800 | bitmasks;implementation |
| - | -0.0518 | 1883F You Are So Beautiful | 1400 | data structures |
| - | -0.0457 | 1883G1 Dances (Easy version) | 1400 | binary search;greedy;two pointers |
| - | -0.0416 | 1998A Find K Distinct Points with Fixed Center | 800 | constructive algorithms;implementation;math |
| - | -0.0300 | 1921D Very Different Array | 1100 | data structures;greedy;sortings;two pointers |
| - | -0.0290 | 1925B A Balanced Problemset? | 1200 | brute force;greedy;math;number theory |
| - | -0.0283 | 2164B Even Modulo Pair | 1000 | brute force;math;number theory |
| - | -0.0267 | 1879C Make it Alternating | 1300 | combinatorics;dp;greedy |
| - | -0.0252 | 1807E Interview | 1300 | binary search;implementation;interactive |
| - | -0.0226 | 1907D Jumping Through Segments | 1400 | binary search;constructive algorithms |
| - | -0.0217 | 1742D Coprime | 1100 | brute force;greedy;number theory |
| - | -0.0213 | 1676G White-Black Balanced Subtrees | 1300 | dfs and similar;dp;graphs;trees |
| - | -0.0209 | 2132B The Secret Number | 900 | math |
| - | -0.0208 | 1870C Colorful Table | 1300 | binary search;data structures;dp;implementation;math;two pointers |
| - | -0.0205 | 2061B Kevin and Geometry | 1100 | binary search;geometry |
| - | -0.0201 | 1895C Torn Lucky Ticket | 1400 | brute force;dp;hashing;implementation;math |

_Plain-language reading:_ TODO

## Axis 2  (sigma = 92.15)

- enriched at `+` end: implementation (z=+2.4), combinatorics (z=+2.1), data structures (z=+2.0), dfs and similar (z=+1.6), shortest paths (z=+1.5)
- enriched at `-` end: constructive algorithms (z=-3.1), greedy (z=-2.3), math (z=-2.2), number theory (z=-1.8), brute force (z=-1.4)
- corr(loading, problem rating) = +0.01; mean rating of `+` end 800, of `-` end 913
- user scores: std 0.482

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.0833 | 1644A Doors and Keys | 800 | implementation |
| + | +0.0831 | 1692A Marathon | 800 | implementation |
| + | +0.0820 | 1703A YES or YES? | 800 | brute force;implementation;strings |
| + | +0.0818 | 1651A Playoff | 800 | implementation |
| + | +0.0808 | 1703B ICPC Balloons | 800 | data structures;implementation |
| + | +0.0801 | 1631A Min Max Swap | 800 | greedy |
| + | +0.0794 | 1676B Equal Candies | 800 | greedy;math;sortings |
| + | +0.0793 | 1676A Lucky? | 800 | implementation |
| + | +0.0785 | 1669A Division? | 800 | implementation |
| + | +0.0768 | 1722B Colourblindness | 800 | implementation |
| + | +0.0739 | 1697A Parkway Walk | 800 | greedy;implementation |
| + | +0.0728 | 1701A Grass Field | 800 | implementation |
| + | +0.0726 | 1632A ABC | 800 | implementation |
| + | +0.0725 | 1703C Cypher | 800 | brute force;implementation;strings |
| + | +0.0711 | 1660A Vasya and Coins | 800 | greedy;math |
| - | -0.0748 | 1999D Slavic's Exam | 1100 | greedy;implementation;strings |
| - | -0.0693 | 1985A Creating Words | 800 | implementation;strings |
| - | -0.0684 | 1985D Manhattan Circle | 900 | implementation;math |
| - | -0.0675 | 1985B Maximum Multiple Sum | 800 | brute force;math;number theory |
| - | -0.0642 | 1986C Update Queries | 1100 | data structures;greedy;sortings |
| - | -0.0622 | 1918A Brick Wall | 800 | constructive algorithms;greedy;implementation;math |
| - | -0.0605 | 1986A X Axis | 800 | brute force;geometry;math;sortings |
| - | -0.0589 | 1999A A+B Again? | 800 | implementation;math |
| - | -0.0588 | 1986B Matrix Stabilization | 1000 | brute force;data structures;greedy;sortings |
| - | -0.0583 | 1985C Good Prefixes | 1000 | greedy |
| - | -0.0568 | 1976A Verify Password | 800 | implementation;sortings;strings |
| - | -0.0564 | 2126C I Will Definitely Make It | 1100 | greedy;sortings |
| - | -0.0557 | 1950A Stair, Peak, or Neither? | 800 | implementation |
| - | -0.0557 | 1980A Problem Generator | 800 | math |
| - | -0.0548 | 2060D Subtract Min Sort | 1100 | greedy |

_Plain-language reading:_ TODO

## Axis 3  (sigma = 75.95)

- enriched at `+` end: dp (z=+6.7), combinatorics (z=+5.4), trees (z=+5.3), graphs (z=+4.9), data structures (z=+4.9)
- enriched at `-` end: math (z=-0.7), games (z=-0.1), strings (z=-0.1)
- corr(loading, problem rating) = +0.14; mean rating of `+` end 1040, of `-` end 833
- user scores: std 0.393

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.0835 | 1927D Find the Different Ones! | 1300 | binary search;brute force;data structures;dp;dsu;greedy;two pointers |
| + | +0.0816 | 1980C Sofia and the Lost Operations | 1300 | constructive algorithms;greedy |
| + | +0.0693 | 1927C Choose the Different Ones! | 1000 | brute force;greedy;math |
| + | +0.0682 | 1955C Inhabitant of the Deep Sea | 1300 | greedy;implementation;math |
| + | +0.0677 | 1931C Make Equal Again | 1000 | brute force;greedy;math |
| + | +0.0638 | 1996C Sort | 1200 | dp;greedy;sortings;strings |
| + | +0.0614 | 1872C Non-coprime Split | 1100 | math;number theory |
| + | +0.0587 | 1850A To My Critics | 800 | implementation;sortings |
| + | +0.0583 | 1850B Ten Words of Wisdom | 800 | implementation;sortings |
| + | +0.0581 | 1850C Word on the Paper | 800 | implementation;strings |
| + | +0.0570 | 1850D Balanced Round | 900 | brute force;greedy;implementation;sortings |
| + | +0.0569 | 1872B The Corridor or There and Back Again | 900 | greedy;implementation |
| + | +0.0568 | 1837A Grasshopper on a Line | 800 | constructive algorithms;math |
| + | +0.0566 | 2000D Right Left Wrong | 1200 | greedy;implementation;two pointers |
| + | +0.0553 | 1954B Make It Ugly | 1200 | implementation;math |
| - | -0.0715 | 1567A Domino Disaster | 800 | implementation;strings |
| - | -0.0699 | 1579A Casimir's String Solitaire | 800 | math;strings |
| - | -0.0665 | 2126C I Will Definitely Make It | 1100 | greedy;sortings |
| - | -0.0650 | 1560A Dislike of Threes | 800 | implementation |
| - | -0.0643 | 2055A Two Frogs | 800 | constructive algorithms;games;greedy;math |
| - | -0.0642 | 1535A Fair Playoff | 800 | brute force;implementation |
| - | -0.0641 | 2148D Destruction of the Dandelion Fields | 1000 | constructive algorithms;greedy;sortings |
| - | -0.0637 | 1569A Balanced Substring | 800 | implementation |
| - | -0.0634 | 1551A Polycarp and Coins | 800 | greedy;math |
| - | -0.0625 | 1624A Plus One on the Subset | 800 | math |
| - | -0.0622 | 1631A Min Max Swap | 800 | greedy |
| - | -0.0618 | 1607A Linear Keyboard | 800 | implementation;strings |
| - | -0.0610 | 1632A ABC | 800 | implementation |
| - | -0.0609 | 1611A Make Even | 800 | constructive algorithms;math |
| - | -0.0606 | 1644A Doors and Keys | 800 | implementation |

_Plain-language reading:_ TODO

## Axis 4  (sigma = 71.75)

- enriched at `+` end: greedy (z=+9.0), constructive algorithms (z=+3.4), binary search (z=+2.8), sortings (z=+2.4), two pointers (z=+1.9)
- enriched at `-` end: meet-in-the-middle (z=-8.9), string suffix structures (z=-8.8), trees (z=-7.0), fft (z=-6.7), divide and conquer (z=-6.5)
- corr(loading, problem rating) = -0.17; mean rating of `+` end 1327, of `-` end 840
- user scores: std 0.356

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.0871 | 1927D Find the Different Ones! | 1300 | binary search;brute force;data structures;dp;dsu;greedy;two pointers |
| + | +0.0740 | 1872D Plus Minus Permutation | 1200 | math |
| + | +0.0726 | 2091E Interesting Ratio | 1300 | brute force;math;number theory;two pointers |
| + | +0.0720 | 2086C Disappearing Permutation | 1300 | dfs and similar;dp;dsu;graphs;greedy;implementation |
| + | +0.0715 | 2072D For Wizards, the Exam Is Easy, but I Couldn't Handle It | 1300 | brute force;greedy;implementation |
| + | +0.0694 | 1931E Anna and the Valentine's Day Gift | 1400 | games;greedy;math;sortings |
| + | +0.0683 | 2000D Right Left Wrong | 1200 | greedy;implementation;two pointers |
| + | +0.0682 | 2025C New Game | 1300 | binary search;brute force;greedy;implementation;sortings;two pointers |
| + | +0.0681 | 2072E Do You Love Your Hero and His Two-Hit Multi-Target Attacks? | 1500 | binary search;brute force;constructive algorithms;dp;geometry;greedy;math |
| + | +0.0680 | 2049B pspspsps | 1300 | brute force;constructive algorithms;graph matchings;implementation |
| + | +0.0667 | 1862D Ice Cream Balls | 1300 | binary search;combinatorics;constructive algorithms;math |
| + | +0.0663 | 1923C Find B | 1400 | constructive algorithms;greedy |
| + | +0.0660 | 1980C Sofia and the Lost Operations | 1300 | constructive algorithms;greedy |
| + | +0.0653 | 1955D Inaccurate Subsequence Search | 1400 | data structures;two pointers |
| + | +0.0647 | 1974D Ingenuity-2 | 1400 | constructive algorithms;greedy;implementation |
| - | -0.0785 | 1791A Codeforces Checking | 800 | implementation;strings |
| - | -0.0764 | 1850A To My Critics | 800 | implementation;sortings |
| - | -0.0736 | 1807A Plus or Minus | 800 | implementation |
| - | -0.0726 | 1850C Word on the Paper | 800 | implementation;strings |
| - | -0.0712 | 1791B Following Directions | 800 | geometry;implementation |
| - | -0.0704 | 1850B Ten Words of Wisdom | 800 | implementation;sortings |
| - | -0.0694 | 1829A Love Story | 800 | implementation;strings |
| - | -0.0689 | 1883F You Are So Beautiful | 1400 | data structures |
| - | -0.0679 | 1807B Grab the Candies | 800 | greedy |
| - | -0.0674 | 1873A Short Sort | 800 | brute force;implementation |
| - | -0.0663 | 1742A Sum | 800 | implementation |
| - | -0.0657 | 1829B Blank Space | 800 | implementation |
| - | -0.0654 | 1760A Medium Number | 800 | implementation;sortings |
| - | -0.0652 | 1873B Good Kid | 800 | brute force;greedy;math |
| - | -0.0651 | 1791C Prepend and Append | 800 | implementation;two pointers |

_Plain-language reading:_ TODO

## Axis 5  (sigma = 65.33)

- enriched at `+` end: meet-in-the-middle (z=+5.7), probabilities (z=+5.5), graphs (z=+4.1), dfs and similar (z=+3.8), divide and conquer (z=+3.7)
- enriched at `-` end: greedy (z=-3.4), games (z=-2.1), math (z=-1.8), constructive algorithms (z=-1.5), number theory (z=-1.4)
- corr(loading, problem rating) = +0.09; mean rating of `+` end 913, of `-` end 1160
- user scores: std 0.341

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.0814 | 1986C Update Queries | 1100 | data structures;greedy;sortings |
| + | +0.0775 | 1999D Slavic's Exam | 1100 | greedy;implementation;strings |
| + | +0.0735 | 1567A Domino Disaster | 800 | implementation;strings |
| + | +0.0730 | 1535A Fair Playoff | 800 | brute force;implementation |
| + | +0.0723 | 1985D Manhattan Circle | 900 | implementation;math |
| + | +0.0708 | 1986B Matrix Stabilization | 1000 | brute force;data structures;greedy;sortings |
| + | +0.0707 | 1985C Good Prefixes | 1000 | greedy |
| + | +0.0701 | 1579A Casimir's String Solitaire | 800 | math;strings |
| + | +0.0694 | 1551A Polycarp and Coins | 800 | greedy;math |
| + | +0.0681 | 1560A Dislike of Threes | 800 | implementation |
| + | +0.0671 | 1542A Odd Set | 800 | math |
| + | +0.0671 | 1569A Balanced Substring | 800 | implementation |
| + | +0.0667 | 1883F You Are So Beautiful | 1400 | data structures |
| + | +0.0656 | 1537A Arithmetic Array | 800 | greedy;math |
| + | +0.0655 | 1541A Pretty Permutations | 800 | constructive algorithms;greedy;implementation |
| - | -0.0788 | 2126C I Will Definitely Make It | 1100 | greedy;sortings |
| - | -0.0782 | 1872D Plus Minus Permutation | 1200 | math |
| - | -0.0686 | 1927D Find the Different Ones! | 1300 | binary search;brute force;data structures;dp;dsu;greedy;two pointers |
| - | -0.0681 | 2179C Blackslex and Number Theory | 1100 | implementation;math;number theory;sortings |
| - | -0.0659 | 1857C Assembly via Minimums | 1200 | greedy;sortings |
| - | -0.0654 | 1872C Non-coprime Split | 1100 | math;number theory |
| - | -0.0650 | 1931E Anna and the Valentine's Day Gift | 1400 | games;greedy;math;sortings |
| - | -0.0633 | 2137D Replace with Occurrences | 1200 | constructive algorithms |
| - | -0.0620 | 2137C Maximum Even Sum | 1100 | brute force;greedy;implementation;math |
| - | -0.0618 | 2148D Destruction of the Dandelion Fields | 1000 | constructive algorithms;greedy;sortings |
| - | -0.0611 | 2162C Beautiful XOR | 1100 | bitmasks;constructive algorithms;greedy |
| - | -0.0610 | 2162B Beautiful String | 1000 | brute force;constructive algorithms |
| - | -0.0600 | 1955D Inaccurate Subsequence Search | 1400 | data structures;two pointers |
| - | -0.0568 | 1931D Divisible Pairs | 1300 | combinatorics;math;number theory |
| - | -0.0556 | 2137B Fun Permutation | 900 | constructive algorithms;math;number theory |

_Plain-language reading:_ TODO

## Axis 6  (sigma = 60.75)

- enriched at `+` end: strings (z=+2.5), implementation (z=+1.6), sortings (z=+1.5), two pointers (z=+1.0), hashing (z=+0.9)
- enriched at `-` end: meet-in-the-middle (z=-4.7), probabilities (z=-4.1), combinatorics (z=-3.8), constructive algorithms (z=-3.1), trees (z=-3.0)
- corr(loading, problem rating) = -0.10; mean rating of `+` end 1007, of `-` end 1127
- user scores: std 0.312

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.0808 | 1650C Weight of the System of Nested Segments | 1200 | greedy;hashing;implementation;sortings |
| + | +0.0787 | 1850A To My Critics | 800 | implementation;sortings |
| + | +0.0771 | 1741D Masha and a Beautiful Tree | 1300 | dfs and similar;divide and conquer;graphs;sortings;trees |
| + | +0.0764 | 1850C Word on the Paper | 800 | implementation;strings |
| + | +0.0752 | 1850B Ten Words of Wisdom | 800 | implementation;sortings |
| + | +0.0703 | 1873A Short Sort | 800 | brute force;implementation |
| + | +0.0689 | 1873B Good Kid | 800 | brute force;greedy;math |
| + | +0.0641 | 1872A Two Vessels | 800 | brute force;greedy;math |
| + | +0.0635 | 1857A Array Coloring | 800 | greedy;math |
| + | +0.0635 | 1618C Paint the Array | 1100 | math |
| + | +0.0634 | 1927D Find the Different Ones! | 1300 | binary search;brute force;data structures;dp;dsu;greedy;two pointers |
| + | +0.0620 | 1849A Morning Sandwich | 800 | implementation;math |
| + | +0.0618 | 1579B Shifting Sort | 1100 | implementation;sortings |
| + | +0.0609 | 1706C Qpwoeirut And The City | 1400 | dp;flows;greedy;implementation |
| + | +0.0592 | 1692F 3SUM | 1300 | brute force;math |
| - | -0.0734 | 2091E Interesting Ratio | 1300 | brute force;math;number theory;two pointers |
| - | -0.0655 | 2091D Place of the Olympiad | 1200 | binary search;greedy;math |
| - | -0.0643 | 1703A YES or YES? | 800 | brute force;implementation;strings |
| - | -0.0642 | 1703B ICPC Balloons | 800 | data structures;implementation |
| - | -0.0638 | 1999D Slavic's Exam | 1100 | greedy;implementation;strings |
| - | -0.0620 | 1883F You Are So Beautiful | 1400 | data structures |
| - | -0.0620 | 1692A Marathon | 800 | implementation |
| - | -0.0606 | 2059B Cost of the Array | 1300 | brute force;constructive algorithms;greedy;math |
| - | -0.0601 | 1703C Cypher | 800 | brute force;implementation;strings |
| - | -0.0593 | 1997C Even Positions | 1100 | constructive algorithms;data structures;greedy |
| - | -0.0558 | 2072D For Wizards, the Exam Is Easy, but I Couldn't Handle It | 1300 | brute force;greedy;implementation |
| - | -0.0552 | 2118C Make It Beautiful | 1300 | bitmasks;data structures;greedy;math |
| - | -0.0550 | 2049B pspspsps | 1300 | brute force;constructive algorithms;graph matchings;implementation |
| - | -0.0546 | 2086C Disappearing Permutation | 1300 | dfs and similar;dp;dsu;graphs;greedy;implementation |
| - | -0.0541 | 1997B Make Three Regions | 1100 | constructive algorithms;two pointers |

_Plain-language reading:_ TODO

## Axis 7  (sigma = 55.34)

- enriched at `+` end: meet-in-the-middle (z=+2.4), graph matchings (z=+2.0), bitmasks (z=+1.9), constructive algorithms (z=+1.8), flows (z=+1.7)
- enriched at `-` end: data structures (z=-2.5), strings (z=-2.4), hashing (z=-2.2), ternary search (z=-2.1), implementation (z=-2.0)
- corr(loading, problem rating) = +0.02; mean rating of `+` end 1120, of `-` end 1067
- user scores: std 0.289

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.0946 | 2131E Adjacent XOR | 1400 | brute force;greedy |
| + | +0.0838 | 2179D Blackslex and Penguin Civilization | 1300 | bitmasks;constructive algorithms;greedy;math |
| + | +0.0838 | 2160C Reverse XOR | 1300 | bitmasks |
| + | +0.0831 | 2162D Beautiful Permutation | 1400 | binary search;interactive |
| + | +0.0797 | 2127B Hamiiid, Haaamid... Hamid? | 1300 | games;greedy |
| + | +0.0708 | 1535A Fair Playoff | 800 | brute force;implementation |
| + | +0.0706 | 1551A Polycarp and Coins | 800 | greedy;math |
| + | +0.0677 | 1542A Odd Set | 800 | math |
| + | +0.0675 | 2137D Replace with Occurrences | 1200 | constructive algorithms |
| + | +0.0663 | 1567A Domino Disaster | 800 | implementation;strings |
| + | +0.0660 | 2146C Wrong Binary Search | 1300 | binary search;constructive algorithms |
| + | +0.0655 | 1560A Dislike of Threes | 800 | implementation |
| + | +0.0648 | 1541A Pretty Permutations | 800 | constructive algorithms;greedy;implementation |
| + | +0.0644 | 2153C Symmetrical Polygons | 1500 | constructive algorithms;geometry;greedy;implementation;sortings |
| + | +0.0627 | 2075B Array Recoloring | 1300 | constructive algorithms;greedy |
| - | -0.1047 | 1857D Strong Vertices | 1300 | math;sortings;trees |
| - | -0.0871 | 1985A Creating Words | 800 | implementation;strings |
| - | -0.0831 | 1985B Maximum Multiple Sum | 800 | brute force;math;number theory |
| - | -0.0831 | 1862D Ice Cream Balls | 1300 | binary search;combinatorics;constructive algorithms;math |
| - | -0.0746 | 1985D Manhattan Circle | 900 | implementation;math |
| - | -0.0743 | 1986A X Axis | 800 | brute force;geometry;math;sortings |
| - | -0.0738 | 1800D Remove Two Letters | 1200 | data structures;greedy;hashing;strings |
| - | -0.0720 | 1857E Power of Points | 1500 | math;sortings |
| - | -0.0719 | 1843D Apple Tree | 1200 | combinatorics;dfs and similar;dp;math;trees |
| - | -0.0704 | 1857C Assembly via Minimums | 1200 | greedy;sortings |
| - | -0.0685 | 1800C2 Powering the Hero (hard version) | 1100 | data structures;greedy |
| - | -0.0680 | 1971A My First Sorting Problem | 800 | implementation;sortings |
| - | -0.0659 | 1872E Data Structures Fan | 1500 | binary search;bitmasks;data structures;dp |
| - | -0.0650 | 1950A Stair, Peak, or Neither? | 800 | implementation |
| - | -0.0645 | 1980A Problem Generator | 800 | math |

_Plain-language reading:_ TODO

## Axis 8  (sigma = 54.10)

- enriched at `+` end: math (z=+7.6), constructive algorithms (z=+4.6), geometry (z=+2.5), number theory (z=+1.9), combinatorics (z=+1.4)
- enriched at `-` end: data structures (z=-8.4), trees (z=-6.1), binary search (z=-6.1), dfs and similar (z=-5.7), two pointers (z=-5.7)
- corr(loading, problem rating) = -0.11; mean rating of `+` end 1220, of `-` end 1240
- user scores: std 0.281

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.1069 | 1979C Earning on Bets | 1200 | binary search;combinatorics;constructive algorithms;number theory |
| + | +0.1010 | 1811C Restore the Array | 1100 | constructive algorithms;greedy |
| + | +0.0969 | 1761B Elimination of a Ring | 1000 | constructive algorithms;greedy;implementation |
| + | +0.0958 | 1844C Particles | 1300 | dp;greedy;implementation;math |
| + | +0.0944 | 1783B Matrix of Differences | 1100 | constructive algorithms;math |
| + | +0.0913 | 1684C Column Swapping | 1400 | brute force;constructive algorithms;greedy;implementation;sortings |
| + | +0.0889 | 1987C Basil's Garden | 1200 | dp;greedy |
| + | +0.0875 | 1929C Sasha and the Casino | 1400 | binary search;brute force;constructive algorithms;games;greedy;math |
| + | +0.0838 | 1738B Prefix Sum Addicts | 1200 | constructive algorithms;greedy;math;sortings |
| + | +0.0825 | 1838B Minimize Permutation Subarrays | 1100 | constructive algorithms;math |
| + | +0.0770 | 1809B Points on Plane | 1000 | binary search;greedy;math |
| + | +0.0750 | 1909B Make Almost Equal With Mod | 1200 | bitmasks;constructive algorithms;math;number theory |
| + | +0.0734 | 1909I Short Permutation Problem | 1900 | combinatorics;dp;fft;math |
| + | +0.0726 | 1811B Conveyor Belts | 1000 | implementation;math |
| + | +0.0720 | 1983B Corner Twist | 1200 | constructive algorithms;greedy;implementation;math |
| - | -0.0683 | 1795C Tea Tasting | 1500 | binary search;data structures;implementation |
| - | -0.0611 | 1778C Flexible String | 1600 | bitmasks;brute force;strings |
| - | -0.0609 | 1706C Qpwoeirut And The City | 1400 | dp;flows;greedy;implementation |
| - | -0.0595 | 2131E Adjacent XOR | 1400 | brute force;greedy |
| - | -0.0594 | 1669G Fall Down | 1200 | dfs and similar;implementation |
| - | -0.0585 | 1742A Sum | 800 | implementation |
| - | -0.0577 | 1760B Atilla's Favorite Problem | 800 | greedy;implementation;strings |
| - | -0.0570 | 1760A Medium Number | 800 | implementation;sortings |
| - | -0.0568 | 1742B Increasing | 800 | greedy;implementation;sortings |
| - | -0.0552 | 1935C Messenger in MAC | 1800 | binary search;brute force;constructive algorithms;data structures;dp;greedy;sortings |
| - | -0.0552 | 1741D Masha and a Beautiful Tree | 1300 | dfs and similar;divide and conquer;graphs;sortings;trees |
| - | -0.0543 | 2072C Creating Keys for StORages Has Become My Main Skill | 1200 | bitmasks;constructive algorithms;greedy |
| - | -0.0541 | 1669H Maximal AND | 1300 | bitmasks;greedy;math |
| - | -0.0539 | 2133C The Nether | 1400 | graphs;interactive |
| - | -0.0536 | 1555C Coin Rows | 1300 | brute force;constructive algorithms;dp;implementation |

_Plain-language reading:_ TODO

## Axis 9  (sigma = 53.09)

- enriched at `+` end: meet-in-the-middle (z=+8.6), trees (z=+8.4), divide and conquer (z=+8.3), dfs and similar (z=+7.6), fft (z=+7.3)
- enriched at `-` end: constructive algorithms (z=-3.8), math (z=-3.3), greedy (z=-3.3), games (z=-1.8), number theory (z=-1.8)
- corr(loading, problem rating) = +0.16; mean rating of `+` end 1160, of `-` end 1127
- user scores: std 0.277

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.0966 | 1980C Sofia and the Lost Operations | 1300 | constructive algorithms;greedy |
| + | +0.0951 | 1927D Find the Different Ones! | 1300 | binary search;brute force;data structures;dp;dsu;greedy;two pointers |
| + | +0.0906 | 1955C Inhabitant of the Deep Sea | 1300 | greedy;implementation;math |
| + | +0.0753 | 1927C Choose the Different Ones! | 1000 | brute force;greedy;math |
| + | +0.0740 | 1955D Inaccurate Subsequence Search | 1400 | data structures;two pointers |
| + | +0.0705 | 1974D Ingenuity-2 | 1400 | constructive algorithms;greedy;implementation |
| + | +0.0666 | 1986D Mathematical Problem | 1400 | brute force;dp;greedy;implementation;math;two pointers |
| + | +0.0628 | 1846B Rudolph and Tic-Tac-Toe | 800 | brute force;implementation;strings |
| + | +0.0609 | 1927B Following the String | 900 | constructive algorithms;greedy;strings |
| + | +0.0606 | 1931C Make Equal Again | 1000 | brute force;greedy;math |
| + | +0.0598 | 2025C New Game | 1300 | binary search;brute force;greedy;implementation;sortings;two pointers |
| + | +0.0575 | 1968D Permutation Game | 1300 | brute force;dfs and similar;games;graphs;greedy;math |
| + | +0.0564 | 1932D Card Game | 1400 | greedy;implementation |
| + | +0.0523 | 1644A Doors and Keys | 800 | implementation |
| + | +0.0514 | 1669C Odd/Even Increments | 800 | greedy;implementation;math |
| - | -0.1182 | 1844C Particles | 1300 | dp;greedy;implementation;math |
| - | -0.0945 | 1811C Restore the Array | 1100 | constructive algorithms;greedy |
| - | -0.0867 | 1840B Binary Cafe | 1100 | bitmasks;combinatorics;math |
| - | -0.0762 | 1807G2 Subsequence Addition (Hard Version) | 1100 | bitmasks;dp;greedy;implementation;sortings |
| - | -0.0754 | 1807G1 Subsequence Addition (Easy Version) | 1100 | brute force;data structures;dp;greedy;implementation;sortings |
| - | -0.0703 | 2119B Line Segments | 1200 | geometry;greedy;math |
| - | -0.0700 | 1844B Permutations & Primes | 1000 | constructive algorithms;math |
| - | -0.0686 | 1844D Row Major | 1400 | constructive algorithms;greedy;math;number theory;strings |
| - | -0.0654 | 1914E2 Game with Marbles (Hard Version) | 1400 | games;greedy;sortings |
| - | -0.0642 | 1650C Weight of the System of Nested Segments | 1200 | greedy;hashing;implementation;sortings |
| - | -0.0640 | 1811B Conveyor Belts | 1000 | implementation;math |
| - | -0.0628 | 1768A Greatest Convex | 800 | greedy;math;number theory |
| - | -0.0620 | 1791A Codeforces Checking | 800 | implementation;strings |
| - | -0.0614 | 1929C Sasha and the Casino | 1400 | binary search;brute force;constructive algorithms;games;greedy;math |
| - | -0.0612 | 1837C Best Binary String | 1000 | constructive algorithms;greedy |

_Plain-language reading:_ TODO

## Axis 10  (sigma = 50.46)

- enriched at `+` end: games (z=+3.4), math (z=+3.0), binary search (z=+2.4), brute force (z=+2.4), constructive algorithms (z=+2.2)
- enriched at `-` end: meet-in-the-middle (z=-6.8), matrices (z=-3.9), sortings (z=-3.7), probabilities (z=-3.7), flows (z=-3.3)
- corr(loading, problem rating) = -0.08; mean rating of `+` end 1427, of `-` end 1193
- user scores: std 0.261

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.0925 | 2007C Dora and C++ | 1500 | math;number theory |
| + | +0.0849 | 1929C Sasha and the Casino | 1400 | binary search;brute force;constructive algorithms;games;greedy;math |
| + | +0.0703 | 2049C MEX Cycle | 1500 | brute force;constructive algorithms;greedy;implementation |
| + | +0.0702 | 1984C2 Magnitude (Hard Version) | 1700 | combinatorics;dp;greedy;math |
| + | +0.0697 | 1994C Hungry Games | 1600 | binary search;dp;two pointers |
| + | +0.0666 | 1883F You Are So Beautiful | 1400 | data structures |
| + | +0.0639 | 1792C Min Max Sort | 1500 | binary search;brute force;greedy;math;two pointers |
| + | +0.0635 | 1957C How Does the Rook Move? | 1600 | combinatorics;dp;math |
| + | +0.0628 | 1762C Binary Strings are Fun | 1400 | combinatorics;math |
| + | +0.0615 | 1736C1 Good Subarrays (Easy Version) | 1300 | binary search;data structures;schedules;two pointers |
| + | +0.0598 | 1989C Two Movies | 1400 | greedy;math |
| + | +0.0593 | 1983D Swap Dilemma | 1700 | constructive algorithms;data structures;divide and conquer;greedy;math;sortings |
| + | +0.0589 | 1644A Doors and Keys | 800 | implementation |
| + | +0.0589 | 1826A Trust Nobody | 1200 | brute force;greedy;implementation;sortings |
| + | +0.0589 | 1883G1 Dances (Easy version) | 1400 | binary search;greedy;two pointers |
| - | -0.1008 | 1800C2 Powering the Hero (hard version) | 1100 | data structures;greedy |
| - | -0.0947 | 1791G1 Teleporters (Easy Version) | 1100 | greedy;sortings |
| - | -0.0930 | 1684C Column Swapping | 1400 | brute force;constructive algorithms;greedy;implementation;sortings |
| - | -0.0929 | 1872D Plus Minus Permutation | 1200 | math |
| - | -0.0925 | 2061B Kevin and Geometry | 1100 | binary search;geometry |
| - | -0.0883 | 1791E Negatives and Positives | 1100 | dp;greedy;sortings |
| - | -0.0872 | 1999D Slavic's Exam | 1100 | greedy;implementation;strings |
| - | -0.0856 | 1791D Distinct Split | 1000 | brute force;greedy;strings |
| - | -0.0852 | 1857C Assembly via Minimums | 1200 | greedy;sortings |
| - | -0.0845 | 1800C1 Powering the Hero (easy version) | 1000 | data structures;greedy |
| - | -0.0814 | 1800B Count the Number of Pairs | 1000 | greedy;strings |
| - | -0.0717 | 1909I Short Permutation Problem | 1900 | combinatorics;dp;fft;math |
| - | -0.0704 | 1829F Forever Winter | 1300 | dfs and similar;graphs;math |
| - | -0.0679 | 1857D Strong Vertices | 1300 | math;sortings;trees |
| - | -0.0660 | 1807G1 Subsequence Addition (Easy Version) | 1100 | brute force;data structures;dp;greedy;implementation;sortings |

_Plain-language reading:_ TODO

## Axis 11  (sigma = 48.35)

- enriched at `+` end: dp (z=+4.2), data structures (z=+3.9), binary search (z=+3.5), brute force (z=+3.1), dfs and similar (z=+2.8)
- enriched at `-` end: constructive algorithms (z=-5.1), games (z=-4.0), greedy (z=-1.6), graph matchings (z=-1.2), flows (z=-1.0)
- corr(loading, problem rating) = +0.00; mean rating of `+` end 1313, of `-` end 1033
- user scores: std 0.252

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.1412 | 1996D Fun | 1500 | binary search;brute force;combinatorics;math;number theory |
| + | +0.1327 | 1996C Sort | 1200 | dp;greedy;sortings;strings |
| + | +0.0978 | 2008F Sakurako's Box | 1400 | combinatorics;math;number theory |
| + | +0.0825 | 2000D Right Left Wrong | 1200 | greedy;implementation;two pointers |
| + | +0.0789 | 2033E Sakurako, Kosuke, and the Permutation | 1400 | brute force;data structures;dfs and similar;dsu;graphs;greedy;math |
| + | +0.0748 | 1985E Secret Box | 1200 | brute force;combinatorics;math |
| + | +0.0739 | 1991C Absolute Zero | 1300 | constructive algorithms;greedy;math |
| + | +0.0682 | 2070C Limited Repainting | 1500 | binary search;greedy |
| + | +0.0668 | 1807G2 Subsequence Addition (Hard Version) | 1100 | bitmasks;dp;greedy;implementation;sortings |
| + | +0.0652 | 2008D Sakurako's Hobby | 1100 | dp;dsu;graphs;math |
| + | +0.0633 | 1807G1 Subsequence Addition (Easy Version) | 1100 | brute force;data structures;dp;greedy;implementation;sortings |
| + | +0.0625 | 2069C Beautiful Sequence | 1500 | combinatorics;dp;greedy;two pointers |
| + | +0.0585 | 1980D GCD-sequence | 1400 | greedy;implementation;math;number theory |
| + | +0.0583 | 1980C Sofia and the Lost Operations | 1300 | constructive algorithms;greedy |
| + | +0.0571 | 2060E Graph Composition | 1500 | dfs and similar;dsu;graphs;greedy |
| - | -0.0771 | 1788C Matching Numbers | 1300 | constructive algorithms;greedy;math |
| - | -0.0723 | 2127B Hamiiid, Haaamid... Hamid? | 1300 | games;greedy |
| - | -0.0722 | 1708B Difference of GCDs | 1100 | constructive algorithms;math |
| - | -0.0720 | 1873A Short Sort | 800 | brute force;implementation |
| - | -0.0708 | 1873B Good Kid | 800 | brute force;greedy;math |
| - | -0.0699 | 1694B Paranoid String | 1200 | constructive algorithms;greedy |
| - | -0.0696 | 2075B Array Recoloring | 1300 | constructive algorithms;greedy |
| - | -0.0682 | 1850A To My Critics | 800 | implementation;sortings |
| - | -0.0676 | 1684C Column Swapping | 1400 | brute force;constructive algorithms;greedy;implementation;sortings |
| - | -0.0662 | 1767D Playoff | 1500 | combinatorics;constructive algorithms;dp;greedy;math |
| - | -0.0660 | 1872A Two Vessels | 800 | brute force;greedy;math |
| - | -0.0654 | 1850C Word on the Paper | 800 | implementation;strings |
| - | -0.0646 | 1849A Morning Sandwich | 800 | implementation;math |
| - | -0.0639 | 1857A Array Coloring | 800 | greedy;math |
| - | -0.0632 | 1850B Ten Words of Wisdom | 800 | implementation;sortings |

_Plain-language reading:_ TODO

## Axis 12  (sigma = 48.13)

- enriched at `+` end: constructive algorithms (z=+4.9), greedy (z=+3.9), flows (z=+1.5), sortings (z=+1.2), implementation (z=+0.9)
- enriched at `-` end: combinatorics (z=-4.9), binary search (z=-4.7), math (z=-4.5), number theory (z=-3.6), dp (z=-3.4)
- corr(loading, problem rating) = -0.05; mean rating of `+` end 1167, of `-` end 1187
- user scores: std 0.252

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.0990 | 1986C Update Queries | 1100 | data structures;greedy;sortings |
| + | +0.0867 | 1997B Make Three Regions | 1100 | constructive algorithms;two pointers |
| + | +0.0781 | 1997C Even Positions | 1100 | constructive algorithms;data structures;greedy |
| + | +0.0779 | 1980C Sofia and the Lost Operations | 1300 | constructive algorithms;greedy |
| + | +0.0777 | 2128B Deque Process | 1100 | constructive algorithms;greedy;sortings;two pointers |
| + | +0.0768 | 2127B Hamiiid, Haaamid... Hamid? | 1300 | games;greedy |
| + | +0.0762 | 1976B Increase/Decrease/Copy | 1100 | greedy;implementation |
| + | +0.0726 | 2005B2 The Strict Teacher (Hard Version) | 1200 | binary search;greedy;math;sortings |
| + | +0.0707 | 2004C Splitting Items | 1100 | games;greedy;sortings |
| + | +0.0636 | 2025C New Game | 1300 | binary search;brute force;greedy;implementation;sortings;two pointers |
| + | +0.0625 | 1986B Matrix Stabilization | 1000 | brute force;data structures;greedy;sortings |
| + | +0.0624 | 2000D Right Left Wrong | 1200 | greedy;implementation;two pointers |
| + | +0.0593 | 1807G2 Subsequence Addition (Hard Version) | 1100 | bitmasks;dp;greedy;implementation;sortings |
| + | +0.0575 | 1993B Parity and Sum | 1100 | constructive algorithms;greedy |
| + | +0.0570 | 2035C Alya and Permutation | 1400 | bitmasks;constructive algorithms;math |
| - | -0.1028 | 2117D Retaliation | 1200 | binary search;math;number theory |
| - | -0.0954 | 2119B Line Segments | 1200 | geometry;greedy;math |
| - | -0.0882 | 2132B The Secret Number | 900 | math |
| - | -0.0820 | 2065C1 Skibidus and Fanum Tax (easy version) | 1100 | binary search;dp;greedy |
| - | -0.0747 | 2070C Limited Repainting | 1500 | binary search;greedy |
| - | -0.0746 | 2044B Normal Problem | 800 | implementation;strings |
| - | -0.0742 | 2044A Easy Problem | 800 | brute force;math |
| - | -0.0738 | 2112C Coloring Game | 1300 | binary search;brute force;greedy;two pointers |
| - | -0.0724 | 2060D Subtract Min Sort | 1100 | greedy |
| - | -0.0700 | 2044C Hard Problem | 800 | greedy;math |
| - | -0.0698 | 2140C Ultimate Value | 1500 | data structures;games;greedy |
| - | -0.0689 | 2110C Racing | 1400 | constructive algorithms;greedy |
| - | -0.0666 | 1996D Fun | 1500 | binary search;brute force;combinatorics;math;number theory |
| - | -0.0665 | 2091E Interesting Ratio | 1300 | brute force;math;number theory;two pointers |
| - | -0.0656 | 1931E Anna and the Valentine's Day Gift | 1400 | games;greedy;math;sortings |

_Plain-language reading:_ TODO

## Axis 13  (sigma = 47.03)

- enriched at `+` end: constructive algorithms (z=+3.4), trees (z=+3.0), implementation (z=+2.6), math (z=+2.1), interactive (z=+1.9)
- enriched at `-` end: dsu (z=-1.6), data structures (z=-1.2), strings (z=-1.1), number theory (z=-1.1), bitmasks (z=-1.0)
- corr(loading, problem rating) = +0.04; mean rating of `+` end 1147, of `-` end 1213
- user scores: std 0.246

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.0760 | 1997B Make Three Regions | 1100 | constructive algorithms;two pointers |
| + | +0.0659 | 2111D Creating a Schedule | 1400 | constructive algorithms;data structures;greedy;implementation;sortings |
| + | +0.0647 | 1551A Polycarp and Coins | 800 | greedy;math |
| + | +0.0644 | 1997D Maximize the Root | 1500 | binary search;dfs and similar;dp;greedy;trees |
| + | +0.0620 | 1927E Klever Permutation | 1400 | constructive algorithms;math;two pointers |
| + | +0.0618 | 1997C Even Positions | 1100 | constructive algorithms;data structures;greedy |
| + | +0.0612 | 2127D Root was Built by Love, Broken by Destiny | 1800 | combinatorics;dfs and similar;graphs;trees |
| + | +0.0599 | 1535A Fair Playoff | 800 | brute force;implementation |
| + | +0.0596 | 1989C Two Movies | 1400 | greedy;math |
| + | +0.0585 | 1560A Dislike of Threes | 800 | implementation |
| + | +0.0583 | 1948C Arrow Path | 1300 | brute force;constructive algorithms;dfs and similar;dp;graphs;shortest paths |
| + | +0.0579 | 1549A Gregor and Cryptography | 800 | math;number theory |
| + | +0.0578 | 1542A Odd Set | 800 | math |
| + | +0.0574 | 1931E Anna and the Valentine's Day Gift | 1400 | games;greedy;math;sortings |
| + | +0.0573 | 1567A Domino Disaster | 800 | implementation;strings |
| - | -0.1199 | 1926C Vlad and a Sum of Sum of Digits | 1200 | dp;implementation |
| - | -0.1176 | 1996D Fun | 1500 | binary search;brute force;combinatorics;math;number theory |
| - | -0.1128 | 1979C Earning on Bets | 1200 | binary search;combinatorics;constructive algorithms;number theory |
| - | -0.1035 | 1800C2 Powering the Hero (hard version) | 1100 | data structures;greedy |
| - | -0.0998 | 2118B Make It Permutation | 1200 | constructive algorithms |
| - | -0.0985 | 2119B Line Segments | 1200 | geometry;greedy;math |
| - | -0.0882 | 1800E2 Unforgivable Curse (hard version) | 1500 | brute force;constructive algorithms;dfs and similar;dsu;graphs;greedy;strings |
| - | -0.0869 | 1800D Remove Two Letters | 1200 | data structures;greedy;hashing;strings |
| - | -0.0848 | 1790E Vlad and a Pair of Numbers | 1400 | bitmasks;constructive algorithms |
| - | -0.0829 | 1742E Scuza | 1200 | binary search;greedy;math |
| - | -0.0821 | 1800E1 Unforgivable Curse (easy version) | 1400 | brute force;constructive algorithms;dsu;graphs;greedy;strings |
| - | -0.0818 | 1987C Basil's Garden | 1200 | dp;greedy |
| - | -0.0787 | 1800C1 Powering the Hero (easy version) | 1000 | data structures;greedy |
| - | -0.0785 | 2132B The Secret Number | 900 | math |
| - | -0.0784 | 1979B XOR Sequences | 1000 | bitmasks;greedy |

_Plain-language reading:_ TODO

## Axis 14  (sigma = 44.88)

- enriched at `+` end: geometry (z=+2.2), math (z=+1.9), constructive algorithms (z=+1.7), graph matchings (z=+1.5), games (z=+1.1)
- enriched at `-` end: dp (z=-4.5), data structures (z=-3.9), trees (z=-3.3), binary search (z=-2.9), divide and conquer (z=-2.8)
- corr(loading, problem rating) = -0.07; mean rating of `+` end 1213, of `-` end 1133
- user scores: std 0.234

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.1178 | 1684C Column Swapping | 1400 | brute force;constructive algorithms;greedy;implementation;sortings |
| + | +0.0876 | 1909I Short Permutation Problem | 1900 | combinatorics;dp;fft;math |
| + | +0.0841 | 2119B Line Segments | 1200 | geometry;greedy;math |
| + | +0.0813 | 1998A Find K Distinct Points with Fixed Center | 800 | constructive algorithms;implementation;math |
| + | +0.0777 | 1983B Corner Twist | 1200 | constructive algorithms;greedy;implementation;math |
| + | +0.0769 | 1774B Coloring | 1500 | constructive algorithms;greedy;math |
| + | +0.0744 | 1778B The Forbidden Permutation | 1300 | greedy;math |
| + | +0.0698 | 1846B Rudolph and Tic-Tac-Toe | 800 | brute force;implementation;strings |
| + | +0.0678 | 1829F Forever Winter | 1300 | dfs and similar;graphs;math |
| + | +0.0662 | 2164B Even Modulo Pair | 1000 | brute force;math;number theory |
| + | +0.0640 | 1738B Prefix Sum Addicts | 1200 | constructive algorithms;greedy;math;sortings |
| + | +0.0639 | 1739B Array Recovery | 1100 | constructive algorithms;greedy;math |
| + | +0.0596 | 1669G Fall Down | 1200 | dfs and similar;implementation |
| + | +0.0595 | 1977B Binary Colouring | 1100 | bitmasks;constructive algorithms;greedy;math |
| + | +0.0586 | 1792B Stand-up Comedian | 1200 | greedy;math |
| - | -0.1891 | 1811C Restore the Array | 1100 | constructive algorithms;greedy |
| - | -0.1606 | 1844C Particles | 1300 | dp;greedy;implementation;math |
| - | -0.1400 | 1807G2 Subsequence Addition (Hard Version) | 1100 | bitmasks;dp;greedy;implementation;sortings |
| - | -0.1361 | 1807G1 Subsequence Addition (Easy Version) | 1100 | brute force;data structures;dp;greedy;implementation;sortings |
| - | -0.1107 | 1840B Binary Cafe | 1100 | bitmasks;combinatorics;math |
| - | -0.1048 | 1811E Living Sequence | 1500 | binary search;dp;math;number theory |
| - | -0.0965 | 1811B Conveyor Belts | 1000 | implementation;math |
| - | -0.0958 | 1844D Row Major | 1400 | constructive algorithms;greedy;math;number theory;strings |
| - | -0.0945 | 1844B Permutations & Primes | 1000 | constructive algorithms;math |
| - | -0.0890 | 1999D Slavic's Exam | 1100 | greedy;implementation;strings |
| - | -0.0882 | 2000D Right Left Wrong | 1200 | greedy;implementation;two pointers |
| - | -0.0786 | 2000C Numeric String Template | 1000 | data structures;strings |
| - | -0.0730 | 1857B Maximum Rounding | 1100 | greedy;implementation;math |
| - | -0.0717 | 1837C Best Binary String | 1000 | constructive algorithms;greedy |
| - | -0.0691 | 1840C Ski Resort | 1000 | combinatorics;math;two pointers |

_Plain-language reading:_ TODO

## Axis 15  (sigma = 44.24)

- enriched at `+` end: dp (z=+4.5), data structures (z=+4.1), dfs and similar (z=+4.1), divide and conquer (z=+3.5), trees (z=+3.3)
- enriched at `-` end: constructive algorithms (z=-3.2), math (z=-3.1), ternary search (z=-1.1), geometry (z=-1.0), games (z=-0.9)
- corr(loading, problem rating) = +0.05; mean rating of `+` end 1160, of `-` end 1193
- user scores: std 0.231

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.1354 | 1684C Column Swapping | 1400 | brute force;constructive algorithms;greedy;implementation;sortings |
| + | +0.1340 | 1807G1 Subsequence Addition (Easy Version) | 1100 | brute force;data structures;dp;greedy;implementation;sortings |
| + | +0.1300 | 1633C Kill the Monster | 1100 | brute force;math |
| + | +0.1292 | 1807G2 Subsequence Addition (Hard Version) | 1100 | bitmasks;dp;greedy;implementation;sortings |
| + | +0.1232 | 1800C2 Powering the Hero (hard version) | 1100 | data structures;greedy |
| + | +0.1008 | 1800C1 Powering the Hero (easy version) | 1000 | data structures;greedy |
| + | +0.0934 | 1800D Remove Two Letters | 1200 | data structures;greedy;hashing;strings |
| + | +0.0787 | 1791E Negatives and Positives | 1100 | dp;greedy;sortings |
| + | +0.0745 | 1878E Iva & Pav | 1400 | binary search;bitmasks;data structures;greedy |
| + | +0.0735 | 1840D Wooden Toy Festival | 1400 | binary search;greedy;sortings |
| + | +0.0725 | 1800B Count the Number of Pairs | 1000 | greedy;strings |
| + | +0.0723 | 1811C Restore the Array | 1100 | constructive algorithms;greedy |
| + | +0.0708 | 1791G1 Teleporters (Easy Version) | 1100 | greedy;sortings |
| + | +0.0670 | 1791A Codeforces Checking | 800 | implementation;strings |
| + | +0.0648 | 1800E2 Unforgivable Curse (hard version) | 1500 | brute force;constructive algorithms;dfs and similar;dsu;graphs;greedy;strings |
| - | -0.1222 | 1927D Find the Different Ones! | 1300 | binary search;brute force;data structures;dp;dsu;greedy;two pointers |
| - | -0.1049 | 1872C Non-coprime Split | 1100 | math;number theory |
| - | -0.0853 | 1872D Plus Minus Permutation | 1200 | math |
| - | -0.0815 | 1933D Turtle Tenacity: Continual Mods | 1200 | constructive algorithms;greedy;math;number theory;sortings |
| - | -0.0786 | 1559C Mocha and Hiking | 1200 | constructive algorithms;graphs |
| - | -0.0734 | 2061B Kevin and Geometry | 1100 | binary search;geometry |
| - | -0.0733 | 1555C Coin Rows | 1300 | brute force;constructive algorithms;dp;implementation |
| - | -0.0714 | 2059B Cost of the Array | 1300 | brute force;constructive algorithms;greedy;math |
| - | -0.0700 | 1872B The Corridor or There and Back Again | 900 | greedy;implementation |
| - | -0.0696 | 2164B Even Modulo Pair | 1000 | brute force;math;number theory |
| - | -0.0683 | 1547D Co-growing Sequence | 1300 | bitmasks;constructive algorithms;greedy |
| - | -0.0650 | 2118B Make It Permutation | 1200 | constructive algorithms |
| - | -0.0614 | 1538C Number of Pairs | 1300 | binary search;data structures;math;two pointers |
| - | -0.0603 | 1955C Inhabitant of the Deep Sea | 1300 | greedy;implementation;math |
| - | -0.0601 | 1935B Informatics in MAC | 1200 | constructive algorithms |

_Plain-language reading:_ TODO

## Axis 16  (sigma = 44.05)

- enriched at `+` end: sortings (z=+3.3), brute force (z=+1.6), two pointers (z=+1.1), geometry (z=+0.7), games (z=+0.5)
- enriched at `-` end: dp (z=-3.3), dsu (z=-1.7), data structures (z=-1.6), number theory (z=-1.5), probabilities (z=-1.3)
- corr(loading, problem rating) = -0.01; mean rating of `+` end 1100, of `-` end 1120
- user scores: std 0.231

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.1235 | 1997B Make Three Regions | 1100 | constructive algorithms;two pointers |
| + | +0.1190 | 1997C Even Positions | 1100 | constructive algorithms;data structures;greedy |
| + | +0.1095 | 2002C Black Circles | 1200 | brute force;geometry;greedy;math |
| + | +0.1092 | 1991C Absolute Zero | 1300 | constructive algorithms;greedy;math |
| + | +0.0838 | 1987C Basil's Garden | 1200 | dp;greedy |
| + | +0.0827 | 1741C Minimize the Thickness | 1100 | brute force;greedy;math;two pointers |
| + | +0.0812 | 2003C Turtle and Good Pairs | 1200 | constructive algorithms;greedy;sortings;strings |
| + | +0.0794 | 1993B Parity and Sum | 1100 | constructive algorithms;greedy |
| + | +0.0756 | 1857C Assembly via Minimums | 1200 | greedy;sortings |
| + | +0.0730 | 1991B AND Reconstruction | 1100 | bitmasks;constructive algorithms;greedy |
| + | +0.0710 | 1741D Masha and a Beautiful Tree | 1300 | dfs and similar;divide and conquer;graphs;sortings;trees |
| + | +0.0692 | 2004C Splitting Items | 1100 | games;greedy;sortings |
| + | +0.0677 | 1829A Love Story | 800 | implementation;strings |
| + | +0.0676 | 1829B Blank Space | 800 | implementation |
| + | +0.0664 | 1850D Balanced Round | 900 | brute force;greedy;implementation;sortings |
| - | -0.1271 | 1811C Restore the Array | 1100 | constructive algorithms;greedy |
| - | -0.1184 | 1807G2 Subsequence Addition (Hard Version) | 1100 | bitmasks;dp;greedy;implementation;sortings |
| - | -0.1149 | 1927D Find the Different Ones! | 1300 | binary search;brute force;data structures;dp;dsu;greedy;two pointers |
| - | -0.1099 | 1927C Choose the Different Ones! | 1000 | brute force;greedy;math |
| - | -0.1055 | 1807G1 Subsequence Addition (Easy Version) | 1100 | brute force;data structures;dp;greedy;implementation;sortings |
| - | -0.0980 | 1955C Inhabitant of the Deep Sea | 1300 | greedy;implementation;math |
| - | -0.0950 | 1955D Inaccurate Subsequence Search | 1400 | data structures;two pointers |
| - | -0.0908 | 1927B Following the String | 900 | constructive algorithms;greedy;strings |
| - | -0.0868 | 1783B Matrix of Differences | 1100 | constructive algorithms;math |
| - | -0.0864 | 1747C Swap Game | 1200 | games |
| - | -0.0830 | 1926C Vlad and a Sum of Sum of Digits | 1200 | dp;implementation |
| - | -0.0774 | 1927A Make it White | 800 | greedy;strings |
| - | -0.0752 | 1811E Living Sequence | 1500 | binary search;dp;math;number theory |
| - | -0.0713 | 1811B Conveyor Belts | 1000 | implementation;math |
| - | -0.0692 | 1915A Odd One Out | 800 | bitmasks;implementation |

_Plain-language reading:_ TODO

## Axis 17  (sigma = 43.06)

- enriched at `+` end: strings (z=+1.8), combinatorics (z=+1.4), matrices (z=+1.2), probabilities (z=+1.1), fft (z=+1.1)
- enriched at `-` end: trees (z=-3.9), data structures (z=-3.5), divide and conquer (z=-3.0), dfs and similar (z=-2.3), shortest paths (z=-2.0)
- corr(loading, problem rating) = -0.05; mean rating of `+` end 1240, of `-` end 1240
- user scores: std 0.225

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.1225 | 1637C Andrew and Stones | 1200 | greedy;implementation |
| + | +0.1056 | 2000D Right Left Wrong | 1200 | greedy;implementation;two pointers |
| + | +0.1055 | 2072E Do You Love Your Hero and His Two-Hit Multi-Target Attacks? | 1500 | binary search;brute force;constructive algorithms;dp;geometry;greedy;math |
| + | +0.1053 | 2072D For Wizards, the Exam Is Easy, but I Couldn't Handle It | 1300 | brute force;greedy;implementation |
| + | +0.1015 | 2000C Numeric String Template | 1000 | data structures;strings |
| + | +0.0966 | 1999E Triple Operations | 1300 | dp;implementation;math |
| + | +0.0964 | 1634B Fortune Telling | 1400 | bitmasks;math |
| + | +0.0933 | 2065C2 Skibidus and Fanum Tax (hard version) | 1300 | binary search;greedy |
| + | +0.0925 | 2065D Skibidus and Sigma | 1200 | greedy;sortings |
| + | +0.0918 | 1694B Paranoid String | 1200 | constructive algorithms;greedy |
| + | +0.0860 | 1925B A Balanced Problemset? | 1200 | brute force;greedy;math;number theory |
| + | +0.0853 | 2091E Interesting Ratio | 1300 | brute force;math;number theory;two pointers |
| + | +0.0830 | 1656B Subtract Operation | 1100 | data structures;greedy;math;two pointers |
| + | +0.0807 | 1659A Red Versus Blue | 1000 | constructive algorithms;greedy;implementation;math |
| + | +0.0796 | 2008F Sakurako's Box | 1400 | combinatorics;math;number theory |
| - | -0.1067 | 1857D Strong Vertices | 1300 | math;sortings;trees |
| - | -0.1058 | 1914E1 Game with Marbles (Easy Version) | 1400 | brute force;games;greedy;sortings |
| - | -0.1006 | 1914E2 Game with Marbles (Hard Version) | 1400 | games;greedy;sortings |
| - | -0.0910 | 2123D Binary String Battle | 1200 | constructive algorithms;games;greedy |
| - | -0.0894 | 1669G Fall Down | 1200 | dfs and similar;implementation |
| - | -0.0883 | 1857C Assembly via Minimums | 1200 | greedy;sortings |
| - | -0.0878 | 1807G1 Subsequence Addition (Easy Version) | 1100 | brute force;data structures;dp;greedy;implementation;sortings |
| - | -0.0853 | 1807G2 Subsequence Addition (Hard Version) | 1100 | bitmasks;dp;greedy;implementation;sortings |
| - | -0.0824 | 1929C Sasha and the Casino | 1400 | binary search;brute force;constructive algorithms;games;greedy;math |
| - | -0.0790 | 1669F Eating Candies | 1100 | binary search;data structures;greedy;two pointers |
| - | -0.0763 | 1844C Particles | 1300 | dp;greedy;implementation;math |
| - | -0.0715 | 1811C Restore the Array | 1100 | constructive algorithms;greedy |
| - | -0.0705 | 1987C Basil's Garden | 1200 | dp;greedy |
| - | -0.0704 | 2127B Hamiiid, Haaamid... Hamid? | 1300 | games;greedy |
| - | -0.0678 | 2059B Cost of the Array | 1300 | brute force;constructive algorithms;greedy;math |

_Plain-language reading:_ TODO

## Axis 18  (sigma = 42.69)

- enriched at `+` end: math (z=+3.7), number theory (z=+3.0), geometry (z=+1.6), ternary search (z=+1.5), flows (z=+1.4)
- enriched at `-` end: greedy (z=-4.8), brute force (z=-2.8), constructive algorithms (z=-2.8), strings (z=-2.6), data structures (z=-1.5)
- corr(loading, problem rating) = +0.01; mean rating of `+` end 1173, of `-` end 1253
- user scores: std 0.223

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.1628 | 1857C Assembly via Minimums | 1200 | greedy;sortings |
| + | +0.1513 | 1857D Strong Vertices | 1300 | math;sortings;trees |
| + | +0.1162 | 1986C Update Queries | 1100 | data structures;greedy;sortings |
| + | +0.1152 | 1846D Rudolph and Christmas Tree | 1200 | constructive algorithms;geometry;math |
| + | +0.1099 | 1862D Ice Cream Balls | 1300 | binary search;combinatorics;constructive algorithms;math |
| + | +0.1083 | 1857B Maximum Rounding | 1100 | greedy;implementation;math |
| + | +0.1047 | 1872D Plus Minus Permutation | 1200 | math |
| + | +0.0992 | 2132B The Secret Number | 900 | math |
| + | +0.0964 | 1986B Matrix Stabilization | 1000 | brute force;data structures;greedy;sortings |
| + | +0.0910 | 1872E Data Structures Fan | 1500 | binary search;bitmasks;data structures;dp |
| + | +0.0876 | 1857E Power of Points | 1500 | math;sortings |
| + | +0.0810 | 2132C1 The Cunning Seller (easy version) | 1000 | greedy;math |
| + | +0.0759 | 2000C Numeric String Template | 1000 | data structures;strings |
| + | +0.0754 | 2137D Replace with Occurrences | 1200 | constructive algorithms |
| + | +0.0753 | 2061B Kevin and Geometry | 1100 | binary search;geometry |
| - | -0.1379 | 1800C2 Powering the Hero (hard version) | 1100 | data structures;greedy |
| - | -0.1216 | 1807G2 Subsequence Addition (Hard Version) | 1100 | bitmasks;dp;greedy;implementation;sortings |
| - | -0.1215 | 1800C1 Powering the Hero (easy version) | 1000 | data structures;greedy |
| - | -0.1181 | 1807G1 Subsequence Addition (Easy Version) | 1100 | brute force;data structures;dp;greedy;implementation;sortings |
| - | -0.1040 | 1800E1 Unforgivable Curse (easy version) | 1400 | brute force;constructive algorithms;dsu;graphs;greedy;strings |
| - | -0.1022 | 1800D Remove Two Letters | 1200 | data structures;greedy;hashing;strings |
| - | -0.1020 | 1800E2 Unforgivable Curse (hard version) | 1500 | brute force;constructive algorithms;dfs and similar;dsu;graphs;greedy;strings |
| - | -0.0859 | 2059B Cost of the Array | 1300 | brute force;constructive algorithms;greedy;math |
| - | -0.0821 | 2049B pspspsps | 1300 | brute force;constructive algorithms;graph matchings;implementation |
| - | -0.0750 | 2072D For Wizards, the Exam Is Easy, but I Couldn't Handle It | 1300 | brute force;greedy;implementation |
| - | -0.0708 | 2048C Kevin and Binary Strings | 1200 | bitmasks;brute force;greedy;implementation;strings |
| - | -0.0667 | 2049C MEX Cycle | 1500 | brute force;constructive algorithms;greedy;implementation |
| - | -0.0650 | 2072C Creating Keys for StORages Has Become My Main Skill | 1200 | bitmasks;constructive algorithms;greedy |
| - | -0.0644 | 1883F You Are So Beautiful | 1400 | data structures |
| - | -0.0634 | 1907C Removal of Unattractive Pairs | 1200 | constructive algorithms;greedy;math;strings |

_Plain-language reading:_ TODO

## Axis 19  (sigma = 41.26)

- enriched at `+` end: geometry (z=+2.0), ternary search (z=+1.4), brute force (z=+1.4), interactive (z=+1.3), constructive algorithms (z=+1.3)
- enriched at `-` end: meet-in-the-middle (z=-3.4), flows (z=-2.7), fft (z=-2.2), divide and conquer (z=-1.9), sortings (z=-1.6)
- corr(loading, problem rating) = -0.01; mean rating of `+` end 1160, of `-` end 1273
- user scores: std 0.216

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.2115 | 1800C2 Powering the Hero (hard version) | 1100 | data structures;greedy |
| + | +0.1962 | 1800C1 Powering the Hero (easy version) | 1000 | data structures;greedy |
| + | +0.1527 | 1800D Remove Two Letters | 1200 | data structures;greedy;hashing;strings |
| + | +0.1465 | 1800B Count the Number of Pairs | 1000 | greedy;strings |
| + | +0.0979 | 1791E Negatives and Positives | 1100 | dp;greedy;sortings |
| + | +0.0920 | 1800E1 Unforgivable Curse (easy version) | 1400 | brute force;constructive algorithms;dsu;graphs;greedy;strings |
| + | +0.0900 | 1807G1 Subsequence Addition (Easy Version) | 1100 | brute force;data structures;dp;greedy;implementation;sortings |
| + | +0.0855 | 1807G2 Subsequence Addition (Hard Version) | 1100 | bitmasks;dp;greedy;implementation;sortings |
| + | +0.0838 | 1791D Distinct Split | 1000 | brute force;greedy;strings |
| + | +0.0835 | 1800E2 Unforgivable Curse (hard version) | 1500 | brute force;constructive algorithms;dfs and similar;dsu;graphs;greedy;strings |
| + | +0.0802 | 2119B Line Segments | 1200 | geometry;greedy;math |
| + | +0.0793 | 1927D Find the Different Ones! | 1300 | binary search;brute force;data structures;dp;dsu;greedy;two pointers |
| + | +0.0777 | 1791G1 Teleporters (Easy Version) | 1100 | greedy;sortings |
| + | +0.0738 | 2118B Make It Permutation | 1200 | constructive algorithms |
| + | +0.0725 | 1997B Make Three Regions | 1100 | constructive algorithms;two pointers |
| - | -0.1601 | 1844C Particles | 1300 | dp;greedy;implementation;math |
| - | -0.1420 | 1684C Column Swapping | 1400 | brute force;constructive algorithms;greedy;implementation;sortings |
| - | -0.1152 | 1844D Row Major | 1400 | constructive algorithms;greedy;math;number theory;strings |
| - | -0.0924 | 1914E1 Game with Marbles (Easy Version) | 1400 | brute force;games;greedy;sortings |
| - | -0.0911 | 1857D Strong Vertices | 1300 | math;sortings;trees |
| - | -0.0903 | 1914E2 Game with Marbles (Hard Version) | 1400 | games;greedy;sortings |
| - | -0.0865 | 1669G Fall Down | 1200 | dfs and similar;implementation |
| - | -0.0803 | 1669E 2-Letter Strings | 1200 | data structures;math;strings |
| - | -0.0761 | 1669F Eating Candies | 1100 | binary search;data structures;greedy;two pointers |
| - | -0.0750 | 1909I Short Permutation Problem | 1900 | combinatorics;dp;fft;math |
| - | -0.0745 | 1844B Permutations & Primes | 1000 | constructive algorithms;math |
| - | -0.0740 | 2072D For Wizards, the Exam Is Easy, but I Couldn't Handle It | 1300 | brute force;greedy;implementation |
| - | -0.0726 | 1809B Points on Plane | 1000 | binary search;greedy;math |
| - | -0.0710 | 1840B Binary Cafe | 1100 | bitmasks;combinatorics;math |
| - | -0.0703 | 1811C Restore the Array | 1100 | constructive algorithms;greedy |

_Plain-language reading:_ TODO

## Axis 20  (sigma = 40.84)

- enriched at `+` end: math (z=+2.9), constructive algorithms (z=+2.7), number theory (z=+2.3), bitmasks (z=+2.0), interactive (z=+1.9)
- enriched at `-` end: two pointers (z=-3.5), games (z=-2.5), data structures (z=-1.9), strings (z=-1.4), implementation (z=-1.3)
- corr(loading, problem rating) = +0.01; mean rating of `+` end 1207, of `-` end 1267
- user scores: std 0.213

| end | loading | problem | rating | tags |
|---|---|---|---|---|
| + | +0.2035 | 1857C Assembly via Minimums | 1200 | greedy;sortings |
| + | +0.2015 | 1857D Strong Vertices | 1300 | math;sortings;trees |
| + | +0.1590 | 1857B Maximum Rounding | 1100 | greedy;implementation;math |
| + | +0.1295 | 1872D Plus Minus Permutation | 1200 | math |
| + | +0.1216 | 2072D For Wizards, the Exam Is Easy, but I Couldn't Handle It | 1300 | brute force;greedy;implementation |
| + | +0.1088 | 1872C Non-coprime Split | 1100 | math;number theory |
| + | +0.1053 | 2072E Do You Love Your Hero and His Two-Hit Multi-Target Attacks? | 1500 | binary search;brute force;constructive algorithms;dp;geometry;greedy;math |
| + | +0.1021 | 1800C2 Powering the Hero (hard version) | 1100 | data structures;greedy |
| + | +0.1013 | 1979C Earning on Bets | 1200 | binary search;combinatorics;constructive algorithms;number theory |
| + | +0.0977 | 1862D Ice Cream Balls | 1300 | binary search;combinatorics;constructive algorithms;math |
| + | +0.0895 | 1800D Remove Two Letters | 1200 | data structures;greedy;hashing;strings |
| + | +0.0881 | 1800C1 Powering the Hero (easy version) | 1000 | data structures;greedy |
| + | +0.0815 | 1872B The Corridor or There and Back Again | 900 | greedy;implementation |
| + | +0.0813 | 1872E Data Structures Fan | 1500 | binary search;bitmasks;data structures;dp |
| + | +0.0789 | 1983B Corner Twist | 1200 | constructive algorithms;greedy;implementation;math |
| - | -0.1320 | 1927D Find the Different Ones! | 1300 | binary search;brute force;data structures;dp;dsu;greedy;two pointers |
| - | -0.0971 | 1633C Kill the Monster | 1100 | brute force;math |
| - | -0.0882 | 1980C Sofia and the Lost Operations | 1300 | constructive algorithms;greedy |
| - | -0.0879 | 1986C Update Queries | 1100 | data structures;greedy;sortings |
| - | -0.0787 | 1669F Eating Candies | 1100 | binary search;data structures;greedy;two pointers |
| - | -0.0774 | 1986D Mathematical Problem | 1400 | brute force;dp;greedy;implementation;math;two pointers |
| - | -0.0759 | 1986B Matrix Stabilization | 1000 | brute force;data structures;greedy;sortings |
| - | -0.0746 | 1927E Klever Permutation | 1400 | constructive algorithms;math;two pointers |
| - | -0.0733 | 1669G Fall Down | 1200 | dfs and similar;implementation |
| - | -0.0730 | 1914E1 Game with Marbles (Easy Version) | 1400 | brute force;games;greedy;sortings |
| - | -0.0719 | 1980D GCD-sequence | 1400 | greedy;implementation;math;number theory |
| - | -0.0708 | 1669E 2-Letter Strings | 1200 | data structures;math;strings |
| - | -0.0691 | 1860B Fancy Coins | 1200 | binary search;brute force;greedy;math |
| - | -0.0681 | 1914E2 Game with Marbles (Hard Version) | 1400 | games;greedy;sortings |
| - | -0.0679 | 1996D Fun | 1500 | binary search;brute force;combinatorics;math;number theory |

_Plain-language reading:_ TODO
