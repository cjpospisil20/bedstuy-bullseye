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
| **"Indoors" written into the space screen** | The Crown Inn's only candidate area turned out to be its backyard, and the season runs through winter. The notes had said "the back area is the candidate space" for weeks without anyone flagging it was open to the sky |
| **First venue lost to outreach rather than analysis** | The Crown Inn was contacted and was not interested. It was also the commissioner's contact's strongest pick. `called_on` / `spoke_to` are populated for the first time |
| **Opponent-travel model built, then dropped** | Opponents travel to the home bar and it had never been scored; the opponent centre of mass sits in Gowanus / north Park Slope, 3.15 km from the team centre, and it reordered the top group. CJ: doesn't care about opponent travel. Not added |
| **"Already has a dartboard" adopted as the strongest single signal** | It answers vibe *and* space at once — the two screens that have eliminated most candidates. Only one non-league bar in range has one: Halyards |
| **Union Hall added at #4 despite the worst distance in the live set** | CJ has stood in it. Firsthand space beats a better number every time — it is the constraint that has eliminated more candidates than anything else |
| **"Vibe" promoted to a fifth screen on the site** | It had quietly eliminated five venues — Doris, Washington Commons, Sound + Fury, Threes Brewing, Rustik Tavern — four of them with ample room, while the site still listed only four screens |
| **Household weighting considered and rejected** | `household_size` looks like a weight but is not: roster rows are one-per-player, so multiplying by it double-counts the three two-player addresses. The published per-player figures were already correct. `analysis.py` now asserts the equivalence |
| **Chilo's, Captain Dan's and Sharlene's dropped without a visit** | CJ's call: Chilo's plainly lacks the interior room for even one board; Captain Dan's has no lane *and* trivia already holds Tuesday; Sharlene's shotgun room has no depth perpendicular to any wall. All three failed on evidence already in hand, so a trip would only have confirmed it |
| Site numbering switched to **sequential 1–N** | CSV ranks all 30 live bars; the site shows a curated subset, so its numbers had gaps |
| **Site order switched from the model score to post-visit likelihood** | The 19 Sept crawl made the distance/space score the weaker evidence. The site and the CSV `rank` now order the live set by how likely each bar is to actually host us; `total_score` is left untouched as the pre-visit model, so the two columns deliberately disagree |
| **Firsthand observation overturned three highly-ranked bars** | The Emerson (#1 for weeks) is a pool bar with a Tuesday queue for the table; Fulton Grand's shuffleboard back room was secondhand and did not exist as described; Black Forest has floor area but no wall. All three scored well on paper |
| **The Layup promoted from #9 to #1** | Every listing said nine screens and no darts. In person: two workable board positions and a Division 4 player from 773 Lounge behind the bar, already lobbying his own management. The strongest insider of the entire search |
| **McMahon's "corporate" impression recorded but not acted on** | CJ's read was that it felt corporate, which would fail the not-a-chain screen. Both owners answer personal mobiles and it is a single location that took over O'Connor's, so the objection was rewritten as atmosphere rather than ownership |
| **Branded Saloon's candidate room moved upstairs → basement** | The basement just lost its pool table and the bar is actively seeking a replacement activity. Tuesday comedy runs upstairs, so it does not collide. Also logged: it is a queer bar and suits a queer or queer-friendly team |
| **A `.gitignore` finally added** | The repo is public and had none, so `PROGRESS.md`'s "never commit `roster.csv`" warning rested entirely on memory. Also covers `.context/`, which now holds owners' personal phone numbers |
| **Personal contacts kept out of everything public** | Owners' mobiles live only in `COMMISSIONER-VENUE-BRIEF.md`, which is committed to the **private** master repo and must never reach the public one. First names plus roles stay in the CSV, following the existing "owner Gina" pattern |

---

## Known gotchas for whoever picks this up

- **`analysis.py` was broken and is now fixed.** It referenced `r["people"]` and `r["label"]`,
  columns that do not exist in the current `roster.csv`, so it raised `KeyError` on every run.
  It now reproduces the published centroid, geometric median and 3.56 km/player exactly.
- **A listing's "Updated <month>" is not a trading status.** Kubo was recorded as open on the
  strength of a Yelp title reading "Updated September 2026"; that describes the page, not the
  business. Google showed it temporarily closed. Yelp and Toast both 403 automated fetches, so
  current status often cannot be read programmatically — check a venue's own channels, or ask.
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

**Seven candidates in play**, reordered on 28 Sept by *likelihood of actually
hosting us* rather than by the distance/space model. Led by **The Layup** and
**Bilt Bar**, the two with a person on the inside who wants this.

The 19 September crawl was the most informative day of the project and the most
destructive to the prior ranking:

- **The Emerson**, #1 for weeks, is a pool bar — ten people waiting for the table
  with cues in hand at 6pm on a Tuesday, and the only usable wall is the one the
  table occupies.
- **Fulton Grand** and **Black Forest** are out on space and vibe.
- **The Layup** went from #9 to #1 on a single conversation.

**A separate brief for the League Commissioner**, `COMMISSIONER-VENUE-BRIEF.md`
— per-bar suitability, contacts, demographics and dartboard status, ordered most
to least likely. It carries **bar owners' personal mobile numbers**, so:

- It **is** committed to the private master repo (`~/Desktop/New Darts Bar/`).
- It must **never** appear in the public repo — this file you are reading is
  copied into `public/` by hand, and that hand copy is the one step in the
  publishing pipeline with no automated leak check behind it. `build_public.py`
  guards the map page; nothing guards a stray `cp`.

**Open items:**

1. **Reach The Layup's ownership via Dominick.** Dominick tends bar there and
   plays for 773 Lounge in Division 4; he cannot get a hearing on his own. We
   have no number for him — we left a card — but **Matt, the 773 captain, is his
   team captain and can introduce us.** One step, entirely inside the league.
2. **Call Branded Saloon.** Email to brandedsaloon@gmail.com has gone unanswered;
   the basement is the best room found and they want an activity for it.
3. **Walk into Dram Shop.** It has hosted a league team before, which is the
   strongest signal available, but nobody has been and there is no contact.
4. **Ask the Commissioner about McMahon's** — abundant space, no obstacles, but
   it would mean a private upstairs function room rather than a bar floor.
5. **Union Hall** was never visited. Unresolved, not ruled out.
6. **Contacts still missing** from the brief: numbers for Dram Shop, Halyards and
   Union Hall, plus the Instagram handles for Fulton Grand and Black Forest.
