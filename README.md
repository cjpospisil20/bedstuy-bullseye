# Bed-Stuy Bullseye

Our two teams lost our home bar after Week 1 of the 2026 season when the venue
changed hands. This is the analysis for picking a replacement.

### **→ [Open the map](https://cjpospisil20.github.io/bedstuy-bullseye/)**

## The finding

The team's mathematical centre — the point that minimises total travel across all
fifteen players — sits in Bed-Stuy near Myrtle and Nostrand. Crown Heights, the
intuitive first guess, ranked **last of ten** candidate zones on transit.

Seven players walk or bike. The **eight who depend on transit** are the ones the
venue actually has to serve:

- **Four need the G** — Carroll St and the L→G transfer at Metropolitan
- **Two need the A/C** — including a one-seat C ride from 103rd St, 11.9 km out
- **Two need the L or the B54**

No bar sits on all three. Several sit within a short walk of both the G and the
A/C, which covers six of the eight, and the Myrtle Ave corridor picks up the last
two. So the venue test is simply: **can you walk to both the G and the C from the
front door?**

That test reorders the shortlist. The Emerson leads on distance and space but is
eighteen minutes from the C — the line two of our transit-dependent players ride.
Hartley's, Glorietta Baldy's, Fulton Grand and Doris all clear both lines.

## What's here

| File | What it is |
|---|---|
| `index.html` | The map — pins, candidate bars, transit analysis, league roster |
| `MASTER-BAR-LIST.csv` | Every bar considered, scored and ranked. The living document |
| `RANKED-BAR-LIST.md` | Written shortlist with reasoning |
| `location-analysis.md` | How the target zone was derived |
| `excluded-bars.md` | The 20 league bars already taken |
| `roster-approx.csv` | Players by street and neighbourhood |
| `analysis.py` | Weighted centroid + geometric median (Weiszfeld) |
| `build_basemap.py`, `fetch_osm.sh` | Turn OpenStreetMap data into the SVG basemap |

## Privacy

Player **street numbers and exact coordinates are not in this repository.**
Map pins are snapped to a 200 m grid and labelled by street and neighbourhood
only; distances are rounded to match. The pins show roughly where people live,
not where they live.

## Method notes

- Distances are straight-line (haversine), not routed travel time.
- Space ratings are inferred from published descriptions, **not measured** — no
  candidate has confirmed room for two regulation boards.
- Bar details come from public listings and are **unverified**. Five candidates
  turned out to be permanently closed during this search, so confirm a bar is
  trading before travelling to it.
- Street geometry © OpenStreetMap contributors, [ODbL](https://opendatacommons.org/licenses/odbl/).

## Licence

Analysis and code: MIT. Street data: ODbL, © OpenStreetMap contributors.
