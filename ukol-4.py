# úkol 4

# Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:
#   Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
#   Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.

# Tvůj program bude obsahovat dvě funkce:
#   První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné 
#       (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, 
#       jinak vrátí hodnotu False. 
#   Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
# Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě 
# se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

# Tipy: 
# Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili.
# Pro kontrolu předvolby použijte slicing (viz první lekce) pro získání prvních 4 znaků řetězce. Ty porovnejte s řetězcem "+420".


tel_cislo = input("Zadejte telefonní číslo, kam chcete zprávu zaslat: ")

tel_cislo = str(tel_cislo)

len(tel_cislo) 

if len(tel_cislo) = 9:
    tel_cislo = True
    zprava = input("Prosím, zadejte zprávu: ")

elif len(tel_cislo) = 13:
    tel_cislo = True
    zprava = input("Prosím, zadejte zprávu: ")

else:
    tel_cislo = False 
    print("Zadané telefonní číslo není platné.")


delka_zpravy = len(zprava)/180

cena_zpravy = delka_zpravy * 3

print(f"Cena Vaší zprávy je {cena_zpravy} Kč. ")





