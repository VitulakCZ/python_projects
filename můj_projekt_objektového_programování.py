class Koupit:
    def __init__(self, vec, cena):
        #self.vec = vec
        #self.cena = cena
        print(vec, "stojí", cena, "korun.")

def start():
    starting = input("Jakou z mých class chceš vyzkoušet? 1 = vybírání věcí: ")
    if starting == "1":
        vybrat_vec()
    else:
        print("Co prosím?")
        start()

def vybrat_vec():
    while True:
        otazka_vec = input("Vyber si věc a zeptáme se Tě na otázky: ")
        otazka_cena = input("Hmm, " + otazka_vec + ". Zajímavý výběr. Kolik tak podle vás stojí korun? ")
        Koupit(otazka_vec, otazka_cena)
        opakovat = input("Chceš mi odpovídat na otázky jiné věci? A = ano, N = ukončit: ")
        if opakovat == "N":
            break
        if opakovat == "A":
            print("DOBRÁ, JEŠTĚ JEDNOU!")
        else:
            exit()

start()