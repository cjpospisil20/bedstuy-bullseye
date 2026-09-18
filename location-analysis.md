> **Note:** this public copy has player street numbers removed and all coordinates
> rounded to three decimal places (~100 m). Locations are given by street and
> neighbourhood only.

# New Home Bar — Location Analysis
**Date:** 2026-09-18 · **Teams:** 2 · **Players:** 15 · **Prepared for:** CJ Pospisil

---

## Headline

**Target zone: south-central Bed-Stuy — the box bounded by Lafayette Ave (N),
Fulton St (S), Classon Ave (W), and Tompkins Ave (E).** Bullseye is roughly
**Gates Ave & Bedford Ave**.

**Crown Heights is the wrong answer.** It ranked last of ten candidate zones on
transit and near-last on distance. Your instinct on Bed-Stuy was right; the
Crown Heights half of the guess costs the team real travel time.

---

## 1. Where everyone lives

15 players, 12 addresses. Geographic split:

| Cluster | Players | Addresses |
|---|---|---|
| West Brooklyn (Gowanus / Park Slope) | 3 | 3rd Ave (2), 5th Ave |
| Central (Clinton Hill / Bed-Stuy) | 4 | Willoughby (2), Willoughby, Halsey |
| East (Bushwick / Ridgewood) | 4 | Suydam, Hart, Cornelia, Cornelia |
| South (Prospect Lefferts Gardens) | 1 | Hawthorne |
| Manhattan | 3 | E 14th (2), W 105th |

The team is a **west–east barbell across north-central Brooklyn**, with a
3-person Manhattan tail. Nobody lives in Crown Heights.

## 2. Pure distance (straight-line, weighted by headcount)

| Measure | Result | Lands at |
|---|---|---|
| Weighted centroid, all 15 | 40.701, -73.952 | Flushing Ave / Broadway — *just outside the red circle's north edge* |
| **Weighted geometric median, all 15** | **40.694, -73.950** | **Myrtle-Willoughby Aves (G) — Bed-Stuy** |
| Weighted centroid, Brooklyn/Queens only | 40.688, -73.947 | Bed-Stuy, Lafayette & Marcy |
| Weighted geometric median, BK/QNS only | 40.691, -73.950 | Bed-Stuy, Bedford-Nostrand (G) |

All four converge inside a ~1.4 km blob centered on **Bed-Stuy between Myrtle
Ave and Lafayette Ave**. The geometric median (which minimizes *total* travel,
rather than being yanked around by the Upper West Side outlier) is the number
to trust: **40.694, -73.950**.

Mean travel at that point: **3.56 km per player**. At Franklin Ave/Eastern Pkwy
in Crown Heights it's **4.56 km** — a 28% increase, every single week.

## 3. Transit connectivity (the tiebreaker you asked for)

Scored by counting players who get a **one-seat ride** — no transfer — from a
service boardable within ~10 min of home.

| Rank | Candidate zone | 1-seat RAIL | 1-seat ANY | Mean km |
|---|---|---|---|---|
| 1 | **Gates & Bedford — S-C Bed-Stuy** | **8/15** | **13/15** | 3.74 |
| 2 | Classon Ave (G) — Clinton Hill | 8/15 | 12/15 | 3.67 |
| 3 | Myrtle-Willoughby (G) — N Bed-Stuy | 6/15 | 12/15 | 3.57 |
| 4 | Bedford-Nostrand (G) — C Bed-Stuy | 6/15 | 12/15 | 3.63 |
| 5 | Franklin Ave (A/C) & Fulton | 5/15 | 8/15 | 3.95 |
| 6 | Nostrand Ave (A/C) & Fulton | 4/15 | 9/15 | 3.98 |
| 7 | Kingston-Throop (C) — E Bed-Stuy | 4/15 | 8/15 | 4.12 |
| 8 | Atlantic Terminal / Barclays | 4/15 | 7/15 | 4.17 |
| 9 | Franklin Ave (2345) — Crown Hts | 1/15 | 3/15 | 4.56 |
| 10 | Nostrand Ave (3) — Crown Hts | 0/15 | 2/15 | 4.61 |

### Why Bed-Stuy wins on transit

**The G train is this team's spine.** Six players get a one-seat G ride to
Bed-Stuy: both Gowanus players and the Park Slope player board at Carroll St;
both Willoughby players board at Classon; Willoughby is already on it.
The two players at E 14th St add a clean two-seat L→G transfer at
Metropolitan/Lorimer. That's **8 of 15 players on one corridor.**

**The C train covers the outliers.** W 105th St has the C at 103rd St —
a genuine one-seat ride straight to Clinton-Washington / Franklin / Nostrand.
For your furthest-flung player (12.8 km), that is the single biggest available
win. Halsey rides the A/C in from Ralph Ave.

**The Myrtle Ave bus (B54) covers Bushwick/Ridgewood.** All four east-side
players get a no-transfer B54 ride down Myrtle, plus B26 (Halsey/Greene) and
B52 (Gates) as alternates.

**Crown Heights has none of this.** It sits on the 2/3/4/5 along Eastern
Parkway — a line essentially nobody on this team lives near. Only one player
(Hawthorne) benefits. Everyone else picks up a transfer *and* extra distance.

## 4. The red-circle constraint

Reading the map against the scale bar and known landmarks, the circle runs
roughly: north edge at South Williamsburg/Broadway (~40.699), east edge around
Ralph Ave (~-73.932), south to Bensonhurst/Ditmas (~40.62), west to the Bay
Ridge waterfront (~-74.03).

Two consequences:

1. **Bushwick and Ridgewood are outside the circle.** Four of your players live
   there and cannot host. Nothing to do about it — but it means the east side
   of the team will always be commuting in, which is exactly why B54/B26/B52
   bus coverage was weighted so heavily above.
2. **The raw centroid (40.701) lands just barely north of the circle line.**
   The geometric median (40.694) is safely inside. Another reason to use it.

The recommended zone sits comfortably inside the circle with margin on all sides.

## 5. The complication: the zone is partly occupied

| Excluded bar | Address | Conflict |
|---|---|---|
| **Moot Bar** | 579 Myrtle Ave | Sits on candidate zones A and F. Dedicated dart bar, 2 regulation boards, runs its own leagues. |
| **Fulton Ale House** | Fulton St, Bed-Stuy | Sits on candidate zone D. |

The Myrtle Ave corridor and the Fulton St corridor are both taken. **The
remaining white space is the band between them** — Lafayette / Gates / Bedford /
Tompkins — which is also the #1 transit zone. That is the search box.

## 6. Recommendation

**Search here first (in priority order):**

1. **Gates Ave, between Classon and Tompkins** — the bullseye.
2. **Bedford Ave, between Lafayette and Fulton.**
3. **Lafayette Ave, between Classon and Marcy.**
4. **Tompkins Ave, between Lafayette and Fulton.**

**Walk-to-transit test for any candidate bar** — it should clear at least three:
- [ ] ≤12 min walk to Bedford-Nostrand Ave (G)
- [ ] ≤12 min walk to Franklin Ave or Nostrand Ave (A/C)
- [ ] On or ≤5 min from the B44 / B44-SBS (Nostrand)
- [ ] On or ≤5 min from the B26 (Halsey/Greene) or B52 (Gates)
- [ ] ≤15 min walk to Classon Ave (G)

**Fallback zone** if nothing viable turns up: shift *north* to Lafayette/DeKalb
around Marcy — not south into Crown Heights. Going north keeps the G and the
buses; going south forfeits both.

---

## Method & confidence notes

- Addresses were **hand-geocoded to roughly 1–2 block accuracy**, not looked up
  through a geocoding API. Across a 13 km spread this does not move the answer —
  but the specific coordinates should not be treated as survey-grade.
- Distances are **straight-line (haversine)**, not routed travel time. The
  transit table is the corrective for that.
- The one-seat-ride score uses **service overlap**, not real timetables. It
  answers "can they get there without a transfer," not "how many minutes."
- Bar names/addresses sourced from public listings and **not independently
  verified** — confirm by phone before acting.
- `Cornelia St` read as Ridgewood, Queens; `Cornelia St` read as
  Bushwick, Brooklyn. **Confirm this is right** — if Cornelia is the
  Manhattan West Village street, the model changes.
