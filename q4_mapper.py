#!/usr/bin/env python3
import sys

# Q4: Dans quelle ville Women's Clothing a généré le plus d'argent Cash
for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')
    if len(fields) >= 6:  # Vérifier que la ligne contient tous les champs
        category = fields[1]  # La catégorie est dans la 2e colonne (index 1)  
        product = fields[2]   # Le produit est dans la 3e colonne (index 2)
        city = fields[3]      # La ville est dans la 4e colonne (index 3)
        amount = float(fields[4])  # Le montant est dans la 5e colonne (index 4)
        payment_method = fields[5]  # Le moyen de paiement est dans la 6e colonne (index 5)
        
        # Filtrer pour Women's Clothing ET Cash
        if product == "Women's Clothing" and payment_method == "Cash":
            print(f"{city}\t{amount}")
