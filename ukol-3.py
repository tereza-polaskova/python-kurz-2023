# úkol 3

# Soubor body.json je JSON, který obsahuje informace o získaných bodech z písemky. 
# Soubor si ulož a načti do slovníku.
# Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). Vytvoř nový slovník. Jeho klíče budou opět jména žáků, 
#   a hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň než 60 bodů. Pokud má méně než 60, hodnota bude "Fail".
# Výsledný slovník ulož jako JSON do souboru prospech.json.


import json

with open('body.json', encoding='utf-8') as treti_ukol:
    data = treti_ukol.read()

print(data)

znamka = input(data)
    if znamka >= 60:
        znamka = ["Pass"]
    else:
        znamka = ["Fail"]



with open('body.json', mode='w', encoding='utf-8') as prospech:
    json.dump(znamka, prospech)
    data2 = prospech.read()

print(prospech)

