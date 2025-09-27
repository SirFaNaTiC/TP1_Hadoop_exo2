#!/usr/bin/env python3
import sys

city_total = {}

for line in sys.stdin:
    city, amount = line.strip().split('\t', 1)
    amount = float(amount)
    city_total[city] = city_total.get(city, 0) + amount

# Trouver la ville avec le montant le plus élevé
max_city = max(city_total, key=city_total.get)
print(f"{max_city}\t{city_total[max_city]}")