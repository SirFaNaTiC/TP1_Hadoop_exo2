#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')
    if len(fields) > 5:  # Assurez-vous que la ligne contient suffisamment de champs
        city = fields[3]  # Supposons que la ville est dans la 4e colonne
        payment_method = fields[5]  # Supposons que le moyen de paiement est dans la 6e colonne
        amount = float(fields[4])  # Supposons que le montant est dans la 5e colonne
        if city == "San Francisco":
            print(f"{payment_method}\t{amount}")