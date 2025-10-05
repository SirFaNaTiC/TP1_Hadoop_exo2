#!/usr/bin/env python3
import sys

# Q4: Dans quelle ville Women's Clothing a généré le plus d'argent Cash
city_total = {}

for line in sys.stdin:
    city, amount = line.strip().split('\t', 1)
    amount = float(amount)
    city_total[city] = city_total.get(city, 0) + amount

# Vérifier s'il y a des résultats
if city_total:
    # Trouver la ville avec le montant le plus élevé
    max_city = max(city_total, key=city_total.get)
    print(f"{max_city}\t{city_total[max_city]:.2f}")
else:
    print("Aucune vente Women's Clothing en Cash trouvée")