#!/usr/bin/env python3
"""
Darts home-bar location analysis.
Inputs : roster.csv (player addresses, hand-geocoded to ~1-2 block accuracy)
Outputs: centrality + transit-connectivity scoring for candidate zones.
Method : weighted centroid, weighted geometric median (Weiszfeld), and a
         one-seat-ride score based on shared MTA services between each
         player's home boardable services and each candidate's services.
"""
import csv, math

R = 6371.0
def hav(a, b):
    la1, lo1 = map(math.radians, a); la2, lo2 = map(math.radians, b)
    h = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(h))

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

if __name__ == "__main__":
    rows = list(csv.DictReader(open("roster.csv")))
    pts = [((float(r["lat"]), float(r["lon"])), int(r["people"]), r["label"], r["neighborhood"]) for r in rows]
    print("centroid        :", tuple(round(v,4) for v in centroid(pts)))
    print("geometric median:", tuple(round(v,4) for v in geomedian(pts)))
