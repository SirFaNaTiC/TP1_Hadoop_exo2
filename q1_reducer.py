#!/usr/bin/env python3
import sys

category_count = {}

for line in sys.stdin:
    category, count = line.strip().split('\t', 1)
    count = int(count)
    category_count[category] = category_count.get(category, 0) + count

for category, count in category_count.items():
    print(f"{category}\t{count}")