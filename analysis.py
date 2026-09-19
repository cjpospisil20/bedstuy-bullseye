#!/usr/bin/env python3
"""
Darts home-bar location analysis.
Inputs : roster.csv (player addresses, hand-geocoded to ~1-2 block accuracy)
Outputs: weighted centroid, weighted geometric median (Weiszfeld), and the
         mean per-player distance for any candidate coordinate.

WEIGHTING - READ THIS BEFORE CHANGING IT
roster.csv holds ONE ROW PER PLAYER, 15 rows for 15 players. Three addresses
house two players each (Joe+Michelle in Clinton Hill, Mark+Olivia in Gowanus,
Craig+Elle in Manhattan), and those players have a row each.

So `household_size` is NOT a weight. It records how many players live at the
address, and because each of them already has their own row, multiplying by it
double-counts all six of them - 21 units of weight for 15 players - and drags
the optimum toward those three addresses. Every published figure in this
project uses one unit of weight per player row, which is the correct
per-player measure.

Weighting by address-with-player-count is mathematically identical to one unit
per player row. check_weighting() below asserts that, so the equivalence is
tested rather than trusted.
"""
import csv, math

R = 6371.0
def hav(a, b):
    la1, lo1 = map(math.radians, a); la2, lo2 = map(math.radians, b)
    h = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(h))

def load(path="roster.csv"):
    rows = list(csv.DictReader(open(path)))
    return [((float(r["lat"]), float(r["lon"])), 1, r["player"], r["neighborhood"]) for r in rows]

def centroid(sub):
    tw = sum(w for _, w, *_ in sub)
    return (sum(p[0]*w for p, w, *_ in sub)/tw, sum(p[1]*w for p, w, *_ in sub)/tw)

def geomedian(sub, iters=500):
    cur = centroid(sub)
    for _ in range(iters):
        nla = nlo = den = 0.0
        for p, w, *_ in sub:
            d = max(hav(cur, p), 1e-9); k = w/d
            nla += p[0]*k; nlo += p[1]*k; den += k
        nxt = (nla/den, nlo/den)
        if hav(cur, nxt) < 1e-7: return nxt
        cur = nxt
    return cur

def mean_km(sub, c):
    tw = sum(w for _, w, *_ in sub)
    return sum(hav(c, p)*w for p, w, *_ in sub)/tw

def check_weighting(path="roster.csv"):
    """Per-player rows == addresses weighted by players living there."""
    per_player = load(path)
    agg = {}
    for p, w, *_ in per_player:
        agg[p] = agg.get(p, 0) + w
    per_address = [(p, w, "", "") for p, w in agg.items()]
    for label, c in (("centroid", centroid), ("geomedian", geomedian)):
        a, b = c(per_player), c(per_address)
        assert hav(a, b) < 1e-6, f"{label} disagrees: {a} vs {b}"
    return len(per_player), len(per_address)

if __name__ == "__main__":
    pts = load()
    n_players, n_addrs = check_weighting()
    print(f"roster: {n_players} players across {n_addrs} addresses")
    print("weighting check : per-player == per-address-by-headcount  OK")
    print("centroid        :", tuple(round(v, 4) for v in centroid(pts)))
    gm = geomedian(pts)
    print("geometric median:", tuple(round(v, 4) for v in gm))
    print(f"mean travel     : {mean_km(pts, gm):.2f} km/player at the median")
