#!/usr/bin/env python3
import sys

# Q5: À quelle heure les clients dépensent-ils le plus ?
hour_total = {}

for line in sys.stdin:
    hour, amount = line.strip().split('\t', 1)
    amount = float(amount)
    hour_total[hour] = hour_total.get(hour, 0) + amount

# Trouver l'heure avec le montant le plus élevé
if hour_total:
    max_hour = max(hour_total, key=hour_total.get)
    print(f"Heure avec le plus de dépenses: {max_hour}h - Total: {hour_total[max_hour]:.2f}€")
    print("\nDétail par heure:")
    for hour in sorted(hour_total.keys()):
        print(f"{hour}h\t{hour_total[hour]:.2f}")
else:
    print("Aucune donnée trouvée")