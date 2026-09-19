# Progress Log — What We Built

**Project:** Finding a new home bar for two Brooklyn darts teams
**Session date:** 2026-09-18
**Companion doc:** `summary.md` holds the *project* context (roster, findings,
candidate detail). This file records *what was built and how* — the deliverables,
the pipelines, and the decisions behind them.

---

## Deliverables

| # | Output | Where |
|---|---|---|
| 1 | **Interactive map page** — real Brooklyn street grid, 15 player pins, 9 candidate bars, distance rings, transit and ruled-out tables | `darts-map.html` |
| 2 | **Public website** | https://cjpospisil20.github.io/bedstuy-bullseye/ |
| 3 | **Public repo** (MIT, redacted) | https://github.com/cjpospisil20/bedstuy-bullseye |
| 4 | **Private artifact** | https://claude.ai/code/artifact/2733fa9c-125b-4eb5-9116-5a217e7ed8cd |
| 5 | **Master bar list** — 44 rows × 34 columns, the living document | `MASTER-BAR-LIST.csv` |
| 6 | **Context handoff doc** | `summary.md` |
| 7 | Supporting analyses | `location-analysis.md`, `RANKED-BAR-LIST.md`, `excluded-bars.md`, `BRD-new-home-bar.md`, `league-bars.csv` |

**44 venues assessed in total:** 30 scored live, 14 disqualified.
**25 commits** to the public repo across the session.

---

## How it was built

### Phase 1 — Geographic analysis
Geocoded 15 player addresses by hand (~1–2 block accuracy). Wrote `analysis.py`
implementing a **weighted centroid** and a **weighted geometric median** via
Weiszfeld's algorithm. All four measures converged on Bed-Stuy.

Read the commissioner's league-boundary screenshot, calibrated it against its own
scale bar using two known landmarks, and traced the boundary to roughly one block.
This revealed the boundary runs on a **diagonal**, not as a bounding box — the
detail that disqualified five bars.

### Phase 2 — Transit modelling
Built a service-overlap model: each player's boardable lines within ~10 min of
home, intersected with each candidate's nearby lines, to count **one-seat rides**.
Later refined to the eight transit-dependent players once CJ identified who walks
or bikes. Verified overnight bus service (B54 runs 24h, ~20 min headways) and the
MTA Request-a-Stop programme for the late-night safety question.

### Phase 3 — Candidate research
Web research across bar guides, Yelp, Foursquare, venue sites and event
calendars. Notable techniques that worked:
- **Pulled Branded Saloon's public Google Calendar ICS feed** (4,312 events since
  2010) and aggregated by weekday to prove Tuesday is their quietest night —
  2 events in 2026 vs 24 Sundays. Far better evidence than any listing.
- Chased ownership to source: found Fulton Hall's operator via a contact email
  domain, then confirmed Vortex Hospitality runs only four venues.
- Cross-checked closure claims against multiple sources and dates, which
  untangled Chilo's close-then-reopen sequence.

### Phase 4 — The map
The artifact CSP blocks external tile servers, so Google/Mapbox tiles were
impossible. Instead:
1. `fetch_osm.sh` queries the **Overpass API** for the bounding box
   (roads by class, water, parks) — 11,879 ways, 12.6 MB raw, with mirror
   fallback and retries
2. `build_basemap.py` projects to the page's coordinate space
   (equirectangular), simplifies with **Douglas-Peucker**, clips to viewport,
   and emits layered SVG paths — 340 KB
3. `build_page.py` renders roads **casing-then-fill by class**, the way real map
   renderers do, which is what gives streets their edges
4. `page_tpl.py` assembles the full page

Result: a genuine street map, fully self-contained, no network calls at runtime.
Street data © OpenStreetMap contributors (ODbL), credited on the page.

**Design:** palette drawn from a real dartboard (cream `#F0EAD9`, board red
`#BC2F26`, board green `#1B6E4A`, brass `#8A7340`); Anton / Archivo / IBM Plex
Mono; full light and dark cartography.

### Phase 5 — Publishing and privacy
`build_public.py` generates the redacted public copy:
- Player pins **snapped to a ~200 m grid**
- Street numbers stripped; street + neighborhood only
- Distances rounded to match
- Coordinates rounded to 3 dp in supporting docs
- **Automated leak check** printed on every run

A subtle catch found during audit: the geometric median printed to 4 dp *is*
Julie's address, so publishing it precisely would have pinpointed her even with
her own row redacted. Rounded.

---

## Decisions and reversals worth remembering

| Decision | Why |
|---|---|
| Weighted space at **70%** over proximity 30% | Space is the binding constraint; distance varies little among candidates |
| Two boards reframed as a **preference** | CJ's call — one lane is workable, it just runs slower |
| Ownership screen changed from "independent only" to **"not a chain"** | Small local groups of 3–4 venues are fine |
| Transit recalculated for **8 players, not 15** | Seven walk or bike, so they don't constrain the venue |
| Rings re-centred on the **team centre**, not The Emerson | Neutral reference once The Emerson stopped being the default pick |
| **Fulton Hall "corporate" label retracted** | Published on secondhand information; verification showed a 4-venue local group. Ownership was never the reason — no visible play space was |
| Ruled-out bars **kept with reasons**, not deleted | Stops anyone re-suggesting them |
| **Searched by venue *category*, not just geography** | The first 44 were almost all cocktail bars, dives and wine bars — the category that fails an 11 ft depth test. Widening to beer halls, taprooms, bocce/game bars and social clubs surfaced Union Hall and four others in one pass |
| **Union Hall added at #4 despite the worst distance in the live set** | CJ has stood in it. Firsthand space beats a better number every time — it is the constraint that has eliminated more candidates than anything else |
| **"Vibe" promoted to a fifth screen on the site** | It had quietly eliminated five venues — Doris, Washington Commons, Sound + Fury, Threes Brewing, Rustik Tavern — four of them with ample room, while the site still listed only four screens |
| **Household weighting considered and rejected** | `household_size` looks like a weight but is not: roster rows are one-per-player, so multiplying by it double-counts the three two-player addresses. The published per-player figures were already correct. `analysis.py` now asserts the equivalence |
| **Chilo's, Captain Dan's and Sharlene's dropped without a visit** | CJ's call: Chilo's plainly lacks the interior room for even one board; Captain Dan's has no lane *and* trivia already holds Tuesday; Sharlene's shotgun room has no depth perpendicular to any wall. All three failed on evidence already in hand, so a trip would only have confirmed it |
| Site numbering switched to **sequential 1–N** | CSV ranks all 30 live bars; the site shows a curated subset, so its numbers had gaps |

---

## Known gotchas for whoever picks this up

- **`analysis.py` was broken and is now fixed.** It referenced `r["people"]` and `r["label"]`,
  columns that do not exist in the current `roster.csv`, so it raised `KeyError` on every run.
  It now reproduces the published centroid, geometric median and 3.56 km/player exactly.
- **Do not weight by `household_size`.** See the note in `summary.md` §2 — it double-counts
  the six players who share an address with a teammate.
- **`basemap.svg` and `osm_raw.json` are gitignored build artifacts.** If missing:
  `./fetch_osm.sh && python3 build_basemap.py && python3 build_page.py`
- **Never edit `darts-map.html` directly** — it is generated. Edit `page_tpl.py`.
- **An artifact publish can fail silently** with "outcome unknown". It happened
  once here. Verify the live artifact before assuming it landed.
- **GitHub Pages takes 30–60 s** to rebuild after a push.
- **Never commit `roster.csv`** to the public repo — it holds exact addresses.
  `build_public.py`'s leak check is the guard; do not push if it flags anything.

---

## Rebuild in three commands

```bash
python3 page_tpl.py                 # darts-map.html
python3 build_public.py             # public/index.html, prints leak check
cd public && git add -A && git commit -m "..." && git push
```
Then republish the artifact with the same file path to keep the URL.

---

## State at hand-off

**8 candidates in play**, ranked 1–8 on the site, led by The Emerson and Branded
Saloon. Chilo's, Captain Dan's, Sharlene's and Doppelgänger were dropped on 18 Sept
without a visit (see the decision log above), and **Union Hall was added at #4 on CJ's
firsthand confirmation of its space** — the only candidate he has vouched for himself.
**Black Forest Brooklyn** joined at #7 on CJ's read that a beer hall may be big enough to
run trivia and darts at once; its real blocker is the 10pm Tuesday close, not the trivia.
Rustik Tavern was ruled out (closed Tuesdays, and a restaurant that would not want a board). CJ is visiting venues today or tomorrow. The two open questions
are unchanged and can only be answered in person:

1. **~11 ft of clear depth perpendicular to a wall** — the number that has
   eliminated more candidates than anything else
2. **Is Tuesday genuinely free?** — and at the Crown Inn, is the back separable
   while trivia runs?

Visit results go in `MASTER-BAR-LIST.csv` under `called_on`, `spoke_to`,
`two_boards_confirmed`, `tuesday_confirmed`, `outcome`. Re-run the scoring after.
