#!/bin/bash
# bbox covering the whole map extent: S,W,N,E
BBOX="40.6448,-74.0185,40.7346,-73.9025"
Q="[out:json][timeout:90];
(
  way($BBOX)[highway~\"^(motorway|trunk|primary|secondary|tertiary)$\"];
  way($BBOX)[highway=residential];
  way($BBOX)[natural=water];
  way($BBOX)[leisure=park];
  way($BBOX)[landuse~\"^(cemetery|grass)$\"];
  relation($BBOX)[natural=water];
);
out geom;"
for M in https://overpass-api.de/api/interpreter https://overpass.kumi.systems/api/interpreter https://overpass.openstreetmap.ru/api/interpreter; do
  for try in 1 2 3; do
    echo ">> $M (attempt $try)" >&2
    curl -s -m 120 -A "brooklyn-darts-map/1.0" "$M" --data-urlencode "data=$Q" -o osm_raw.json
    if head -c 20 osm_raw.json | grep -q '{'; then
      SZ=$(wc -c < osm_raw.json); echo ">> OK $SZ bytes" >&2; exit 0
    fi
    sleep 4
  done
done
echo ">> all mirrors failed" >&2; exit 1
