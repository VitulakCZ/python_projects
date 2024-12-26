import random
import os

clear = "clear" if os.name == "posix" else "cls"
class FirstNumberBiggerError(Exception):
    pass

def randomnumbers(first, last, number_of_numbers):
    for _ in range(number_of_numbers):
        yield random.randint(first, last)

def randomrange(first_number1, first_number2, last_number1, last_number2):
    if first_number1 > first_number2 or last_number1 > last_number2:
        raise FirstNumberBiggerError("First number(s) were bigger than the second number(s).")
    first_number = random.randint(first_number1, first_number2)
    last_number = random.randint(last_number1, last_number2)
    while first_number >= last_number:
        first_number = random.randint(first_number1, first_number2)
        last_number = random.randint(last_number1, last_number2)
    for i in range(first_number, last_number + 1):
        yield i

def randomPrachy():
    spatna_jmena = False
    while True:
        os.system(clear)
        print("Musíte zadat jméno a žádné mezerníky!\n\n" if spatna_jmena else "", end=""); spatna_jmena = False
        menu = input("Chceš hrát hru random prachy? A = Ano, N = Ne: ").upper()
        os.system(clear)
        if menu == "N":
            return
        elif menu != "A" and menu != "N":
            continue
        hrac1jmeno = input("Kdo je hráč 1: ")
        if " " in hrac1jmeno or hrac1jmeno == "":
            spatna_jmena = True
            continue
        hrac2jmeno = input("Kdo je hráč 2: ")
        if " " in hrac2jmeno or hrac2jmeno == "":
            spatna_jmena = True
            continue
        os.system(clear)
        class Hrac:
            def __init__(self):
                self.penize = round(random.randint(1000, 20000), -3)
            def return_penize(self):
                return self.penize
        hrac1 = Hrac()
        hrac2 = Hrac()
        
        print(f"{hrac1jmeno} má: {hrac1.return_penize()} peněz...")
        print(f"{hrac2jmeno} má: {hrac2.return_penize()} peněz...")
        if hrac1.return_penize() != hrac2.return_penize(): print(f"Vyhrál {hrac1jmeno}! " if hrac1.return_penize() > hrac2.return_penize() else f"Vyhrál {hrac2jmeno}! ", end="")
        else: print("Nerozhodně, musíme hrát znovu! ", end="")
        input()
# KV Script compiler
promenne = {}
while True:
    string = input("Write KV script line: ")
    if string.startswith("writeln(\"") and string.endswith("\")"):
        to_print = string.split("\"")
        try:
            zkouska = to_print[3]
            print("ERROR!")
        except IndexError:
            print(to_print[1])
    elif string.startswith("dfn(") and string.endswith(")"):
        to_define = string.split("(")[1].split(")")
        if "=" in to_define[0]:
            finalni = to_define[0].split("=")
            try:
                zkouska = to_define[2]
                print("ERROR!")
            except IndexError:
                finalni[0] = finalni[0].replace(" ", "")
                finalni[1] = finalni[1].replace(" ", "")
                promenne[finalni[0]] = finalni[1]
        else:
            print("ERROR!")
    elif string.startswith("writeln(") and string.endswith(")") and "\"" not in string:
        to_print = string.split("(")[1].split(")")
        try:
            zkouska = to_print[2]
            print("ERROR!")
        except IndexError:
            if to_print[0] in promenne:
                print(promenne[to_print[0]])
            else:
                print("ERROR!")
    else:
        print("ERROR!")
#randomPrachy()
