# úkol 3

# Soubor body.json je JSON, který obsahuje informace o získaných bodech z písemky. 
# Soubor si ulož a načti do slovníku.
# Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). Vytvoř nový slovník. Jeho klíče budou opět jména žáků, 
#   a hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň než 60 bodů. Pokud má méně než 60, hodnota bude "Fail".
# Výsledný slovník ulož jako JSON do souboru prospech.json.


import json

with open('body.json', encoding='utf-8') as treti_ukol:
    data = json.loads(treti_ukol.read()

print(data)

znamka = input(json.loads(data))
for student in data:
    if znamka in treti_ukol >= 60:
        hodnoceni = ["Pass"]
    else:
        hodnoceni = ["Fail"]


with open('body.json', mode='w', encoding='utf-8') as prospech:
   json.dump(hodnoceni, prospech)
   data2 = prospech.read()

seznam_prospech = json.loads(data2)
print(data2[0])
