import json, math

lat0, lon0 = 40.6942, -73.9605
KM_LAT = 111.32; KM_LON = 111.32*math.cos(math.radians(lat0))
W, H = 980, 1000
def proj(la, lo):
    return ((lo-lon0)*KM_LON+4.9)*100, (4.5-(la-lat0)*KM_LAT)*100

def dp(pts, eps):                      # Douglas-Peucker
    if len(pts) < 3: return pts
    a, b = pts[0], pts[-1]
    dx, dy = b[0]-a[0], b[1]-a[1]
    n = math.hypot(dx, dy)
    idx, dmax = 0, -1
    for i in range(1, len(pts)-1):
        p = pts[i]
        d = abs(dy*p[0]-dx*p[1]+b[0]*a[1]-b[1]*a[0])/n if n else math.hypot(p[0]-a[0], p[1]-a[1])
        if d > dmax: idx, dmax = i, d
    if dmax > eps:
        return dp(pts[:idx+1], eps)[:-1] + dp(pts[idx:], eps)
    return [a, b]

M = 60                                  # clip margin
def visible(pts):
    return any(-M <= x <= W+M and -M <= y <= H+M for x, y in pts)

def path(ways, eps, close=False):
    out = []
    for pts in ways:
        p = [proj(g['lat'], g['lon']) for g in pts]
        if len(p) < 2 or not visible(p): continue
        p = dp(p, eps)
        d = "M" + " ".join(f"{x:.1f},{y:.1f}" for x, y in p)
        if close: d += "Z"
        out.append(d)
    return "".join(out)

d = json.load(open('osm_raw.json'))
CLASSES = {
 'motorway': ([], 1.0), 'trunk': ([], 1.0), 'primary': ([], 0.9),
 'secondary': ([], 0.9), 'tertiary': ([], 1.1), 'residential': ([], 1.4),
}
water, park = [], []
for e in d['elements']:
    t = e.get('tags', {})
    g = e.get('geometry')
    if e['type'] == 'relation':
        for m in e.get('members', []):
            if m.get('geometry') and t.get('natural') == 'water':
                water.append(m['geometry'])
        continue
    if not g: continue
    hw = t.get('highway')
    if hw in CLASSES: CLASSES[hw][0].append(g)
    elif t.get('natural') == 'water': water.append(g)
    elif t.get('leisure') == 'park' or t.get('landuse') in ('cemetery', 'grass'): park.append(g)

layers = {}
layers['water'] = path(water, 1.2, close=True)
layers['park']  = path(park,  1.2, close=True)
for k, (ways, eps) in CLASSES.items():
    layers[k] = path(ways, eps)

tot = sum(len(v) for v in layers.values())
for k, v in layers.items(): print(f"  {k:<12}{len(v):>9,} chars")
print(f"  {'TOTAL':<12}{tot:>9,} chars  (~{tot/1024:.0f} KB)")
json.dump(layers, open('basemap.json', 'w'))
