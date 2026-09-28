# Brooklyn Darts — Home Bar Search: Full Context

**Last updated:** 2026-09-28 · **For:** anyone picking this up cold

---

## 1. The situation

CJ Pospisil runs **two steel-tip darts teams — 15 players total** — in a Brooklyn
league. Every team must have a home bar; opponents travel to it.

**They lost their home bar after Week 1 of the 2026 season.** The venue was sold
and the new owner stopped responding — the arrangement was informal and tied to
the previous individuals, so it didn't survive the sale. The season is already
underway, so this is a live problem, not a planning exercise.

### The deal on offer to a bar
- Bar pays **$125 per team per season — $250 for both**
- In exchange: **15–16 people, Tuesday nights, 3–4.5 hours, ~15 match nights**
- Estimated season value to the bar: **$6,750–$9,000** (≈27–36× the fee)
- Bars do **not** need to already own dartboards — the teams are recruiting bars
  into the league, and many won't know it exists
- CJ is in contact with the league commissioner, who is helping

---

## 2. The roster

15 players. **Seven walk or bike** and drop out of the venue calculation.
**Eight depend on transit** — they are the group the venue has to serve.

| Player | Neighborhood | Transit-dependent? | Line they need |
|---|---|---|---|
| Julie | Bed-Stuy (Willoughby Ave) | no — walks | — |
| Joe | Clinton Hill (Willoughby Ave) | no — walks | — |
| Michelle | Clinton Hill (Willoughby Ave) | no — walks | — |
| Matt | Bushwick (Suydam St) | no — bikes | — |
| Josh | Ridgewood (Cornelia St) | no — bikes | — |
| Isaac | Park Slope (5th Ave) | no — bikes | — |
| CJ | Prospect Lefferts Gardens (Hawthorne St) | no — bikes | — |
| **Mark** | Gowanus (3rd Ave) | **yes** | G |
| **Olivia** | Gowanus (3rd Ave) | **yes** | G |
| **Craig** | Manhattan (E 14th St) | **yes** | G (via L) |
| **Elle** | Manhattan (E 14th St) | **yes** | G (via L) |
| **Hayley** | Bed-Stuy East (Halsey St) | **yes** | A/C |
| **Chris** | Upper West Side (W 105th St) | **yes** | A/C — one-seat C from 103rd |
| **Mitch** | Bushwick (Hart St) | **yes** | L or B54 |
| **Lulu** | Bushwick (Cornelia St) | **yes** | L or B54 |

**Four need the G, two need the A/C, two need the L or B54.** No venue sits on
all three. The practical venue test: **can you walk to both the G and the C from
the front door?**

> **Weighting, and a trap.** `roster.csv` holds **one row per player** — 15 rows, 15
> players. Three addresses house two players each, and each of those players has their own
> row, so `household_size` is *not* a weight: multiplying by it double-counts those six
> people (21 units for 15 players) and drags the optimum toward Clinton Hill, Gowanus and
> Manhattan. Every published figure uses one unit per player row, which is already the
> correct per-player measure. `analysis.py` asserts the equivalence with
> address-weighted-by-headcount so this cannot silently regress.

> Exact street addresses are in `roster.csv` (local only — never published).
> The public repo carries `roster-approx.csv` with street and neighborhood only.

---

## 3. The geographic finding

- **Team mathematical centre (geometric median, minimises total travel):**
  40.6947, -73.9505 — Bed-Stuy, essentially on Julie's doorstep
- **Mean travel at that point:** 3.56 km/player
- **Crown Heights — the intuitive first guess — ranked LAST of ten zones.**
  It sits on the 2/3/4/5 along Eastern Parkway, a line almost nobody lives near.
  At 4.56 km/player it costs 28% more travel than the optimum.
- **Bushwick and Ridgewood are outside the league boundary**, so four players
  will always commute in.

The league boundary (from the commissioner's map screenshot) cuts on a
**diagonal**: its eastern edge is near Marcy Ave at Myrtle latitude but out at
Stuyvesant Ave by Fulton St. Bars east of that line are a hard no.

---

## 4. Non-negotiables and preferences

| Screen | Rule |
|---|---|
| **Not a chain** | Small local groups of 3–4 venues are fine. A corporation running dozens is not. |
| **Inside the league boundary** | Fixed by the commissioner's map |
| **Free on Tuesdays** | 3–4.5 hours, 15–16 people |
| **Room to throw** | ~11 ft depth, ~5 ft wall per board, and **INDOORS** — the season runs Tuesdays through winter, so a yard, patio or beer garden is not play space however big. **Two boards is a PREFERENCE, not a requirement — one works.** |
| **Vibe** | The bar has to suit a loud, standing, four-hour weekly night. A judgement, not a measurement — CJ's to make. Has cost five venues, four of them with ample room. |

**Room shape matters as much as size.** The lane needs depth *perpendicular* to
the wall. Long narrow bars have length and no depth — that alone has sunk
several candidates.

---

## 5. Current standing (7 in play)

Ordered by **how likely each bar is to actually host us** after the 19 September
crawl — firsthand evidence, not the distance/space model that ordered this list
before. The CSV `rank` follows this order; `total_score` is left untouched as the
pre-visit model, so the two columns deliberately disagree.

| # | Bar | Address | km/player | Space | Transit 8 | Status after the crawl |
|---|---|---|---|---|---|---|
| 1 | **Branded Saloon** | 603 Vanderbilt Ave | 4.18 | **Basement, seen — best room** | 2/8 | Bar wants an activity; no reply yet |
| 2 | **The Layup** | 47 5th Ave | 4.35 | **Two board spots, seen** | 6/8 | Best prospect; ownership unreachable |
| 3 | **Bilt Bar** | 583 Vanderbilt Ave | 4.13 | **One board, seen** | 2/8 | Owner interested, contact in hand |
| 4 | The Dram Shop | 339 9th St | 5.30 | Darts, pool & shuffleboard | 4/8 | Has hosted a team before; not visited |
| 5 | McMahon's Public House | 39 5th Ave | 4.35 | **Large private upstairs, seen** | 6/8 | Space fine; is it the right *kind* of venue? |
| 6 | Halyards | 406 3rd Ave | 4.91 | **Board seen — badly sited** | 4/8 | Fallback only |
| 7 | Union Hall | 702 Union St | 4.52 | Confirmed, CJ firsthand | 4/8 | Not visited on the crawl; unresolved |

### Key facts per candidate

- **The Layup** — went from #9 to #1 on one conversation. Every listing called it
  a nine-screen sports bar with its walls spoken for; in person there are **two
  separate spots** a board would fit. **Dominick**, a bartender there, plays for
  **773 Lounge in Division 4** and has been pushing his own management for a
  board for a while without getting a hearing. We left a card but have no number;
  the route to him is **Matt, the 773 captain**, who is his team captain. The
  demographic fits darts as squarely as anywhere assessed. Ownership changed
  hands this year, which may explain the silence.
- **Bilt Bar** — the board would replace two pinball tables in the back. **One
  board only**, and the area is tight for a full team. Co-owner **Laney is a
  darts player herself** and is interested, though clear she could not run it.
  Replied on Instagram; direct number held in the commissioner's brief, not here.
- **The Dram Shop** — **it has hosted a darts team before**, per Mac Diller, met
  at Bilt Bar, who played on it. Darts, pool *and* shuffleboard, and the Brooklyn
  APA Pool League runs from the address. Strongest possible signal that the room
  works — but **nobody has been and there is no contact**, and 5.30 km is further
  than the old home bar.
- **Branded Saloon** — the candidate room is the **basement**, not the upstairs
  assumed pre-visit. It recently lost its pool table and **the bar is openly
  looking for an activity to replace it** — the only venue actively seeking what
  we are offering. The visit turned up a Tuesday comedy night the calendar did
  not show; it runs *upstairs*, so it does not collide. Emailed the owner, no
  reply. **Queer owned and operated** — suits a queer or queer-friendly team, and
  worth matching deliberately rather than by default.
- **McMahon's Public House** — a large **private upstairs event room**, more clear
  wall than anything else assessed. Two catches, neither about size: the room
  *feels* like a corporate event space even though the ownership is not (single
  location, took over O'Connor's, both owners reachable on personal mobiles), and
  a board behind a closed upstairs door gets no passing trade. A question about
  what the league wants a home bar to be.
- **Halyards** — the board is real, and that is the problem. It hangs **over the
  pool table**, which is in demand; the cellar door the barbacks use is right
  beside the throw line; sightlines fit about eight people. Workable if desperate,
  a weekly source of friction otherwise.
- **Union Hall** — never visited on the crawl. The room is not in doubt — 5,000
  sq ft, two indoor bocce courts, already hosts an outside league on Mondays —
  but they run a great deal of programming and the read is that darts would be
  one thing too many. **Unresolved rather than ruled out.**

---

## 6. Ruled out — and why (36 venues)

**Ruled out on the 19 Sept crawl — all seen in person:**
**The Emerson** (561 Myrtle Ave — **it is a pool bar**. Ten people sitting with cues in
hand waiting for the table at 6pm on a Tuesday, and the only wall a board could use is
the one the pool table occupies. It led this list on distance, transit and every written
description of its size, and it is the most painful loss of the search) ·
**Fulton Grand** (1011 Fulton St — cramped, nowhere to hang a board, and not the vibe for
a four-hour standing night. **Its shuffleboard back room was secondhand from the owner of
Moot Bar and did not exist as described** — for weeks this was the one room anyone was
said to have stood in) ·
**Black Forest** (733 Fulton St — floor area but no usable wall, and a darts night would
sit oddly in a communal-table beer hall. No one in charge reached. Costly: 8/8 on transit,
the best of anything assessed)

**Referred to the league rather than dropped:**
**Greenwood Park** (555 7th Ave, Greenwood Heights — recommended by Laney at Bilt Bar, who
knows the owner. 13,000 sq ft, a kitchen, three bocce courts and an events business. **Not
for us**: an estimated 6.18 km/player, the furthest assessed, and the space is principally
open-air. But the distance objection is *ours*, not the venue's — for a team based around
South Slope, Sunset Park or Bay Ridge, where Farrell's and Shenanigans already play, it
looks well placed. Handed to the commissioner as a candidate for another team.)

**By CJ in person (earlier):** Hartley's (small, wrong fit) · Glorietta Baldy's (same) ·
Washington Commons (low vibe + 0/8 transit) · Doris (vibe) ·
Fulton Hall (no visible play space — **note: its "corporate" label was wrong,
Vortex Hospitality runs only 4 venues; ownership was NOT the reason**)

**On space, without a visit (CJ's call, 18 Sept):**
**Doppelgänger** (415 Myrtle Ave — no room for a board anywhere in the bar; this address was
on the list as *Cardiff Giant*, which closed in March 2026) ·
**Sharlene's** (no room for a board at all — a long narrow room with the bar down one
side and tables down the other leaves only the walkway between, and a lane needs depth
*perpendicular* to a wall; good transit could not fix the geometry) ·
**Chilo's** (clearly not enough room inside for one board, let alone two — everything
else about it was strong) · **Captain Dan's Good Time Tavern** (no room for a lane
*and* trivia already holds Tuesday at 7:30 — two strikes on the two screens that
matter, so not worth the trip; it was 8/8 on transit and third-closest of anything
considered, which is what makes it the most expensive loss on the list)

**Contacted and declined (18 Sept):** **The Crown Inn** (724 Franklin Ave — CJ reached out and
they were not interested; the back area it would have offered is *entirely outdoors*, no use for
a winter season, and trivia holds Tuesday. **This was the commissioner's contact's strongest
recommendation — "by far the most likely to work" — and it did not survive first contact.**)

**On vibe or ownership (18 Sept):** **Sound + Fury Brewery** (141 Lawrence St — the largest
room found in-boundary at 6,000 sq ft, but too far at 4.48 and not divey enough) ·
**Threes Brewing** (333 Douglass St — a five-site chain, past the three-to-four venue local
group the screen allows, plus the same vibe objection)

**No room, or no darts (Gowanus/Slope sweep, 18 Sept):** **Fourth Avenue Pub** (76 4th Ave —
not enough room for a board; costly, it had the best distance of the cluster at 4.32 and a
possible ownership link to Fulton Grand) · **High Dive** (243 5th Ave — surfaced on a Yelp
"dart bars" list but actually has *pinball and arcade games*, the inference that already
failed twice here) · **Littlefield** and **The Bell House** (Gowanus music venues that book
weeknights; Bell House shares owners with Union Hall)

**Tuesday conflict:** C'mon Everybody (music venue books Tuesdays) ·
Tip Top Bar & Grill (closed Tuesdays entirely) · **Rustik Tavern** (471 DeKalb Ave —
closed Mondays *and* Tuesdays, and a comfort-food restaurant that would not want a board
on the wall; painful at 3.62 km/player, the second-closest venue assessed)

**Outside the boundary:** All Night Skate (an entire arcade room — the best raw
space found anywhere) · Wonderville · Turtles All the Way Down ·
Therapy Wine Bar · Bar LunÀtico

**Permanently closed (7):** Project Parlor (*had the single best geographic
score — exactly the optimum*) · Swell Dive · The Low Post · Lover's Rock ·
Hanson Dry · Brooklyn Public House · Dynaco (temporarily — recheck)

**Unclear:** Bed-Vyne Brew (sources conflict)

**Excluded by the league** (20 bars already hold teams) — see `league-bars.csv`.
Two sit in the target zone: **Moot Bar** (579 Myrtle Ave, a dedicated dart bar)
and **Fulton Ale House** (1446 Fulton St).

---

### Two corrections found 18 Sept
1. **Cardiff Giant (415 Myrtle Ave) had been sitting in the CSV as a live rank-7 candidate
   marked OPEN — it closed in March 2026.** The address now trades as Doppelgänger, and is
   ruled out on space.
2. **Swell Dive (1013 Bedford Ave) was marked closed — the address has since had two more
   states.** Kubo, a Filipino bar, opened there 13 Feb 2026; as of Sept 2026 **Google shows
   it temporarily closed** (CJ spotted this). Held as `RECHECK IF IT REOPENS`, the same
   handling as Dynaco. At 3.65 km/player the address beats Fulton Grand on distance, so it
   is worth a recheck rather than deletion.

   ⚠️ **A bad inference to avoid repeating.** Kubo was briefly recorded here as "open as of
   Sept 2026" on the strength of a Yelp page title reading *Updated September 2026*. That
   phrase means the listing was updated, **not** that the business is trading — and Yelp and
   Toast both block automated fetching, so neither could be read live. Lesson 1 below applies
   to reopenings as much as closures, and a listing's freshness is not a venue's status.

Both are lesson 1 below running in *both* directions: listings go stale on reopenings too.

---

### What the Gowanus/Slope sweep established
CJ's old home bar, **The Bar in Gowanus, 286 Third Ave**, scored **4.72 km/player — further
than every current candidate.** So distance has never been the binding constraint, and moving
toward the Slope is not a compromise but a return to what already worked for a season.
(Mark and Olivia's roster entry uses that same address as an approximation of where they
live nearby — **this is intentional, not an error. Do not "fix" it.**)

Also established: **no bar in the ideal Bed-Stuy/Clinton Hill zone has a dartboard except
Moot Bar, which the league already holds.** Every non-league bar with a board is in
Gowanus or Park Slope. Union Hall does *not* have darts — it is bocce, and appears on dart
lists only because it is a "bar with games".

---

### Two things the Crown Inn taught us (18 Sept)
1. **Outdoor space is not space.** The season runs through winter. The Crown Inn's only
   candidate area was its backyard, and that had been sitting in the notes as "the back area
   is the candidate space" without anyone flagging that it is open to the sky. **Re-read every
   remaining candidate for this** — several lean on yards and gardens. Black Forest's beer
   garden and McMahon's back garden and patios do not count; their indoor rooms do.
2. **Insider endorsements have a poor hit rate.** Of the commissioner's contact's
   recommendations, Hartley's, Glorietta Baldy's, Washington Commons and the Crown Inn are all
   out and Hanson Dry was closed. **Only Fulton Grand survives, and it carries a vibe query.**
   A human saying "this one will work" has been no more reliable than a listing.

---

## 7. Hard-won lessons

1. **Published bar guides go stale.** Seven candidates turned out to be closed,
   including one sitting exactly on the mathematical optimum. **Always confirm a
   bar is trading before travelling to it.**
2. **Listings describe drinks and vibe, never floor plans.** Every space and
   vibe ruling has come from a person walking in — never from a search. Treat
   every `UNKNOWN` as genuinely unknown.
3. **Owning game furniture is weak evidence of space.** Pinball is a wall
   footprint, not a floor one. This inference failed twice (Hartley's,
   Glorietta).
4. **A closure announcement can be reversed.** (Chilo's is now ruled out on space,
   but the lesson stands.) Chilo's announced closing in
   Sept 2025, held a closing party, then reopened 28 Dec 2025 under new owner
   Dave Zirin. The original Instagram post still circulates and reads as current.
5. **Don't assert something you haven't verified** — the Fulton Hall "corporate"
   label was taken from conversation and published without checking. It was wrong.
6. **Secondhand rooms are not evidence.** Fulton Grand's shuffleboard back room
   was described by another bar's owner and carried here for weeks as the one
   space someone had actually stood in. It did not survive a visit. A person can
   be as stale a source as a listing.
7. **Walking in beats every source.** The 19 Sept crawl overturned three of the
   top eight and promoted The Layup from #9 to #1 — a bar every listing described
   as having no room for darts. Nothing on paper predicted either outcome.
8. **A bar's existing game furniture cuts both ways.** Halyards' board and The
   Emerson's pool table both proved the room *can* host a game and that the space
   is already spoken for. Ask who is using it, not just whether it exists.
9. **The best lead in the search was a person, not a venue.** A Division 4 player
   working behind the bar at The Layup is worth more than any amount of floor
   area, because he wants it to happen and the league can reach him.

---

## 8. Files in this folder

| File | What it is |
|---|---|
| `MASTER-BAR-LIST.csv` | **The living document.** Every bar, scored, with ownership, space notes, Tuesday status, reasons. Blank columns `called_on` / `spoke_to` / `two_boards_confirmed` / `tuesday_confirmed` / `outcome` are for visit results |
| `darts-map.html` | The map page (generated — do not edit directly) |
| `page_tpl.py` | **Source for the map page.** Edit this, then run it |
| `build_public.py` | Makes the redacted public copy into `public/` |
| `build_basemap.py`, `fetch_osm.sh` | Pull OpenStreetMap geometry and render the SVG basemap |
| `analysis.py` | Weighted centroid + geometric median (Weiszfeld) |
| `roster.csv` | **Full addresses — local only, never publish** |
| `league-bars.csv` | The 20 league bars already taken |
| `location-analysis.md`, `RANKED-BAR-LIST.md`, `excluded-bars.md` | Earlier written analyses |
| `BRD-new-home-bar.md` | Requirements doc from the initial scoping |
| `public/` | The redacted public repo — its own git remote |
| `COMMISSIONER-VENUE-BRIEF.md` | **Per-bar suitability brief for the League Commissioner.** Contacts, demographics, dartboard status, ordered most to least likely. **Never copy into `public/`** — it carries owners' personal mobile numbers |

### Rebuild workflow
```bash
python3 page_tpl.py      # regenerate darts-map.html
python3 build_public.py  # regenerate public/index.html (redacted)
cd public && git add -A && git commit -m "..."
```
**Changes to the public repo now go via a pull request**, not a direct push to
`main`. GitHub Pages publishes from `main` at root, so merging the PR is what
takes a change live — it rebuilds in 30–60 seconds.
Then republish the artifact with the `Artifact` tool, same file path.

If `basemap.svg` is missing: `./fetch_osm.sh && python3 build_basemap.py && python3 build_page.py`

---

## 9. Published outputs

- **Public site:** https://cjpospisil20.github.io/bedstuy-bullseye/
- **Repo:** https://github.com/cjpospisil20/bedstuy-bullseye (public, MIT)
- **Private artifact:** https://claude.ai/code/artifact/2733fa9c-125b-4eb5-9116-5a217e7ed8cd

### ⚠️ Privacy rule
The public copy **must never contain player street numbers or exact
coordinates.** Pins are snapped to a 200 m grid, addresses shown as street +
neighborhood only, coordinates rounded to 3 decimals. `build_public.py` performs
the redaction and prints a leak check — **do not push if it reports anything.**

---

## 10. What's next

The crawl answered the space question at eight venues. What is left is almost
entirely **reaching people**, not assessing rooms.

1. **Reach The Layup's ownership.** Go through **Matt at 773 Lounge** to reach
   **Dominick**, then approach the owners with the league behind it, framed on
   incremental weeknight revenue. One step, entirely inside the league, and the
   single highest-value action available.
2. **Call Branded Saloon.** Email has gone unanswered. Best room found, and they
   want an activity for the basement — this should not die of a missed inbox.
3. **Walk into Dram Shop.** It has hosted a team before, but nobody has been and
   there is no contact. One visit settles it; only the distance argues against.
4. **Decide about McMahon's.** Space is not the question. Does the league want a
   private upstairs function room as a home bar? That is a taste call, not ours.
5. **Union Hall** was never visited. Unresolved, not ruled out.

**Still-missing contacts** for the brief: Dram Shop, Halyards and Union Hall, plus
Instagram handles for Fulton Grand and Black Forest.

Record answers in `MASTER-BAR-LIST.csv` (`called_on`, `spoke_to`,
`two_boards_confirmed`, `tuesday_confirmed`, `outcome`) and re-run the scoring.
