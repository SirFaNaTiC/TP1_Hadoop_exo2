#!/usr/bin/env python3
import sys
current = None
count = 0
for line in sys.stdin:
    line=line.strip()
    if not line: continue
    key, val = line.split('\t',1)
    try:
        v = int(val)
    except:
        continue
    if current == key:
        count += v
    else:
        if current is not None:
            print(f"{current}\t{count}")
        current = key
        count = v
if current is not None:
    print(f"{current}\t{count}")