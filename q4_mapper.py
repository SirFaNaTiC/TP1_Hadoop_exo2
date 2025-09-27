#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')
    if len(fields) > 5:  # Assurez-vous que la ligne contient suffisamment de champs
        category = fields[2]  # Supposons que la catégorie est dans la 3e colonne
        city = fields[3]  # Supposons que la ville est dans la 4e colonne
        payment_method = fields[5]  # Supposons que le moyen de paiement est dans la 6e colonne
        amount = float(fields[4])  # Supposons que le montant est dans la 5e colonne
        if category == "Women’s Clothing" and payment_method == "Cash":
            print(f"{city}\t{amount}")