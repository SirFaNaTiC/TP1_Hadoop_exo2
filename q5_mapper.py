#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')
    if len(fields) > 4:  # Assurez-vous que la ligne contient suffisamment de champs
        time = fields[1].split(':')[0]  # Supposons que l’heure est dans la 2e colonne (format HH:MM:SS)
        amount = float(fields[4])  # Supposons que le montant est dans la 5e colonne
        print(f"{time}\t{amount}")