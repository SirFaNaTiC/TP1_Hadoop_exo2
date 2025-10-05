#!/usr/bin/env python3
import sys

# Q1: Nombre d'achats effectués pour chaque catégorie
for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')
    if len(fields) >= 6:  # Vérifier que la ligne contient tous les champs
        category = fields[1]  # La catégorie est dans la 2e colonne (index 1)
        print(f"{category}\t1")