import random
import math
import time
import os
from colorama import init, Fore, Back, Style
from pygame import mixer

init()
mixer.init()
clear = "cls" if os.name == "nt" else "clear"
mixer.music.load("hudba do pozadí.mp3")
mixer.music.play(-1)

# Intro
'''
os.system(clear)
time.sleep(0.8)
print("KV uvádí...")
time.sleep(1.2)
print("Pepa Na Výpravách!")
time.sleep(1.7)
print(f"{Fore.LIGHTBLACK_EX}Speciální poděkování firmě {Fore.RED}Rare{Fore.LIGHTBLACK_EX} za poskytnutí licence na hudbu v pozadí {Fore.RED}GOLDENEYE 007 MAIN THEME{Fore.RESET}")
time.sleep(1.6)
print(f"{Fore.LIGHTBLACK_EX}© 2021 - 2022 VŠECHNA PRÁVA VYHRAZENA!{Fore.RESET}")
time.sleep(4.9)
'''
# Pepa
class Pepa():
	def __init__(self, penize, zivoty, xp, level):
		self.penize = penize
		self.zivoty = zivoty
		self.max_zivoty = zivoty
		self.limit_zivoty = 350
		self.xp = xp
		self.level = level
		self.stats = [30, 50]
		self.xp_multiplier = 1
		self.koupeno = []
		self.vlastnene_itemy = []
		self.damage = 0
		self.max_damage = 1000
		self.resistance = 0
		self.max_resistance = 150
		self.faze = 1

	def __repr__(self):
		return f"Pepo, máš {Fore.RED}{self.zivoty} životů{Fore.RESET} a {Fore.LIGHTMAGENTA_EX}{self.penize} peněz{Fore.RESET}. Máš {Fore.LIGHTBLUE_EX}level {self.level}{Fore.BLUE} ({self.xp} / {50 * int(self.level)} XP){Fore.RESET}\nChceš se vydat na výpravu? A = Ano, S = Shop, C = Character: "

	def vyprava(self):
		nepritel = Nepritel(random.randint(self.stats[0], self.stats[1]))
		self.boss = nepritel.bossfight()
		if (self.boss): return
		self.ztraceno_zivotu = 0 if (x := (int(round(nepritel.return_damage() - self.damage / 100 - self.resistance/(10+pepa.level), 0)))) < 0 else x
		self.ziskano_penez = random.randint(15, 30)
		self.ziskano_xp = int(round(random.randint(10, 25) * self.xp_multiplier, 0))
		self.drops = nepritel.generate_drops()
		self.vlastnene_itemy += self.drops
		# print(self.vlastnene_itemy)

		self.zivoty -= self.ztraceno_zivotu
		self.penize += self.ziskano_penez
		self.xp += self.ziskano_xp

	def zivotu_ztraceno(self):
		return self.ztraceno_zivotu

	def penez_ziskano(self):
		return self.ziskano_penez

	def xp_ziskano(self):
		return self.ziskano_xp

	def return_drops(self):
		return self.drops

	def rank_up(self):
		self.xp -= 50 * self.level
		self.level += 1
		print(f"{Fore.LIGHTBLUE_EX}Pepo, dostal jsi nový level! Jsi už na levelu " + str(self.level) + f"!{Fore.RESET}")

# Pro debug dobrý...
pepa = Pepa(0, 100, 0, 1)

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
			if nazev != "Life potion":
				pepa.vlastnene_itemy.append(self)
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
	def __init__(self, nazev, zkratka, cena, pocet_kusu, barva, potrebny_level, predchozi_itemy, heal):
		super().__init__(nazev, zkratka, cena, pocet_kusu, barva, potrebny_level, predchozi_itemy)
		self.heal = heal

	def koupit(self):
		self.k = self.nakup(self.nazev, self.cena, self.pocet_kusu, self.potrebny_level, self.predchozi_itemy)
		if "Error" not in self.k:
			if pepa.max_zivoty - pepa.zivoty <= self.heal:
				pepa.zivoty = pepa.max_zivoty
			else:
				pepa.zivoty += self.heal

class Mec(Item):
	def __init__(self, nazev, zkratka, cena, pocet_kusu, barva, potrebny_level, predchozi_itemy, stat):
		super().__init__(nazev, zkratka, cena, pocet_kusu, barva, potrebny_level, predchozi_itemy)
		self.stat = stat

	def koupit(self):
		self.k = self.nakup(self.nazev, self.cena, self.pocet_kusu, self.potrebny_level, self.predchozi_itemy)
		if "Error" not in self.k:
			self.pocet_kusu -= 1
			pepa.stats[0] = self.stat

class Stit(Item):
	def __init__(self, nazev, zkratka, cena, pocet_kusu, barva, potrebny_level, predchozi_itemy, stat):
		super().__init__(nazev, zkratka, cena, pocet_kusu, barva, potrebny_level, predchozi_itemy)
		self.stat = stat

	def koupit(self):
		self.k = self.nakup(self.nazev, self.cena, self.pocet_kusu, self.potrebny_level, self.predchozi_itemy)
		if "Error" not in self.k:
			self.pocet_kusu -= 1
			pepa.stats[1] = self.stat

class XPMultiplier(Item):
	def __init__(self, nazev, zkratka, cena, pocet_kusu, barva, potrebny_level, predchozi_itemy):
		super().__init__(nazev, zkratka, cena, pocet_kusu, barva, potrebny_level, predchozi_itemy)

	def koupit(self):
		self.k = self.nakup(self.nazev, self.cena, self.pocet_kusu, self.potrebny_level, self.predchozi_itemy)
		if "Error" not in self.k:
			self.pocet_kusu -= 1
			pepa.xp_multiplier += 0.2

class Drop(Item):
	def __init__(self, nazev, zkratka, cena, barva, vlastnosti):
		super().__init__(nazev, zkratka, cena, None, barva, pepa.level, [])
		self.vlastnosti = vlastnosti
		self.ilvl = pepa.level

	def __repr__(self):
		return f"{self.barva}{self.zkratka} = {self.nazev} ({self.ilvl} iLVL, {self.cena} peněz) => {self.vlastnosti}"

class DamageUpgrade(Drop):
	def __init__(self, nazev, zkratka, cena, barva):
		self.add_damage = random.randint(200 * (pepa.level // 3), 200 * (pepa.level // 2))
		super().__init__(nazev, zkratka, cena, barva, f"+{self.add_damage} damage")
		pepa.damage += self.add_damage
		pepa.damage = pepa.damage if pepa.damage <= pepa.max_damage else pepa.max_damage

class HealthUpgrade(Drop):
	def __init__(self, nazev, zkratka, cena, barva):
		self.add_health = random.randint(10 * (pepa.level // 3), 10 * (pepa.level // 2))
		super().__init__(nazev, zkratka, cena, barva, f"+{self.add_health} životů")
		pepa.max_zivoty += self.add_health
		pepa.max_zivoty = pepa.max_zivoty if pepa.max_zivoty <= pepa.limit_zivoty else pepa.limit_zivoty

class ResistanceUpgrade(Drop):
	def __init__(self, nazev, zkratka, cena, barva):
		self.add_damage = random.randint(250 * (pepa.level // 3), 250 * (pepa.level // 2))
		super().__init__(nazev, zkratka, cena, barva, f"+{self.add_damage//10} odolnost")
		pepa.resistance += self.add_damage//10
		pepa.resistance = pepa.resistance if pepa.resistance <= pepa.max_resistance else pepa.max_resistance

# Inicializace itemů
lifePotion = LifePotion("Life potion", "L", 25, None, Fore.LIGHTRED_EX, 1, [], 100)
drevenyMec = Mec("Dřevěný meč", "DM", 150, 1, Fore.LIGHTBLACK_EX, 3, [], 25)
drevenyStit = Stit("Dřevěný štít", "DŠ", 200, 1, Fore.LIGHTBLACK_EX, 3, [], 40)
bronzovyMec = Mec("Bronzový meč", "BM", 350, 1, Fore.YELLOW, 7, ["Dřevěný meč"], 20)
bronzovyStit = Stit("Bronzový štít", "BŠ", 400, 1, Fore.YELLOW, 7, ["Dřevěný štít"], 30)
xpMultiplier = XPMultiplier("XP Multiplier", "XP", 500, 5, Fore.BLUE, 8, ["Dřevěný meč", "Dřevěný štít"])
itemy = [lifePotion, drevenyMec, drevenyStit, bronzovyMec, bronzovyStit, xpMultiplier]
dropy = [
	{"DamageUpgrade": ["Damage upgrade", "DUP", 100, "Fore.CYAN"]},
	{"HealthUpgrade": ["Health upgrade", "HUP", 100, "Fore.LIGHTRED_EX"]},
	{"HealthUpgrade": ["Health upgrade", "HUP", 100, "Fore.LIGHTRED_EX"]},
	{"ResistanceUpgrade": ["Resistance upgrade", "RUP", 100, "Fore.BLUE"]},
	{"ResistanceUpgrade": ["Resistance upgrade", "RUP", 100, "Fore.BLUE"]}
]

# Nepřátelé
class Nepritel():
	def __init__(self, damage):
		self.damage = damage

	def return_damage(self):
		return self.damage

	def generate_drops(self):
		# čím větší level, tím více dropů!
        # NEMĚNIT
		x = pepa.level // 3
		y = x
		drops = []
		while x > 0 and y > 0:
			per = random.random()
			x = random.randint(0, x)
			if x > 0:
				if x / 10 >= per - x / 5:
					drop = random.choice(dropy)
					drop_c = str(list(drop.keys())[0])
					exec(f"drops.append({drop_c}(\"{drop.get(drop_c)[0]}\", \"{drop.get(drop_c)[1]}\", {drop.get(drop_c)[2]}, {drop.get(drop_c)[3]}))")
			y -= 1
		return drops
	def bossfight(self):
		boss = None
		# Agent
		if pepa.level >= 6 and pepa.faze == 1:
			if pepa.level == 8:
				x = 8
			else:
				x = random.randint(pepa.level - math.ceil(pepa.level/2), 8)
				if x == 8:
					boss = "Agent"

		if boss is None:
			return boss
		# Agent bossfight
		if boss == "Agent":
			boss_health = 2000
			boss_damage = [80, 120]
		while True:
			pepa_status = str(pepa)
			print(pepa_status.split("\n")[0])
			print(f"Napadl tě {Style.BRIGHT}{Fore.RED}{boss}!{Fore.RESET}{Style.RESET_ALL}")
			bossfight_input = input("Co chceš dělat? A = Útok, L = Life potion (25 peněz), B = Bránit se: ").upper()
			if bossfight_input == "A":
				pepa_damage = 0 if (x := random.randint(pepa.damage - 200, pepa.damage + 200) // 5) < 0 else x
				boss_health -= pepa_damage
				print(f"Zaútočil jsi a dal jsi {Fore.LIGHTBLUE_EX}{pepa_damage} damage!{Fore.RESET}")
				if boss_health <= 0:
					print(f"Úspěšně jsi zabil bosse {pepa.faze}. fáze jménem {Style.BRIGHT}{Fore.RED}{boss}{Fore.RESET}{Style.RESET_ALL}, Pepo! Jsem na tebe hrdý!\nTímto smíš vstoupit do nové fáze.")
					pepa.faze += 1
					return 1
			elif bossfight_input == "B":
				pepa_damage = pepa.stats[0] if (x := pepa.resistance - random.randint(pepa.stats[0], pepa.stats[1])) < pepa.stats[0] else x
				if (pepa.stats[0] <= 25):
					pepa_damage += pepa.stats[0]
				boss_health -= pepa_damage
				print(f"Bránil ses úspěšně, boss si vzal sám sobě {Fore.LIGHTBLUE_EX}{pepa_damage} damage!{Fore.RESET}")
				if boss_health <= 0:
					print(f"Úspěšně jsi zabil bosse {Back.LIGHTGREEN_EX}{pepa.faze}. fáze{Back.RESET} jménem {Style.BRIGHT}{Fore.RED}{boss}{Fore.RESET}{Style.RESET_ALL}, Pepo! Jsem na tebe hrdý!\nTímto smíš vstoupit do nové fáze.")
					pepa.faze += 1
					return 1
			if bossfight_input == "A" or bossfight_input == "B":
				boss_damage_now = random.randint(boss_damage[0], boss_damage[1]) - pepa.resistance // pepa.level
				boss_damage_now = boss_damage_now if bossfight_input == "A" else boss_damage_now - random.randint(30, 40)
				pepa.zivoty -= boss_damage_now
				print(f"{Fore.RED}{boss}{Fore.RESET} Ti dal {boss_damage_now} damage!")
				if pepa.zivoty <= 0:
					print(f"{Fore.LIGHTRED_EX}Bohužel, Pepa umřel na výpravě.{Fore.RESET}")
					mixer.music.load("hudba když zemřeš.mp3")
					mixer.music.play()
					time.sleep(10)
					exit(0)
			elif bossfight_input == "L":
				if (pepa.penize >= 25):
					print(f"{Fore.GREEN}Úspěšně zakoupen life potion, Pepo!")
					pepa.penize -= 25
					pepa.zivoty = pepa.max_zivoty if pepa.max_zivoty - pepa.zivoty <= 100 else pepa.zivoty + 100
				else:
					print(f"{Fore.RED}Error: Nemáš doatatek peněz, Pepo!{Fore.RESET}")
			else:
				print("WHAT?\n")

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

		if (not pepa.boss):
			drop_str = ""
			for drop in pepa.return_drops():
				drop_str += f"Padlo ti: {Back.BLUE}{drop.nazev}{Back.RESET}\n"

			print(f"{Fore.LIGHTCYAN_EX}Pepo, to bylo ofous! Ztratil jsi {Fore.RED}{pepa.zivotu_ztraceno()} životů{Fore.RESET}{Fore.LIGHTCYAN_EX} a získal jsi {Fore.LIGHTMAGENTA_EX}{pepa.penez_ziskano()} peněz{Fore.RESET}{Fore.LIGHTCYAN_EX}.\nDostal jsi {Fore.BLUE}{pepa.xp_ziskano()} XP{Fore.RESET}{Fore.LIGHTCYAN_EX}!\n" + drop_str + f"{Fore.RESET}{Fore.LIGHTGREEN_EX}Stiskni COKOLI pro pokračování: {Fore.RESET}", end="")
			input()
	elif rozhodnuti == "S":
		print(f"{Fore.MAGENTA}Co chceš koupit?{Fore.RESET}\n")
		shop()
		vyber = input().upper()
		print(kupovani(vyber))
	elif rozhodnuti == "C":
		print(f"{Fore.MAGENTA}Vlastněné itemy:{Fore.RESET}")
		for vlastneny_item in pepa.vlastnene_itemy:
			if ">" not in str(vlastneny_item):
				print(f"{vlastneny_item.barva}{vlastneny_item.zkratka} = {vlastneny_item.nazev} => " + ("Menší šance na větší útok nepřátel" if "meč" in vlastneny_item.nazev else "Snížení limitu damage nepřátel") + f"{Fore.RESET}")
			else:
				print(str(vlastneny_item) + Fore.RESET)
		print(f"{Style.BRIGHT}DUP:{Style.RESET_ALL} {pepa.damage}/{pepa.max_damage}\t{Style.BRIGHT}HUP:{Style.RESET_ALL} {pepa.max_zivoty}/{pepa.limit_zivoty}\t{Style.BRIGHT}RUP:{Style.RESET_ALL} {pepa.resistance}/{pepa.max_resistance}")
	else:
		print("What?\n")
