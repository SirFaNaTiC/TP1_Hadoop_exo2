#!/usr/bin/env python3
import sys

# Q5: À quelle heure les clients dépensent-ils le plus ?
for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')
    if len(fields) >= 6:  # Vérifier que la ligne contient tous les champs
        datetime = fields[0]  # La date/heure est dans la 1ère colonne (index 0)
        # Extraire l'heure de "2023-01-01 10:30:00"
        time_part = datetime.split(' ')[1]  # "10:30:00"
        hour = time_part.split(':')[0]      # "10"
        amount = float(fields[4])  # Le montant est dans la 5e colonne (index 4)
        print(f"{hour}\t{amount}")
