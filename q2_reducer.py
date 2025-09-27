#!/usr/bin/env python3
import sys

category_total = {}

for line in sys.stdin:
    category, amount = line.strip().split('\t', 1)
    amount = float(amount)
    category_total[category] = category_total.get(category, 0) + amount

for category, total in category_total.items():
    print(f"{category}\t{total}")