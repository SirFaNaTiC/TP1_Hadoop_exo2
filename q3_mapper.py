#!/usr/bin/env python3
import sys

# Q3: Somme dépensée dans San Francisco avec chaque moyen de paiement
for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')
    if len(fields) >= 6:  # Vérifier que la ligne contient tous les champs
        city = fields[3]  # La ville est dans la 4e colonne (index 3)
        payment_method = fields[5]  # Le moyen de paiement est dans la 6e colonne (index 5)
        amount = float(fields[4])  # Le montant est dans la 5e colonne (index 4)
        if city == "San Francisco":
            print(f"{payment_method}\t{amount}")