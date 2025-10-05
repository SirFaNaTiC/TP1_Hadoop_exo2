#!/usr/bin/env python3
import sys
current = None
total = 0.0
for line in sys.stdin:
    line=line.strip()
    if not line: continue
    key, val = line.split('\t',1)
    try:
        v = float(val)
    except:
        continue
    if current == key:
        total += v
    else:
        if current is not None:
            print(f"{current}\t{total:.2f}")
        current = key
        total = v
if current is not None:
    print(f"{current}\t{total:.2f}")
# ensuite trier localement pour trouver la ville avec max: sort -k2 -nr | head -n1