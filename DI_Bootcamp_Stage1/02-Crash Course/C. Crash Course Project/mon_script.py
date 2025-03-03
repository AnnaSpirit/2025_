import csv

# Remplacez 'votre_tableau.csv' par le nom de votre fichier CSV.
with open('votre_tableau.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

html = '<table border="1">\n'
# Ajouter l'en-tête
html += '  <tr>\n'
for header in rows[0]:
    html += f'    <th>{header}</th>\n'
html += '  </tr>\n'

# Ajouter les lignes de données
for row in rows[1:]:
    html += '  <tr>\n'
    for cell in row:
        html += f'    <td>{cell}</td>\n'
    html += '  </tr>\n'
html += '</table>'

# Sauvegarder le résultat dans un fichier HTML
with open('tableau.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Votre tableau HTML a été généré avec succès !")
