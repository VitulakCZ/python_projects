import random
import time
from colorama import init, Fore
from pygame import mixer
init()
mixer.init()
mixer.music.load("hudba do pozadí.mp3")
mixer.music.play(-1)
# Intro
time.sleep(0.8)
print("KV uvádí...")
time.sleep(1.2)
print("Pepa Na Výpravách!")
time.sleep(1.7)
print(f"{Fore.LIGHTBLACK_EX}Speciální poděkování firmě {Fore.RED}Rare{Fore.LIGHTBLACK_EX} za poskytnutí licence na hudbu v pozadí {Fore.RED}GOLDENEYE 007 MAIN THEME{Fore.RESET}")
time.sleep(1.6)
print(f"{Fore.LIGHTBLACK_EX}© 2021 - 2022 VŠECHNA PRÁVA VYHRAZENA!{Fore.RESET}")
time.sleep(4.9)

# Pepa
class Pepa():
	def __init__(self, penize, zivoty, xp):
		self.penize = penize
		self.zivoty = zivoty
		self.xp = xp
		self.level = 1
		self.stats = [20, 50]
		self.xp_multiplier = 1
		self.koupeno = []

	def __repr__(self):
		return f"Pepo, máš {Fore.RED}{self.zivoty} životů{Fore.RESET} a {Fore.LIGHTMAGENTA_EX}{self.penize} peněz{Fore.RESET}. Máš {Fore.LIGHTBLUE_EX}level {self.level}{Fore.BLUE} ({self.xp} / {50 * int(self.level)} XP){Fore.RESET}\nChceš se vydat na výpravu? A = Ano, S = Shop: "

	def vyprava(self):
		self.ztraceno_zivotu = random.randint(self.stats[0], self.stats[1])
		self.ziskano_penez = random.randint(15, 30)
		self.ziskano_xp = int(round(random.randint(10, 25) * self.xp_multiplier, 0))

		self.zivoty -= self.ztraceno_zivotu
		self.penize += self.ziskano_penez
		self.xp += self.ziskano_xp

	def zivotu_ztraceno(self):
		return self.ztraceno_zivotu

	def penez_ziskano(self):
		return self.ziskano_penez

	def xp_ziskano(self):
		return self.ziskano_xp

	def rank_up(self):
		self.xp -= 50 * self.level
		self.level += 1
		print(f"{Fore.LIGHTBLUE_EX}Pepo, dostal jsi nový level! Jsi už na levelu " + str(self.level) + f"!{Fore.RESET}")

# Pro debug dobrý...
pepa = Pepa(0, 100, 0)

class Item():
	def __init__(self, nazev, zkratka, cena, pocet_kusu, barva, potrebny_level, predchozi_itemy):
		self.nazev = nazev
		self.zkratka = zkratka
		self.cena = cena
		self.pocet_kusu = pocet_kusu
		self.barva = barva
		self.potrebny_level = potrebny_level
		self.predchozi_itemy = predchozi_itemy

	def __repr__(self):
		return f"{self.barva}{self.zkratka} = {self.nazev} ({self.cena} peněz, " + (f"{self.pocet_kusu}" if self.pocet_kusu != None else "nekonečno") + " kusů)"

	def nakup(self, nazev, cena, pocet_kusu, potrebny_level, predchozi_itemy):
		if pocet_kusu != None and pocet_kusu < 1:
			return self.neni_na_sklade()
		if not all(value in pepa.koupeno for value in predchozi_itemy):
			return self.neni_predchozi_item(predchozi_itemy)
		if pepa.level < self.potrebny_level:
			return self.nedostatecny_level()
		if pepa.penize < cena:
			return self.nedostatek_penez()
		pepa.penize -= cena
		if nazev not in pepa.koupeno:
			pepa.koupeno.append(nazev)
		return f"{Fore.GREEN}Úspěšně zakoupen {nazev}, Pepo!{Fore.RESET}"

	def nedostatek_penez(self):
		return f"{Fore.RED}Error: Nemáš doatatek peněz, Pepo!{Fore.RESET}"

	def nedostatecny_level(self):
		return f"{Fore.RED}Error: Nemáš dostatek levelů, Pepo!{Fore.RESET}"

	def neni_predchozi_item(self, predchozi_itemy):
		return_str = ""
		nekoupene_predchozi_itemy = []

		for item in predchozi_itemy:
			if item not in pepa.koupeno:
				nekoupene_predchozi_itemy.append(item)

		for item in nekoupene_predchozi_itemy:
			if item == nekoupene_predchozi_itemy[0] and len(nekoupene_predchozi_itemy) == 1:
				return_str += f"{Fore.RED}Error: Nekoupil sis ani {item} Pepo!"
			elif item == nekoupene_predchozi_itemy[0]:
				return_str += f"{Fore.RED}Error: Nekoupil sis ani {item} ani "
			elif item != nekoupene_predchozi_itemy[-1]:
				return_str += f"{item} ani "
			else:
				return_str += f"{item} Pepo!{Fore.RESET}"
		return return_str

	def neni_na_sklade(self):
		return f"{Fore.RED}Error: Vyprodáno!{Fore.RESET}"

class LifePotion(Item):
	def __init__(self, nazev, zkratka, cena, pocet_kusu, barva, potrebny_level, predchozi_itemy):
		super().__init__(nazev, zkratka, cena, pocet_kusu, barva, potrebny_level, predchozi_itemy)

	def koupit(self):
		self.k = self.nakup(self.nazev, self.cena, self.pocet_kusu, self.potrebny_level, self.predchozi_itemy)
		if "Error" not in self.k:
			pepa.zivoty = 100

class DrevenyMec(Item):
	def __init__(self, nazev, zkratka, cena, pocet_kusu, barva, potrebny_level, predchozi_itemy):
		super().__init__(nazev, zkratka, cena, pocet_kusu, barva, potrebny_level, predchozi_itemy)

	def koupit(self):
		self.k = self.nakup(self.nazev, self.cena, self.pocet_kusu, self.potrebny_level, self.predchozi_itemy)
		if "Error" not in self.k:
			self.pocet_kusu -= 1
			pepa.stats[0] = 15

class DrevenyStit(Item):
	def __init__(self, nazev, zkratka, cena, pocet_kusu, barva, potrebny_level, predchozi_itemy):
		super().__init__(nazev, zkratka, cena, pocet_kusu, barva, potrebny_level, predchozi_itemy)

	def koupit(self):
		self.k = self.nakup(self.nazev, self.cena, self.pocet_kusu, self.potrebny_level, self.predchozi_itemy)
		if "Error" not in self.k:
			self.pocet_kusu -= 1
			pepa.stats[1] = 40

class BronzovyMec(Item):
	def __init__(self, nazev, zkratka, cena, pocet_kusu, barva, potrebny_level, predchozi_itemy):
		super().__init__(nazev, zkratka, cena, pocet_kusu, barva, potrebny_level, predchozi_itemy)

	def koupit(self):
		self.k = self.nakup(self.nazev, self.cena, self.pocet_kusu, self.potrebny_level, self.predchozi_itemy)
		if "Error" not in self.k:
			self.pocet_kusu -= 1
			pepa.stats[0] = 10

class BronzovyStit(Item):
	def __init__(self, nazev, zkratka, cena, pocet_kusu, barva, potrebny_level, predchozi_itemy):
		super().__init__(nazev, zkratka, cena, pocet_kusu, barva, potrebny_level, predchozi_itemy)

	def koupit(self):
		self.k = self.nakup(self.nazev, self.cena, self.pocet_kusu, self.potrebny_level, self.predchozi_itemy)
		if "Error" not in self.k:
			self.pocet_kusu -= 1
			pepa.stats[1] = 30

class XPMultiplier(Item):
	def __init__(self, nazev, zkratka, cena, pocet_kusu, barva, potrebny_level, predchozi_itemy):
		super().__init__(nazev, zkratka, cena, pocet_kusu, barva, potrebny_level, predchozi_itemy)

	def koupit(self):
		self.k = self.nakup(self.nazev, self.cena, self.pocet_kusu, self.potrebny_level, self.predchozi_itemy)
		if "Error" not in self.k:
			self.pocet_kusu -= 1
			pepa.xp_multiplier += 0.2

# Inicializace itemů
lifePotion = LifePotion("Life potion", "L", 25, None, Fore.LIGHTRED_EX, 1, [])
drevenyMec = DrevenyMec("Dřevěný meč", "DM", 150, 1, Fore.LIGHTBLACK_EX, 3, [])
drevenyStit = DrevenyStit("Dřevěný štít", "DŠ", 200, 1, Fore.LIGHTBLACK_EX, 3, [])
bronzovyMec = BronzovyMec("Bronzový meč", "BM", 350, 1, Fore.YELLOW, 7, ["Dřevěný meč"])
bronzovyStit = BronzovyStit("Bronzový štít", "BŠ", 400, 1, Fore.YELLOW, 7, ["Dřevěný štít"])
xpMultiplier = XPMultiplier("XP Multiplier", "XP", 500, 5, Fore.BLUE, 8, ["Dřevěný meč", "Dřevěný štít"])
itemy = [lifePotion, drevenyMec, drevenyStit, bronzovyMec, bronzovyStit, xpMultiplier]

# Nepřátelé
#

def kupovani(vec):
	match vec:
		case "L":
			lifePotion.koupit()
			item_k = lifePotion.k
		case "DM":
			drevenyMec.koupit()
			item_k = drevenyMec.k
		case "DŠ":
			drevenyStit.koupit()
			item_k = drevenyStit.k
		case "BM":
			bronzovyMec.koupit()
			item_k = bronzovyMec.k
		case "BŠ":
			bronzovyStit.koupit()
			item_k = bronzovyStit.k
		case "XP":
			xpMultiplier.koupit()
			item_k = xpMultiplier.k
		case _:
			return "Zpět!"
	return item_k

def shop():
	print("\n".join(map(str, itemy[:-1])))
	print(itemy[-1], end="")
	print(Fore.RESET, end=": ")

# Herní smyčka
while True:
	while pepa.xp >= 50 * pepa.level:
		pepa.rank_up()
	print(pepa, end="")
	rozhodnuti = input().upper()
	if rozhodnuti == "A":
		pepa.vyprava()
		if pepa.zivoty <= 0:
			print(f"{Fore.LIGHTRED_EX}Bohužel, Pepa umřel na výpravě.{Fore.RESET}")
			mixer.music.load("hudba když zemřeš.mp3")
			mixer.music.play()
			time.sleep(10)

		print(f"{Fore.LIGHTCYAN_EX}Pepo, to bylo ofous! Ztratil jsi {Fore.RED}{pepa.zivotu_ztraceno()} životů{Fore.RESET}{Fore.LIGHTCYAN_EX} a získal jsi {Fore.LIGHTMAGENTA_EX}{pepa.penez_ziskano()} peněz{Fore.RESET}{Fore.LIGHTCYAN_EX}.\nDostal jsi {Fore.BLUE}{pepa.xp_ziskano()} XP{Fore.RESET}{Fore.LIGHTCYAN_EX}!{Fore.RESET}{Fore.LIGHTGREEN_EX}\nStiskni COKOLI pro pokračování: {Fore.RESET}", end="")
		input()
	elif rozhodnuti == "S":
		print(f"{Fore.MAGENTA}Co chceš koupit?{Fore.RESET}\n")
		shop()
		vyber = input().upper()
		print(kupovani(vyber))
	else:
		print("What?\n")
