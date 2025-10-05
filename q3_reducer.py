#!/usr/bin/env python3
import sys

# Q3: Somme dépensée dans San Francisco avec chaque moyen de paiement
payment_total = {}

for line in sys.stdin:
    payment_method, amount = line.strip().split('\t', 1)
    amount = float(amount)
    payment_total[payment_method] = payment_total.get(payment_method, 0) + amount

# Afficher les résultats triés par moyen de paiement avec 2 décimales
for payment_method in sorted(payment_total.keys()):
    print(f"{payment_method}\t{payment_total[payment_method]:.2f}")