import random

pocet_enteru = 0
while True:
    hra = input(f"Počet ENTERŮ: {pocet_enteru}\nL = Načíst hru, S = Uložit hru, Stiskněte ENTER: ").upper()
    if hra == "":
        pocet_enteru += 1
    elif hra == "L":
        try:
            with open("data.txt", "r") as f:
                data_poctu_enteru = []
                for pismeno_sifry in f.read():
                    if pismeno_sifry == "!" or pismeno_sifry == "@" or pismeno_sifry == "#" or pismeno_sifry == "$" or pismeno_sifry == "%" or pismeno_sifry == "^" or pismeno_sifry == "&" or pismeno_sifry == "*" or pismeno_sifry == "-" or pismeno_sifry == "_" or pismeno_sifry == "=" or pismeno_sifry == "+" or pismeno_sifry == ";" or pismeno_sifry == ":" or pismeno_sifry == "'" or pismeno_sifry == "\"" or pismeno_sifry == "¨" or pismeno_sifry == "|"  or pismeno_sifry == "," or pismeno_sifry == "<" or pismeno_sifry == "." or pismeno_sifry == ">" or pismeno_sifry == "/" or pismeno_sifry == "?" or pismeno_sifry == "´" or pismeno_sifry == "ˇ":
                        pass
                    else:
                        data_poctu_enteru.append(pismeno_sifry)
                pocet_enteru = int("".join(data_poctu_enteru))
                print("\033[0;32mÚspěšně načteno!\033[0m")
        except FileNotFoundError:
            print("\033[0;31mZatím jste neuložil žádné ENTERY!\033[0m")
    elif hra == "S":
        with open("data.txt", "w") as f:
            random_range1 = random.randint(50, 750)
            random_sifra1 = []
            random_range2 = random.randint(50, 750)
            random_sifra2 = []
            for i in range(random_range1):
                random_sifra1.append(random.choice(("!", "@", "#", "$", "%", "^", "&", "*", "-", "_", "=", "+", ";", ":", "'", "\"", "¨", "|", ",", "<", ".", ">", "/", "?", "´", "ˇ")))
            for i in range(random_range2):
                random_sifra2.append(random.choice(("!", "@", "#", "$", "%", "^", "&", "*", "-", "_", "=", "+", ";", ":", "'", "\"", "¨", "|", ",", "<", ".", ">", "/", "?", "´", "ˇ")))
            f.write("".join(random_sifra1) + str(pocet_enteru) + "".join(random_sifra2))
    else:
        print("POUZE ENTER!")