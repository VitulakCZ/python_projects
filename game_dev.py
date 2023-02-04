import random

penize = 2200
pocet_her_na_kterych_se_pracuje = 0
hry_na_kterych_se_pracuje = {}
zanr_her_na_kterych_se_pracuje = {}
# Odečítat
najem = 320
vyplaty = 0
# Přičítat
penize_z_her = 0

level = 1
zanry = ["Závodní", "Bojová", "Střílečka", "Role Playing Game", "Strategie", "Arkáda", "Adventura"]
zacatecni_zanr = random.choice(zanry)
zacatecni_zanr_2 = random.choice(zanry)
while zacatecni_zanr == zacatecni_zanr_2:
    zacatecni_zanr_2 = random.choice(zanry)
odemknute_zanry = [zacatecni_zanr, zacatecni_zanr_2]
pocet_her = 0
hry = {}
pocet_zamestnancu = 0
zamestnanci = []
rok = 2021
mesic = 1

while True:
    menu = input("""\
------------------------------
KV GAME DEVELOPMENT SIMULATOR!
------------------------------
PLAY = Hrát hru
OPT = Nastavení
Q = Quit: """).upper()
    if menu == "PLAY":
        jmeno = input("Vyber si jméno tvé postavy: ").title()
        jmeno_firmy = input("Vyber si jméno tvé firmy: ")
        while True:
            for hra_na_ktere_se_pracuje in hry_na_kterych_se_pracuje:
                if hry_na_kterych_se_pracuje.get(hra_na_ktere_se_pracuje) <= 0:
                    print(f"Hra {hra_na_ktere_se_pracuje} byla úspěšně dokončena!")
                    penize_z_her += 200
                    hry[hra_na_ktere_se_pracuje] = zanr_her_na_kterych_se_pracuje.get(hra_na_ktere_se_pracuje)
                    hry_na_kterych_se_pracuje.pop(hra_na_ktere_se_pracuje)
                    pocet_her_na_kterych_se_pracuje -= 1
                    break
            penize_za_mesic = 0 + penize_z_her - najem - vyplaty
            if penize < 0:
                print("PROHRÁL JSI!")
                exit()
            zaklad = input(f"\nZákladní Přehled:\n- {mesic}. MĚSÍC\n- ROK {rok}\n- Tvůj level: {level}\n- Peněz: {penize} $\n- Výdělek za měsíc: {penize_za_mesic} $\n- Zaměstnanců: {pocet_zamestnancu}\nAkce:\nV = Vytvořit, F = Finance, H = Hry vaší společnosti, N = Najmout zaměstnance, R = Vyzkoumat, D = Další Kolo, Q = Ukončit hru: ").upper()
            if zaklad == "V":
                if pocet_her_na_kterych_se_pracuje > pocet_zamestnancu:
                    print("Nemáš dostatek zaměstnanců, aby jsi mohl vytvářet více věcí najednou!")
                else:
                    vytvorit = input("Co chceš vytvořit?\nH = Hru\nE = Engine: ").upper()
                    if vytvorit == "H":
                        naklady = 0
                        jmeno_hry = input("Jméno hry: ")
                        if jmeno_hry not in hry:
                            while True:
                                for odemknuty_zanr in odemknute_zanry:
                                    if odemknuty_zanr == odemknute_zanry[0]:
                                        print("Jaký žánr? Můžeš použít žánry " + odemknuty_zanr, end=", ")
                                    elif odemknuty_zanr != odemknute_zanry[0] and odemknuty_zanr != odemknute_zanry[-1]:
                                        print(odemknuty_zanr, end=", ")
                                    else:
                                        print(odemknuty_zanr, end=": ")
                                zanr_hry = input().title()
                                if zanr_hry in odemknute_zanry:
                                    naklady += 250
                                    if penize >= naklady:
                                        pocet_her_na_kterych_se_pracuje += 1
                                        hry_na_kterych_se_pracuje[jmeno_hry] = 3
                                        zanr_her_na_kterych_se_pracuje[jmeno_hry] = zanr_hry
                                        print(f"Na hře {jmeno_hry} se začalo úspěšně pracovat, bude trvat 3 kola, než se dokončí. Náklady: {naklady} $")
                                        break
                                else:
                                    print("TENTO ŽÁNR NENÍ NA VÝBĚR!\n")
                        else:
                            print("Takovou hru už jsi dělal!")
                    else:
                        print("WHAT?")
            elif zaklad == "F":
                while True:
                    finance = input(f"\nINFORMACE O PENĚZÍCH:\nPříjmy:\n- Z her: {penize_z_her} $\nPoplatky:\n- Nájem: {najem} $\n- Výplaty: {vyplaty} $\nENTER pro pokračování: ")
                    if finance == "":
                        break
                    else:
                        pass
            elif zaklad == "H":
                while True:
                    if hry != {}:
                        print(f"VŠECHNY HRY FIRMY {jmeno_firmy}:")
                        for hra in hry:
                            print(f"Hra: {hra} | {hry.get(hra)}")
                    else:
                        print(f"Firma {jmeno_firmy} zatím ještě nevydala žádnou hru...")
                    moje_hry = input("\nENTER pro pokračování: ")
                    if moje_hry == "":
                        break
                    else:
                        pass
            elif zaklad == "N":
                print("MIMO PROVOZ!")
            elif zaklad == "R":
                print("MIMO PROVOZ!")
            elif zaklad == "D":
                if mesic >= 12:
                    mesic = 1
                    rok += 1
                else:
                    mesic += 1
                penize += penize_za_mesic
                for hra_na_ktere_se_pracuje in hry_na_kterych_se_pracuje:
                    hry_na_kterych_se_pracuje[hra_na_ktere_se_pracuje] -= 1
            elif zaklad == "Q":
                exit()
            else:
                print("WHAT?\n")
    elif menu == "OPT":
        print("NASTAVENÍ!\n")
    elif menu == "Q":
        exit()
    else:
        print("WHAT?\n")