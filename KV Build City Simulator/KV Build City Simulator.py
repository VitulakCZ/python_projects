from pygame import mixer
mixer.init()

penize = 10000
kolo = 1
penize_za_kolo = None
elektrina = 0
domy = {}
panelaky = {}
obyvatele = 0
kapacita = None
odstehovani = 0

# Menu hry
while True:
    menu = input("Chceš hrát hru KV Build City Simulator? A = Ano, N = Ne: ").upper()
    if menu == "A":
        print("Doufáme, že se vám hra bude líbit :)")
        break
    elif menu == "N":
        exit()
    else:
        print("WHAT?\n")

# Hra
mixer.music.load("songa do pozadí.mp3")
mixer.music.play(-1)
click = mixer.Sound("nejlepsi_zvuk.mp3")
error = mixer.Sound("ERROR.mp3")
while True:
    # Relativní proměnné
    kapacita = len(domy) * 4 + len(panelaky) * 26
    penize_za_kolo = obyvatele * 180 - elektrina - 500

    print(domy)
    print(panelaky)
    vyber = input(f"{kolo}. KOLO!\nZákladní přehled:\n- Peníze: {penize}\n- Výdělek za kolo: {penize_za_kolo}\n- Obyvatel: {obyvatele}/{kapacita}\n- Domů: {len(domy)}\n- Paneláků: {len(panelaky)}\nK = Koupit budovy, O = Obyvatelé, E = Elektřina, D = Další kolo: ").upper()
    if vyber in ["K", "O", "E", "D"]: click.play()
    # Koupit budovy
    if vyber == "K":
        koupit_vyber = input("Co chcete koupit? D = Domy, P = Paneláky: ").upper()
        if koupit_vyber == "D":
            click.play()
            pocet_vyber = input("Kolik domů chcete koupit? 1 dům stojí 5000 peněz: ")
            try:
                pocet_vyber = int(pocet_vyber)
                if penize >= pocet_vyber * 5000:
                    click.play()
                    penize -= pocet_vyber * 5000
                    for dum in range(len(domy), pocet_vyber + len(domy)):
                        domy[dum + 1] = [0, False]
                else:
                    error.play()
                    print("NEMÁŠ DOSTATEK FINANCÍ!\n")
            except ValueError:
                error.play()
                print("Špatné zadání!\n")
        elif koupit_vyber == "P":
            click.play()
            pocet_vyber = input("Kolik paneláků chcete koupit? 1 panelák stojí 27500 peněz: ")
            try:
                pocet_vyber = int(pocet_vyber)
                if penize >= pocet_vyber * 27500:
                    click.play()
                    penize -= pocet_vyber * 27500
                    for panelak in range(len(panelaky), pocet_vyber + len(panelaky)):
                        panelaky[panelak + 1] = [0, False]
                else:
                    error.play()
                    print("NEMÁŠ DOSTATEK FINANCÍ!\n")
            except ValueError:
                error.play()
                print("Špatné zadání!\n")
        else:
            error.play()
            print("WHAT?\n")
    # Obyvatelé
    elif vyber == "O":
        kolik_obyvatel = input(f"Obyvatel: {obyvatele}/{kapacita}\nKolik chcete přistěhovat obyvatel? ")
        try:
            kolik_obyvatel = int(kolik_obyvatel)
            if kolik_obyvatel + obyvatele > kapacita:
                print("Jste za kapacitou!\n")
                error.play()
            elif penize < kolik_obyvatel * 50:
                print("NEMÁŠ DOSTATEK FINANCÍ!\n")
                error.play()
            else:
                click.play()
                penize -= kolik_obyvatel * 50
                obyvatele += kolik_obyvatel
                print(f"Obyvatel zakoupeno: {kolik_obyvatel}")
                for dum in domy:
                    vypocet_elektriny = domy.get(dum)[1]
                    while domy.get(dum)[0] < 4 and kolik_obyvatel > 0:
                        domy.get(dum)[0] += 1
                        kolik_obyvatel -= 1
                for panelak in panelaky:
                    while panelaky.get(panelak)[0] < 26 and kolik_obyvatel > 0:
                        panelaky.get(panelak)[0] += 1
                        kolik_obyvatel -= 1
        except ValueError:
            error.play()
            print("Špatné zadání!\n")
    # Elektřina
    elif vyber == "E":
        elektrina_vyber = input("Jste si jisti? A/N: ").upper()
        if elektrina_vyber == "A":
            vypocet_elektriny = 0
            for dum in domy:
                if not domy.get(dum)[1]:
                    vypocet_elektriny += 120
            for panelak in panelaky:
                if not panelaky.get(panelak)[1]:
                    vypocet_elektriny += 750
            if vypocet_elektriny == 0:
                error.play()
                print("Nemáš ještě ani jednu stavbu!\n")
            elif penize < vypocet_elektriny:
                error.play()
                print("NEMÁŠ DOSTATEK FINANCÍ!\n")
            else:
                click.play()
                penize -= vypocet_elektriny
                elektrina += vypocet_elektriny
                for dum in domy:
                    domy.get(dum)[1] = True
                for panelak in panelaky:
                    panelaky.get(panelak)[1] = True
                print("Úspěšně navedena elektřina do vašich budov!\n")
        elif elektrina_vyber == "N":
            click.play()
            print("OK!\n")
        else:
            error.play()
    # Další kolo
    elif vyber == "D":
        kolo += 1
        odstehovat = False
        kolo_odstehovani = 0
        for dum in domy:
            if not domy.get(dum)[1]:
                ted_odstehovani = 0
                odstehovani += domy.get(dum)[0]
                kolo_odstehovani += domy.get(dum)[0]
                ted_odstehovani += domy.get(dum)[0]
                obyvatele -= ted_odstehovani
                if domy.get(dum)[0] > 0:
                    odstehovat = True
                domy.get(dum)[0] = 0
        for panelak in panelaky:
            if not panelaky.get(panelak)[1]:
                ted_odstehovani = 0
                odstehovani += panelaky.get(panelak)[0]
                kolo_odstehovani += panelaky.get(panelak)[0]
                ted_odstehovani += panelaky.get(panelak)[0]
                obyvatele -= ted_odstehovani
                if panelaky.get(panelak)[0] > 0:
                    odstehovat = True
                panelaky.get(panelak)[0] = 0
        if odstehovat:
            print(f"Nějací lidé se odstěhovali z vašeho města kvůli nedodané elektřině!\nPočet lidí: {kolo_odstehovani}")
        penize_za_kolo = obyvatele * 180 - elektrina - 500
        penize += penize_za_kolo
    else:
        error.play()
        print("WHAT?\n")
