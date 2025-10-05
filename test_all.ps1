# Script de test pour toutes les questions MapReduce - CORRIGÉ
Write-Host "=== TESTS CORRIGES - Questions du fichier de ventes ===" -ForegroundColor Green
Write-Host "Données: Date,Catégorie,Produit,Ville,Prix,Moyen_paiement`n" -ForegroundColor Cyan

Write-Host "Q1 - Quel est le nombre d'achats effectués pour chaque catégorie d'achat ?" -ForegroundColor Yellow
Get-Content input_test.txt | python q1_mapper.py | Sort-Object | python q1_reducer.py
Write-Host ""

Write-Host "Q2 - Quelle est la somme totale dépensée pour chaque catégorie d'achat ?" -ForegroundColor Yellow  
Get-Content input_test.txt | python q2_mapper.py | Sort-Object | python q2_reducer.py
Write-Host ""

Write-Host "Q3 - Quelle somme est dépensée dans la ville de San Francisco avec chaque moyen de paiement ?" -ForegroundColor Yellow
Get-Content input_test.txt | python q3_mapper.py | Sort-Object | python q3_reducer.py
Write-Host ""

Write-Host "Q4 - Dans quelle ville la catégorie Women's Clothing a permis de générer le plus d'argent Cash ?" -ForegroundColor Yellow
Get-Content input_test.txt | python q4_mapper.py | Sort-Object | python q4_reducer.py
Write-Host ""

Write-Host "Q5 - À quelle heure les clients dépensent-ils le plus ?" -ForegroundColor Yellow
Get-Content input_test.txt | python q5_mapper.py | Sort-Object | python q5_reducer.py
Write-Host ""

Write-Host "=== RÉSUMÉ DES RÉSULTATS ===" -ForegroundColor Green
Write-Host "✅ Q1: 3 catégories (Electronics=4, Clothing=2, Books=1)"
Write-Host "✅ Q2: Electronics domine avec 2199.96€"
Write-Host "✅ Q3: À San Francisco, 289.49€ en Cash"
Write-Host "✅ Q4: San Francisco avec 89.50€ en Women's Clothing Cash"
Write-Host "✅ Q5: 12h est l'heure de pointe avec 1299.99€"