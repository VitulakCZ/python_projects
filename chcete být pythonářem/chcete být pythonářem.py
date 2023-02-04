import time
import random
from pygame import mixer
from colorama import init, Fore
from itertools import count

mixer.init()
init()
otazky = {
     1: [
        {"Co je pravda o programu:\n\nprint(\"Hello, world!\")": {"a) Čeká na input člověka. Pokud napíše \"Hello, world!\", program odpoví": False, "b) Napíše \"Hello, world!\"": True, "c) Program vyhodí ValueError": False, "d) Program zavře všechna otevřená okna": False}},
        {"Co je pravda o programu:\n\nstring = input(\"Jak se jmenuješ: \")\nprint(f\"Jméno: {string}\")": {"a) Čeká na input člověka, potom napíše \"Jméno: {string}\"": True, "b) Napíše náhodné jméno": False, "c) Čeká na input člověka, pokud napíše číslo, program skončí": False, "d) Čeká na input sluchátek, poté pomocí odposlouchávání zjistí vaše jméno": False}}
    ],
     2: [
        {"Co je pravda o programu:\n\nx = 30\ny = 10\nprint(x - y * 3)": {"a) Napíše 20": False, "b) Napíše False": False, "c) Napíše 0": True, "d) Napíše 60": False}},
        {"Co je pravda o programu:\n\npenize = 0\ndef pridat(penize, kolik):\n    penize += kolik\n    return penize\nfor i in range(1, 6):\n    penize = pridat(penize, 100 * i)\n    print(penize)": {"a) Napíše 100\\n400\\n800\\n1000\n1500": False, "b) Napíše 200\\n600\\n1200\\n2000\\n3000": False, "c) Napíše \"100 100\"\\n\"200 200\"\\n\"600 600\"\\n\"1500 1500\"\\n\"2500 2500\"": False, "d) Napíše \"100\\n300\\n600\\n1000\\n1500\"": True}}
    ],
     3: [
        {"Co je pravda o programu:\n\ntry:\n    odpoved = int(input(\"Napiš mi jakékoli číslo: \"))\n    print(f\"Řekl jsi mi číslo {odpoved}!\")\nexcept ValueError:\n    print(\"Toto není číslo!\")": {"a) Napíše \"Řekl jsi mi číslo {odpoved}!\" pokud člověk napsal int, pokud ne, napíše \"Toto není číslo!\"": True, "b) Napíše \"Toto není číslo!\"": False, "c) Vyhodí ValueError, pokud člověk nenapíše int": False, "d) Napíše \"Toto není číslo\", pokud člověk napsal int": False}},
        {"Co je pravda o programu:\n\nlist = [\"zaparkovat\", \"p\", \"u\", \"ukrást\", \"ukrást kreditku\", \"h\", \"hrát\", \"hrát hru\"]\nvec = input(\"Co chcete udělat? Za(p)arkovat, (U)krást kreditku, (H)rát hru: \").lower()\nif vec in list:\n    print(\"Správná akce.\")\nelse:\n    print(\"ŠPATNĚ!\")": {"a) Pokud člověk napsal \"list\", napíše \"Správná akce.\", pokud ne, \"ŠPATNĚ!\"": False, "b) Pokud člověk napsal všechny věci z listu, napíše \"Správná akce.\", pokud ne, \"ŠPATNĚ!\"": False, "c) Pokud člověk stiskl jakoukoli klávesu z listu list, okamžitě napíše \"Správná akce.\", pokud ne, \"ŠPATNĚ!\"": False, "d) Pokud to, co člověk napsal, je v listu list, napíše \"Správná akce.\", pokud ne, \"ŠPATNĚ!\"": True}}
    ],
     4: [
        {"Co je pravda o programu:\n\njmeno = \"Krypl\"\nif jmeno == \"Krypl\":\n    print(\"HROZNĚ VTIPNÉ!\")\nprint(f\"Vítám Tě, {jmeno}!\")": {"a) Napíše \"Vítám Tě, {jmeno}!\"": False, "b) Napíše \"HROZNĚ VTIPNÉ!\"": False, "c) Napíše \"HROZNĚ VTIPNÉ!\" i \"Vítám Tě, {jmeno}!\"": True, "d) Napíše \"Krypl\" i \"HROZNĚ VTIPNÉ!\"": False}},
        {"Co je pravda o programu:\n\nlist_veci = [\"Bazén\", \"Počítač\", \"Klávesnice\", \"Nabíječka\", \"Cihla\"]\nif (x := len(list_veci)) == 5:\n    print(x)": {"a) Napíše True": False, "b) Napíše 5": True, "c) Nic se nestane": False, "d) Napíše \"Cihla\"": False}}
    ],
     5: [
        {"Co je pravda o programu:\n\nlimit = 10\nwhile limit > 0:\n    print(\"AHOJ!\")\n    limit -= 1\nprint(\"JOOOO!\")": {"a) Napíše \"JOOOO!\" po 10 sekundách": False, "b) Napíše \"AHOJ!\" a \"JOOOO!\" 10krát": False, "c) Napíše \"AHOJ!\" 10krát a potom jednou \"JOOOO!\", to se opakuje nekonečnokrát": False, "d) Napíše \"AHOJ!\" 10krát a potom jednou \"JOOOO!\"": True}},
        {"Co je pravda o programu:\n\nlist_veci = [\"Bazén\", \"Počítač\", \"Klávesnice\", \"Nabíječka\", \"Cihla\"]\nif x := len(list_veci) == 5:\n    print(x)": {"a) Napíše True": True, "b) Napíše 5": False, "c) Napíše \"Bazén\"\\n\"Počítač\"\\n\"Klávesnice\"\\n\"Nabíječka\"\\n\"Cihla\"": False, "d) Napíše \"Cihla\"": False}}
    ],
     6: [
        {"Co je pravda o programu:\n\nlide = [None, \"Dvořák\", \"Mladý\", \"Poslední\"]\nfor index, clovek in enumerate(lide):\n    if index == 0:\n        continue\n    print(f\"{index}. {clovek}\")": {"a) Napíše všechny lidi takto: \"Dvořák\"\\n\"Mladý\"\\n\"Poslední\"": False, "b) Napíše všechny lidi takto: 0\\n\"Dvořák\"\\n\"Mladý\"\\n\"Poslední\"": False, "c) Napíše všechny lidi takto: \"1. Dvořák\"\\n\"2. Mladý\"\\n\"3. Poslední\"": True, "d) Napíše všechny lidi takto: \"0. None\"\\n\"1. Dvořák\"\\n\"2. Mladý\"\\n\"3. Poslední\"": False}},
        {"Co je pravda o programu:\n\nimport math\nx = 9\nprint(min(min(math.sqrt(x), 5) + max(math.sqrt(x), 5) ** 2, 30))": {"a) Napíše 28.0": True, "b) Napíše 30": False, "c) Napíše 20": False, "d) Napíše 3": False}}
     ],
     7: [
        {"Co je pravda o programu:\n\njidlo_cena = {\"Rohlík\": 2, \"Chleba\": 45, \"Rýže\": 30, \"Kuře\": 45}\nfor jidlo in jidlo_cena:\n    print(jidlo, jidlo_cena.get(jidlo))": {"a) Napíše všechno jídlo takto: \"Rohlík 2\"\\n\"Chleba 45\"\\n\"Rýže 30\"\\n\"Kuře 45\"": True, "b) Napíše všechno jídlo takto: \"Rohlík, 2\"\\n\"Chleba, 45\"\\n\"Rýže, 30\"\\n\"Kuře, 45\"": False, "c) Napíše všechno jídlo takto: \"2 Rohlík\"\\n\"45 Chleba\"\\n\"30 Rýže\"\\n\"45 Kuře\"": False, "d) Napíše všechno jídlo takto: \"Rohlík2\"\\n\"Chleba45\"\\n\"Rýže30\"\\n\"Kuře45\"": False}},
        {"Co je pravda o programu:\n\nimport random\nhry = {\n    \"New Studio\": [1989],\n    \"Agent\": [1995, 2011, 2013, 2019],\n    \"Blastoff\": [1999, 2004, 2021]\n}\nhra = random.choice(list(hry))\nprint(str(hry.get(hra)).replace(\"[\", \"\").replace(\", \", \"\\n\").replace(\"]\", \"\"))": {"a) Pokud je hra \"Blastoff\" napíše 1999": False, "b) Pokud je hra \"Agent\" napíše 1995\\n2011\\n2013\\n2019": True, "c) Napíše 1989\\n1995\\n1999\\n2004\\n2011\\n2013\\n2019\\n2021": False, "d) Pokud je hra 1999 napíše \"Blastoff\"": False}}
    ],
     8: [
        {"Co je pravda o programu:\n\ncislo = 0\nlst = [10, 90, 100, 900, 1000]\ndef zmenit_cislo(plus):\n    global cislo\n    for i in range(151):\n        cislo = i\n    for index in lst:\n        cislo += index\n    cislo += plus\n\nzmenit_cislo(250)\nprint(cislo)": {"a) Napíše číslo 151": False, "b) Napíše číslo 2500": True, "c) Napíše číslo 2501": False, "d) Napíše číslo 250": False}},
        {"Co je pravda o programu:\n\ncislo = 0\nlst = [10, 90, 100, 900, 1000]\ndef zmenit_cislo(plus):\n    global cislo\n    for i in range(151):\n        cislo = i\n    for index in lst:\n        cislo += index\n    cislo += plus\n\nzmenit_cislo(250)\nprint(cislo)": {"a) Napíše číslo 151": False, "b) Napíše číslo 2500": True, "c) Napíše číslo 2501": False, "d) Napíše číslo 250": False}}
    ],
     9: [
        {"Co je pravda o programu:\n\ncislo = 0\ndef zmenit_cislo(plus):\n    cislo += plus\nzmenit_cislo(10)\nprint(cislo)": {"a) Vyhodí UnboundLocalError": True, "b) Napíše číslo 10": False, "c) Napíše číslo 11": False, "d) Napíše číslo -10": False}},
        {"Co je pravda o programu:\n\ncislo = 0\ndef zmenit_cislo(plus):\n    cislo += plus\nzmenit_cislo(10)\nprint(cislo)": {"a) Vyhodí UnboundLocalError": True, "b) Napíše číslo 10": False, "c) Napíše číslo 11": False, "d) Napíše číslo -10": False}}
    ],
    10: [
        {"Od jaké python verze je možné tento program spustit:\n\nx = 0\nmatch x:\n    case 0:\n    print(\"Hello, world!\")\n    case _:\n    print(\"x != 0!\")": {"a) 3.5.5": False, "b) 3.7": False, "c) 3.11.0b1": False, "d) 3.10": True}},
        {"Od jaké python verze je možné tento program spustit:\n\nx = 0\nmatch x:\n    case 0:\n        print(\"Hello, world!\")\n    case _:\n        print(\"x != 0!\")": {"a) 3.5.5": False, "b) 3.7": False, "c) 3.11.0b1": False, "d) 3.10": True}}
    ],
    11: [
        {"Co je pravda o programu:\n\nimport random\nveci = [\"Mobil\", \"Taška\", \"Ulita\", \"Počítač\"]\nrandom_veci = []\nfor _ in range(len(veci)):\n    random_veci.append(random.choice(veci))\nif random_veci[0] == random_veci[1] == random_veci[2] == random_veci[3]:\n    print(f\"JACKPOT!\")\nelse:\n    print(\"Padlo Ti: \", end=\"\")\n    for random_vec in random_veci:\n        print(random_vec, end=\", \")\n    print(\"to je vše!\")": {"a) Do listu random_veci se přidají 4 věci z listu veci, pokud se věci nerovnají, napíše \"JACKPOT!\"": False, "b) Do listu random_veci se přidá jedna věc, pokud se rovná Tašce, napíše \"JACKPOT!\"": False, "c) Pokud se jackpot rovná Tašce, napíše \"JACKPOT!\"": False, "d) Do listu random_veci se přidají 4 věci z listu veci, pokud se věci rovnají, napíše \"JACKPOT!\"": True}},
        {"Co je pravda o programu:\n\nimport random\nveci = [\"Mobil\", \"Taška\", \"Ulita\", \"Počítač\"]\nrandom_veci = []\nfor _ in range(len(veci)):\n    random_veci.append(random.choice(veci))\nif random_veci[0] == random_veci[1] == random_veci[2] == random_veci[3]:\n    print(f\"JACKPOT!\")\nelse:\n    print(\"Padlo Ti: \", end=\"\")\n    for random_vec in random_veci:\n        print(random_vec, end=\", \")\n    print(\"to je vše!\")": {"a) Do listu random_veci se přidají 4 věci z listu veci, pokud se věci nerovnají, napíše \"JACKPOT!\"": False, "b) Do listu random_veci se přidá jedna věc, pokud se rovná Tašce, napíše \"JACKPOT!\"": False, "c) Pokud se jackpot rovná Tašce, napíše \"JACKPOT!\"": False, "d) Do listu random_veci se přidají 4 věci z listu veci, pokud se věci rovnají, napíše \"JACKPOT!\"": True}}
    ],
    12: [
        {"Co je pravda o programu:\n\nimport time\nsekundy = 0\nwhile True:\n    time.sleep(0.1)\n    sekundy += 0.1\n    print(\"{:.1f} sekund!\".format(sekundy))": {"a) Každou desetinu sekundy program napíše [format(sekundy // (60 * 60)), sekundy]": False, "b) Každou sekundu napíše, kolik sekund.desetin (např. 2.0) program běží": False, "c) Každou milisekundu napíše kolik milisekund program běží": False, "d) Každou desetinu sekundy napíše kolik sekund.desetin (např. 2.6) program běží": True}},
        {"Co je pravda o programu:\n\nimport time\nsekundy = 0\nwhile True:\n    time.sleep(0.1)\n    sekundy += 0.1\n    print(\"{:.1f} sekund!\".format(sekundy))": {"a) Každou desetinu sekundy program napíše [format(sekundy // (60 * 60)), sekundy]": False, "b) Každou sekundu napíše, kolik sekund.desetin (např. 2.0) program běží": False, "c) Každou milisekundu napíše kolik milisekund program běží": False, "d) Každou desetinu sekundy napíše kolik sekund.desetin (např. 2.6) program běží": True}}    
    ],
    13: [
        {"Co je pravda o programu:\n\nimport random\nimport time\n\nkrat = lambda x, y: x * y\nwhile True:\n    print(krat(random.randint(10, 100), random.randint(10, 100)))\n    time.sleep(0.5)": {"a) Každou půlsekundu napíše 10 * 10": False, "b) Vyhodí UnsupportedError, unsupported expression: lambda": False, "c) Každých 500 milisekund napíše náhodné číslo * náhodné číslo, maximum je 10000": True, "d) Každých pět desetin sekundy napíše náhodné číslo // náhodné číslo, nesmí se dostat pod nulu": False}},
        {"Co je pravda o programu:\n\nimport random\nimport time\n\nkrat = lambda x, y: x * y\nwhile True:\n    print(krat(random.randint(10, 100), random.randint(10, 100)))\n    time.sleep(0.5)": {"a) Každou půlsekundu napíše 10 * 10": False, "b) Vyhodí UnsupportedError, unsupported expression: lambda": False, "c) Každých 500 milisekund napíše náhodné číslo * náhodné číslo, maximum je 10000": True, "d) Každých pět desetin sekundy napíše náhodné číslo // náhodné číslo, nesmí se dostat pod nulu": False}}
    ],
    14: [
        {"Co je pravda o programu:\n\nlist_cisel = []\nwhile True:\n    try:\n        cislo = input(\"Zadej číslo, nebo l = list čísel: \")\n        if cislo == \"l\":\n            if list_cisel != []:\n                for l_cislo in list_cisel:\n                    print(str(l_cislo) + \" zajímavé\" if l_cislo % 2 == 0 else str(l_cislo) + \" nezajímavé\")\n            else:\n                print(\"Prázdný list!\")\n        else:\n            list_cisel.append(int(cislo))\n    except ValueError:\n        print(\"Nezadal jsi číslo!\")": {"a) Po člověku chceme číslo, pokud číslo nenapsal, napíše mu to list čísel, když je číslo liché, napíše se \"nezajímavé\"": False, "b) Vyhodí PrintIfsError, can't have if in a function": False, "c) Po člověku chceme číslo, to se uloží do listu, když člověk dá \"l\", když je sudé k napíše se k němu \"zajímavé\"": True, "d) Po člověku chceme číslo, pokud napíše \"l\", zobrazí se mu čísla takto: [1, \"nezajímavé\", 2, \"zajímavé\"] atd...": False}},
        {"Co je pravda o programu:\n\nlist_cisel = []\nwhile True:\n    try:\n        cislo = input(\"Zadej číslo, nebo l = list čísel: \")\n        if cislo == \"l\":\n            if list_cisel != []:\n                for l_cislo in list_cisel:\n                    print(str(l_cislo) + \" zajímavé\" if l_cislo % 2 == 0 else str(l_cislo) + \" nezajímavé\")\n            else:\n                print(\"Prázdný list!\")\n        else:\n            list_cisel.append(int(cislo))\n    except ValueError:\n        print(\"Nezadal jsi číslo!\")": {"a) Po člověku chceme číslo, pokud číslo nenapsal, napíše mu to list čísel, když je číslo liché, napíše se \"nezajímavé\"": False, "b) Vyhodí PrintIfsError, can't have if in a function": False, "c) Po člověku chceme číslo, to se uloží do listu, když člověk dá \"l\", když je sudé k napíše se k němu \"zajímavé\"": True, "d) Po člověku chceme číslo, pokud napíše \"l\", zobrazí se mu čísla takto: [1, \"nezajímavé\", 2, \"zajímavé\"] atd...": False}}
    ],
    15: [
        {"Co je pravda o programu:\n\nslovnik = {\"Ahoj\": {\"en\": \"Hello\", \"de\": \"Hallo\"},\n           \"Kniha\": {\"en\": \"Book\", \"de\": \"Buch\"},\n           \"Auto\": {\"en\": \"Car\", \"de\": \"Auto\"}}\nfor slovicka in slovnik:\n    print(slovicka + \",\", list(slovnik.get(slovicka).keys())[0],\n          \"=\", list(slovnik.get(slovicka).values())[0] + \",\", list(slovnik.get(slovicka).keys())[1], \"=\",\n          list(slovnik.get(slovicka).values())[1])": {"a) Napíše \"Ahoj,Hello = Hallo\\nKniha,Book = Buch\\nAuto,Car = Auto\"": False, "b) Napíše \"Ahoj, Hello, Hallo\\nKniha, Book, Buch\\nAuto, Car, Auto\"": False, "c) Napíše \"Ahoj = Hello = Hallo\\nKniha = Book = Buch\\nAuto = Car = Auto\"": False, "d) Napíše \"Ahoj, en = Hello, de = Hallo\\nKniha, en = Book, de = Buch\\nAuto, en = Car, de = Auto\"": True}},
        {"Co je pravda o programu:\n\nslovnik = {\"Ahoj\": {\"en\": \"Hello\", \"de\": \"Hallo\"},\n           \"Kniha\": {\"en\": \"Book\", \"de\": \"Buch\"},\n           \"Auto\": {\"en\": \"Car\", \"de\": \"Auto\"}}\nfor slovicka in slovnik:\n    print(slovicka + \",\", list(slovnik.get(slovicka).keys())[0],\n          \"=\", list(slovnik.get(slovicka).values())[0] + \",\", list(slovnik.get(slovicka).keys())[1], \"=\",\n          list(slovnik.get(slovicka).values())[1])": {"a) Napíše \"Ahoj,Hello = Hallo\\nKniha,Book = Buch\\nAuto,Car = Auto\"": False, "b) Napíše \"Ahoj, Hello, Hallo\\nKniha, Book, Buch\\nAuto, Car, Auto\"": False, "c) Napíše \"Ahoj = Hello = Hallo\\nKniha = Book = Buch\\nAuto = Car = Auto\"": False, "d) Napíše \"Ahoj, en = Hello, de = Hallo\\nKniha, en = Book, de = Buch\\nAuto, en = Car, de = Auto\"": True}}
    ]
}

# Intro
#mixer.music.load("chcete být pythonářem znělka.mp3")
#mixer.music.play()
#time.sleep(1.3)
#print("KV uvádí...")
#time.sleep(3.3)
#print("Chcete Být Pythonářem!")
#time.sleep(3.3)
#print(f"{Fore.LIGHTBLACK_EX}Speciální poděkování firmě {Fore.RED}Sony Pictures Television{Fore.LIGHTBLACK_EX} za poskytnutí licence {Fore.RED}WHO WANTS TO BE A MILLIONAIRE?{Fore.RESET}")
#time.sleep(1.6)
#print(f"{Fore.LIGHTBLACK_EX}Hra vytvořena v programovacím jazyku {Fore.RED}Python 3.10.0 64-bit{Fore.RESET}")
#time.sleep(0.9)
#print(f"{Fore.LIGHTBLACK_EX}© 2022 VŠECHNA PRÁVA VYHRAZENA!{Fore.RESET}")
#time.sleep(0.9)
#print("Počkejte prosím...")
#time.sleep(1.5)
#mixer.music.stop()
# Hra
nerozumel = 0
nerozumel_kolo = False
vyhral = None
for otazka in count(start=1):
    otazka -= nerozumel
    if not nerozumel_kolo:
        random_index = 1 #random.randint(0, 1)
    if otazka > list(otazky.keys())[-1]:
        vyhral = True
        break
    print(f"{otazka}. otázka:")
    if not nerozumel_kolo:
        mixer.Sound("začátek otázky.mp3").play()
        time.sleep(3)
    if otazka == 1:
        mixer.music.load("chcete být pythonářem prvních 5 otázek.mp3")
        mixer.music.play(-1)
    elif otazka > 5 and otazka < 15:
        mixer.music.load(f"chcete být pythonářem otázka {otazka}.mp3")
        mixer.music.play(-1)
    time.sleep(1.8)
    print(f"\n{list(otazky.get(otazka)[random_index].keys())[-1]}\n")
    time.sleep(1.8)
    odpovedi = list(otazky.get(otazka)[random_index].values())[0]
    for odpoved in odpovedi:
        time.sleep(0.1)
        spravna_odpoved = None
        if odpoved == list(odpovedi)[-1]:
            print(odpoved, end=": ")
            break
        print(odpoved)
    user_odpoved = input()
    spravne_a_nespravne_odpovedi = {}
    for odpoved in odpovedi:
        spravne_a_nespravne_odpovedi[odpoved[0]] = odpovedi.get(odpoved)
    if user_odpoved in spravne_a_nespravne_odpovedi and spravne_a_nespravne_odpovedi.get(user_odpoved):
        time.sleep(2)
        print("Správná odpověď!")
        mixer.Sound("správná odpověď.mp3").play()
        time.sleep(1.5)
        nerozumel_kolo = False
    elif user_odpoved in spravne_a_nespravne_odpovedi and not spravne_a_nespravne_odpovedi.get(user_odpoved):
        vyhral = False
        break
    else:
        print("Nerozumím...")
        nerozumel += 1
        nerozumel_kolo = True
# Konec hry
if vyhral:
    mixer.music.load("chcete být pythonářem výhra.mp3")
    mixer.music.play()
    print("VYHRÁL JSI! JSI OPRAVDOVÝ PYTHONÁŘ!!!")
    time.sleep(22)
    exit()
time.sleep(2)
mixer.music.load("chcete být pythonářem prohra.mp3")
mixer.music.play()
print("To je špatná odpověď!")
time.sleep(2)
print("GAME OVER!")
time.sleep(6)