#!/usr/bin/env python3
import sys, csv, re
def parse(line):
    line=line.strip()
    if not line: return None
    parts = list(csv.reader([line], delimiter='\t'))[0]
    if len(parts) < 6:
        parts = re.split(r'\s{2,}', line)
    return parts if len(parts) >= 6 else None

for line in sys.stdin:
    parts = parse(line)
    if not parts: continue
    category = parts[3].strip()
    amount = parts[4].strip()
    try:
        a = float(amount)
    except:
        continue
    print(f"{category}\t{a}")