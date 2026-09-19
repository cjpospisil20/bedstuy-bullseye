# Brooklyn Darts — Home Bar Search: Full Context

**Last updated:** 2026-09-18 · **For:** anyone picking this up cold

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
| **Room to throw** | ~11 ft depth, ~5 ft wall per board. **Two boards is a PREFERENCE, not a requirement — one works.** |

**Room shape matters as much as size.** The lane needs depth *perpendicular* to
the wall. Long narrow bars have length and no depth — that alone has sunk
several candidates.

---

## 5. Current standing (7 in play)

| # | Bar | Address | km/player | Space | Transit 8 | Tuesday |
|---|---|---|---|---|---|---|
| 1 | The Emerson | 561 Myrtle Ave | 3.60 | Partial — "huge inside" | 6/8 | Clear |
| 2 | Branded Saloon | 603 Vanderbilt Ave | 4.18 | **Exceptional** | 2/8 | **Clear — verified** |
| 3 | Bilt Bar | 583 Vanderbilt Ave | 4.13 | Adequate | 2/8 | Unverified |
| 4 | The Crown Inn | 724 Franklin Ave | 4.46 | Unknown | 0/8 | Trivia — may coexist |
| 5 | Fulton Grand | 1011 Fulton St | 3.91 | **Confirmed good** | **8/8** | Unverified |
| 6 | The Layup | 47 5th Ave | 4.35 | Unknown | 6/8 | Unverified |
| 7 | Sharlene's | 353 Flatbush Ave | 4.23 | Wrong shape | 6/8 | Unverified |

### Key facts per candidate
- **The Emerson** — owner Gina, independent since 2010, cash only, no kitchen
  (BYO/delivery). **Already runs APA pool league nights** — a bar that already
  says yes to leagues. One block from Moot Bar (a league bar), which CJ counts
  as a plus.
- **Branded Saloon** — queer owned and operated. Back performance room
  (capacity 120) **plus substantial upstairs**. Tuesday confirmed free from
  their public Google Calendar: 2 Tuesday events in all of 2026 vs 24 Sundays.
- **Fulton Grand** — back room formerly used for shuffleboard (a 22-ft table, so
  depth is not in question). Same ownership team as Washington Commons and 4th
  Ave Pub. CJ's caveat: vibe doesn't obviously say darts.
- **Sharlene's** — good transit, wrong geometry: long narrow room, tables down
  the one long wall.

---

## 6. Ruled out — and why (22 venues)

**By CJ in person:** Hartley's (small, wrong fit) · Glorietta Baldy's (same) ·
Washington Commons (low vibe + 0/8 transit) · Doris (vibe) ·
Fulton Hall (no visible play space — **note: its "corporate" label was wrong,
Vortex Hospitality runs only 4 venues; ownership was NOT the reason**)

**On space, without a visit (CJ's call, 18 Sept):**
**Chilo's** (clearly not enough room inside for one board, let alone two — everything
else about it was strong) · **Captain Dan's Good Time Tavern** (no room for a lane
*and* trivia already holds Tuesday at 7:30 — two strikes on the two screens that
matter, so not worth the trip; it was 8/8 on transit and third-closest of anything
considered, which is what makes it the most expensive loss on the list)

**Tuesday conflict:** C'mon Everybody (music venue books Tuesdays) ·
Tip Top Bar & Grill (closed Tuesdays entirely)

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

### Rebuild workflow
```bash
python3 page_tpl.py      # regenerate darts-map.html
python3 build_public.py  # regenerate public/index.html (redacted)
cd public && git add -A && git commit -m "..." && git push
```
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

CJ is visiting venues. The two questions that decide it:

1. **~11 ft of clear depth perpendicular to a wall**, out of the path to the
   bathroom and the bar. This is the number that has killed candidates.
2. **Is it free on Tuesdays?** — and at the Crown Inn, is the back separable while
   trivia runs?

Also worth asking: at Branded Saloon, whether the **upstairs** is available on a
*recurring* Tuesday; at Fulton Grand, whether the **back room is still free**
and whether they'd actually want a league night.

Record answers in `MASTER-BAR-LIST.csv` and re-run the scoring.
