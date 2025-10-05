#!/usr/bin/env python3
import sys

# Q1: Nombre d'achats effectués pour chaque catégorie
category_count = {}

for line in sys.stdin:
    category, count = line.strip().split('\t', 1)
    count = int(count)
    category_count[category] = category_count.get(category, 0) + count

# Afficher les résultats triés par catégorie
for category in sorted(category_count.keys()):
    print(f"{category}\t{category_count[category]}")