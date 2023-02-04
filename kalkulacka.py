jmenoBlbce = input("Tvoje jméno: ")
prijmeniBlbce = input("Tvoje příjmení: ")
hesloBlbce = input("Tvoje heslo: ")

print("Ahoj, " + jmenoBlbce + " " + prijmeniBlbce + ".")
funguje = input("Tvoje heslo ještě jednou: ")
if funguje == hesloBlbce:
    print("Tvoje heslo jsi zadal správně!")
    funkcni = input("Zadejte jméno a příjmení: ")
    if funkcni == jmenoBlbce + " " + prijmeniBlbce:
        print("SPRÁVNĚ!")
        kalkulackaOtazky = input("Co chceš dál? K = Kalkulačku, O = Otázky")
        if kalkulackaOtazky == "K":
                cislo1 = input("prvni cislo?")
                cislo2 = input("druhe cislo?")
                plusMinus = input("+, -, *, /?")
                if plusMinus == "+":
                    vysledek = int(cislo1) + int(cislo2)
                    print(vysledek)
                elif plusMinus == "-":
                    vysledek = int(cislo1) - int(cislo2)
                    print(vysledek)
                elif plusMinus == "*":
                    vysledek = int(cislo1) * int(cislo2)
                    print(vysledek)
                elif plusMinus == "/":
                    vysledek = int(cislo1) / int(cislo2)
                    print(vysledek)
        elif kalkulackaOtazky == "O":
            mamRadaChleba = input("Zadejte vaše nejoblíbenější jídlo: ")
            mamRadaBarvu = input("Zadejte vaši nejoblíbenější barvu: ")
            mamRadaYoutubera = input("Zadejte vašeho nejoblíbenějšího youtubera: ")
            print(mamRadaChleba + " je " + mamRadaBarvu + ". " + mamRadaYoutubera + " je do Tebe zamilovaný.")
        else:
            print("Co prosím?")
    else:
        print("OSTUDA")
else:
    print("NOPE!")
