# úkol 2

# Vyvíjíš software pro obchod s elektronickými součástkami. Firma eviduje informace o počtu součástek na skladě ve slovníku. 
# Klíč slovníku je kód součástky a hodnota klíče je počet součástek na skladě.

# Napiš software, který bude využívat prodavač v případě, že do obchodu přijde zákazník. Software se nejprve zeptá na kód součástky 
# a poté na množství, které si zákazník chce koupit. Obě informace si ulož. Následně naprogramuj následující varianty:
#    a) Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.
#    b) Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom, že lze prodat pouze omezené množství kusů. 
#       Následně součástku odeber ze slovníku, protože je vyprodaná.
#    c) Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši, a sniž počet součástek 
#       na skladě o množství požadované zákazníkem.


sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}


kod_soucastky = input(f"Zadejte kód součastky, kterou si chcete koupit. ")

if kod_soucastky in sklad:
    pocet_soucastek = int(input(f"Kolik si přejete koupit kusů? "))

    if pocet_soucastek >= 
        print(f"Vaši poptávku můžeme uspokojit v plné výši.")

    elif pocet_soucastek < 
        print(f"Omlouváme se, můžeme Vám nabídnout pouze omezené množství kusů, které je { }.")


else: 
    print(f"Omlouváme se, tato součástka není skladem.")