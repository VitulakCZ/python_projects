import random
from colorama import init, Fore
import time
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
class Pepa:
	def __init__(self):
		self.penize = 0
		self.zivoty = 100
		self.xp = 0
		self.level = 1
		self.stats = [15, 50]
		self.shop = {"L": f"{Fore.LIGHTRED_EX}L = Life potion (25 peněz, nekonečno kusů){Fore.RESET}", "DM": f"{Fore.LIGHTBLACK_EX}DM = Dřevěný meč (3. level, 150 peněz, 1 kus){Fore.RESET}", "DŠ": f"{Fore.LIGHTBLACK_EX}DŠ = Dřevěný štít (3. level, 200 peněz, 1 kus){Fore.RESET}", "BM": f"{Fore.YELLOW}BM = Bronzový meč (7. level, 350 peněz, 1 kus){Fore.RESET}", "BŠ": f"{Fore.YELLOW}BŠ = Bronzový štít (7. level, 400 peněz, 1 kus){Fore.RESET}"}
	def return_zivoty(self):
		return str(self.zivoty)
	def return_penize(self):
		return str(self.penize)
	def return_xp(self):
		return str(self.xp)
	def return_level(self):
		return str(self.level)
	def return_stats(self):
		return self.stats
	def return_shop(self):
		return self.shop
	def vyprava(self):
		self.ztraceno_zivotu = random.randint(self.stats[0], self.stats[1])
		self.ziskano_penez = random.randint(15, 30)
		self.ziskano_xp = random.randint(10, 25)
		self.zivoty -= self.ztraceno_zivotu
		self.penize += self.ziskano_penez
		self.xp += self.ziskano_xp
	def return_ztraceno_zivotu(self):
		return str(self.ztraceno_zivotu)
	def return_ziskano_penez(self):
		return str(self.ziskano_penez)
	def return_ziskano_xp(self):
		return str(self.ziskano_xp)
	def rank_up(self):
		self.xp -= 50 * self.level
		self.level += 1
		return f"{Fore.LIGHTBLUE_EX}Pepo, dostal jsi nový level! Jsi už na levelu " + str(self.level) + f"!{Fore.RESET}"
	def koupit(self, vec):
		self.potrebny_level = 1
		# Cena věcí
		if vec == "L":
			self.cena = 25
		elif vec == "DM":
			self.cena = 150
			self.potrebny_level = 3
		elif vec == "DŠ":
			self.cena = 200
			self.potrebny_level = 3
		elif vec == "BM":
			self.cena = 350
			self.potrebny_level = 7
		elif vec == "BŠ":
			self.cena = 400
			self.potrebny_level = 7

		if self.level >= self.potrebny_level:
			if self.penize >= self.cena:
				self.penize -= self.cena
				# Atributy věcí
				if vec == "L":
					self.zivoty = 100
					return f"{Fore.GREEN}Úspěšně zakoupen a použit Life potion!{Fore.RESET}"
				elif vec == "DM":
					self.stats[0] = 10
					self.shop.pop(vec)
					return f"{Fore.GREEN}Úspěšně zakoupen Dřevěný meč!{Fore.RESET}"
				elif vec == "DŠ":
					self.stats[1] = 40
					self.shop.pop(vec)
					return f"{Fore.GREEN}Úspěšně zakoupen Dřevěný štít!{Fore.RESET}"
				elif vec == "BM":
					self.stats[0] = 5
					self.shop.pop(vec)
					return f"{Fore.GREEN}Úspěšně zakoupen Bronzový meč!{Fore.RESET}"
				elif vec == "BŠ":
					self.stats[1] = 30
					self.shop.pop(vec)
					return f"{Fore.GREEN}Úspěšně zakoupen Bronzový štít!{Fore.RESET}"
			else:
				return f"{Fore.RED}Nemáš doatatek peněz, Pepo!{Fore.RESET}"
		else:
			return f"{Fore.RED}Nemáš dostatek levelů, Pepo!{Fore.RESET}"

pepa = Pepa()
while True:
	if int(pepa.return_xp()) >= 50 * int(pepa.return_level()):
		print(pepa.rank_up())
	print(f"Pepo, máš {Fore.RED}" + pepa.return_zivoty() + f" životů{Fore.RESET} a {Fore.LIGHTMAGENTA_EX}" + pepa.return_penize() + f" peněz{Fore.RESET}. Máš {Fore.LIGHTBLUE_EX}level " + pepa.return_level() + f"{Fore.BLUE} (" + pepa.return_xp() + " / " + str(50 * int(pepa.return_level())) + f" XP){Fore.RESET}\nChceš se vydat na výpravu? A = Ano, S = Shop: ", end="")
	rozhodnuti = input().upper()
	if rozhodnuti == "A":
		pepa.vyprava()
		if int(pepa.return_zivoty()) <= 0:
			print(f"{Fore.LIGHTRED_EX}Bohužel, Pepa umřel na výpravě.{Fore.RESET}")
			mixer.music.load("hudba když zemřeš.mp3")
			mixer.music.play()
			time.sleep(10)
			break
		print(f"{Fore.LIGHTCYAN_EX}Pepo, to bylo ofous! Ztratil jsi {Fore.RED}" + pepa.return_ztraceno_zivotu() + f" životů{Fore.RESET}{Fore.LIGHTCYAN_EX} a získal jsi {Fore.LIGHTMAGENTA_EX}" + pepa.return_ziskano_penez() + f" peněz{Fore.RESET}{Fore.LIGHTCYAN_EX}.\nDostal jsi {Fore.BLUE}" + pepa.return_ziskano_xp() + f" XP{Fore.RESET}{Fore.LIGHTCYAN_EX}!{Fore.RESET}{Fore.LIGHTGREEN_EX}\nStiskněte COKOLI pro pokračování: {Fore.RESET}", end="")
		input()
	elif rozhodnuti == "S":
		print(f"{Fore.MAGENTA}Co chceš koupit?{Fore.RESET}\n", end="")
		for i in pepa.return_shop():
			if i != list(pepa.return_shop().keys())[-1]:
				print(pepa.return_shop().get(i))
			else:
				print(pepa.return_shop().get(i), end=": ")
		koupit = input().upper()
		if koupit in pepa.return_shop():
			print(pepa.koupit(koupit))
		else:
			print("Zpět!\n")
	else:
		print("What?\n")