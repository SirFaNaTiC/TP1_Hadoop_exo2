#!/usr/bin/env python3
import sys

# Q2: Somme totale dépensée pour chaque catégorie
category_total = {}

for line in sys.stdin:
    category, amount = line.strip().split('\t', 1)
    amount = float(amount)
    category_total[category] = category_total.get(category, 0) + amount

# Afficher les résultats triés par catégorie avec 2 décimales
for category in sorted(category_total.keys()):
    print(f"{category}\t{category_total[category]:.2f}")