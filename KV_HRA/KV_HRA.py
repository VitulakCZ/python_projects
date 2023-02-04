import random

def uzhra_DEF():
    penize = 100000
    penize_za_kolo = 15000
    kolo = 1
    vojaci = 0
    cena_vojaka = 50

    while True:
        print(f"{kolo}. KOLO (výdělek za jedno kolo: {penize_za_kolo})")
        ahoj = input(f"Máš {penize} peněz a vlastníš {vojaci} vojáků. Co uděláš?\n\nV = koupit armádu\nI = investovat\nD = další kolo: ")
        if ahoj == "STOP":
            opustit_behem_hry = input("OPRAVDU? ANO = ano, NE = ne ")
            if opustit_behem_hry == "ANO":
                break
            elif opustit_behem_hry == "NE":
                print("MÁŠ ŠTĚSTÍ KAMARÁDE!\n\n")
            else:
                print("WHAT?\n")
        elif ahoj == "V":
            print(f"Momentálně vlastníte {vojaci} vojáků.")
            nakup_vojaku = input(f"Právě kupuješ vojáky. 1 voják je za {cena_vojaka} peněz. Kolik chceš vojáků? 1000, 1500, 2000, 2500, 3000, 5000: ")
            try:
                i = int(nakup_vojaku)
                if nakup_vojaku == "1000":
                    if penize >= 50000:
                        vojaci += 1000
                        penize -= 50000
                    else:
                        print("NEMÁTE DOSTATEK FINANCÍ!\n\n")
                elif nakup_vojaku == "1500":
                    if penize >= 75000:
                        vojaci += 1500
                        penize -= 75000
                    else:
                        print("NEMÁTE DOSTATEK FINANCÍ!\n\n")
                elif nakup_vojaku == "2000":
                    if penize >= 100000:
                        vojaci += 2000
                        penize -= 100000
                    else:
                        print("NEMÁTE DOSTATEK FINANCÍ!\n\n")
                elif nakup_vojaku == "2500":
                    if penize >= 125000:
                        vojaci += 2500
                        penize -= 125000
                    else:
                        print("NEMÁTE DOSTATEK FINANCÍ!\n\n")
                elif nakup_vojaku == "3000":
                    if penize >= 150000:
                        vojaci += 3000
                        penize -= 150000
                    else:
                        print("NEMÁTE DOSTATEK FINANCÍ!\n\n")
                elif nakup_vojaku == "5000":
                    if penize >= 250000:
                        vojaci += 250000
                        penize -= 250000
                    else:
                        print("NEMÁTE DOSTATEK FINANCÍ!\n\n")
                else:
                    print("TENTO POČET VOJÁKŮ NENÍ NA VÝBĚR!!\n\n")
            except ValueError:
                print("ČÍSLA!!!!\n\n")
        elif ahoj == "I":
            investice = input("Kolik chcete investovat peněz?\n10000 (zvýšení peněz za kolo o 750)\n20000 (zvýšení peněz za kolo o 1500)\n40000 (zvýšení peněz za kolo o 3000)\n80000 (zvýšení peněz za kolo o 6000) ")
            try:
                i = int(investice)
                if investice == "10000":
                    if penize >= 10000:
                        penize_za_kolo += 750
                        penize -= 10000
                    else:
                        print("NEMÁTE DOSTATEK FINANCÍ!\n\n")
                elif investice == "20000":
                    if penize >= 20000:
                        penize_za_kolo += 1500
                        penize -= 20000
                    else:
                        print("NEMÁTE DOSTATEK FINANCÍ!\n\n")
                elif investice == "40000":
                    if penize >= 40000:
                        penize_za_kolo += 3000
                        penize -= 40000
                    else:
                        print("NEMÁTE DOSTATEK FINANCÍ!\n\n")
                elif investice == "80000":
                    if penize >= 80000:
                        penize_za_kolo += 6000
                        penize -= 80000
                    else:
                        print("NEMÁTE DOSTATEK FINANCÍ!\n\n")
                else:
                    print("TENTO POČET VOJÁKŮ NENÍ NA VÝBĚR!!\n\n")
            except ValueError:
                print("ČÍSLA!!!!!!\n\n")
        elif ahoj == "D":
            penize += penize_za_kolo
            kolo += 1
        else:
            print("WHAT?\n")

def start_DEF():
    start = input("Vítej ve hře KV War Simulator. PLAY = začít hrát, OPT = nastavení, Q = Opustit hru. ")
    if start == "PLAY":
        warning_DEF()
    elif start == "OPT":
        opt_DEF()
    elif start == "Q":
        opustit = input("OPRAVDU? ANO = ano, NE = ne ")
        if opustit == "ANO":
            exit
        elif opustit == "NE":
            print("MÁŠ ŠTĚSTÍ!\n\n\n")
            start_DEF()
        else:
            print("WHAT?\n")
            start_DEF()
    else:
        print("WHAT?\n")
        start_DEF()

def warning_DEF():
    print("{0:*^50}".format("VAROVÁNÍ!"))
    OPT_POZOR = input("Teď ještě kontrola. Jestli si chcete zajít do nastavení, můžete napsat OPT. Ve hře můžete kdykoli napsat STOP pro ukončení hry. GO začne hru: ")
    if OPT_POZOR == "OPT":
        opt_DEF()
    elif OPT_POZOR == "GO":
        uzhra_DEF()
    elif OPT_POZOR == "STOP":
        war_opustit = input("OPRAVDU? ANO = ano, NE = ne ")
        if war_opustit == "ANO":
            exit
        elif war_opustit == "NE":
            print("MÁŠ ŠTĚSTÍ!\n\n\n")
            warning_DEF()
    else:
        print("WHAT?\n")
        warning_DEF()

def opt_DEF():
        print("NASTAVENÍ!")

start_DEF()