#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')
    if len(fields) > 4:  # Assurez-vous que la ligne contient suffisamment de champs
        category = fields[2]  # Supposons que la catégorie est dans la 3e colonne
        amount = float(fields[4])  # Supposons que le montant est dans la 5e colonne
        print(f"{category}\t{amount}")