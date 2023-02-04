class Clovek:
    def __init__(self, jmeno, prijmeni, vek, mesto_narozeni):
        #self.jmeno = jmeno
        #self.prijmeni = prijmeni
        #self.vek = vek
        #self.mesto_narozeni = mesto_narozeni
        print(f"Jmenujete se {jmeno} {prijmeni}. Je vám {vek} let. Jste z města {mesto_narozeni}.\n")
        print("TO JE PRAVDĚPODOBNĚ VÁŠ E-MAIL :D")
        print(f"{jmeno}.{prijmeni}@gmail.com")

def start():
    starting = input("Ahoj, uděláme s tebou menší interview. Co ty na to? A = chci, N = nechci")
    if starting == "A":
        interview()
    elif starting == "N":
        print("Tak nic :(")
        exit
    else:
        print("Co jsi říkal?")
        start()

def interview():
    pls_jmeno = input("Vaše jméno? ")
    pls_prijmeni = input("Vaše příjmení? ")
    pls_vek = input("Kolik je vám let?")
    pls_mesto_narozeni = input("Kde jste se narodil? ")
    Clovek(pls_jmeno, pls_prijmeni, pls_vek, pls_mesto_narozeni)

start()