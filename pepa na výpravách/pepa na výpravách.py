import random
import time
from colorama import init, Fore
from pygame import mixer
init()
mixer.init()
mixer.music.load("hudba do pozadí.mp3")
mixer.music.play(-1)
# Intro
'''
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
penize = 0
zivoty = 100
xp = 0
level = 1
stats = [15, 50]
xp_multiplier = 1
xp_multiplier_kusu = 5
shop = {"L": [f"{Fore.LIGHTRED_EX}L = Life potion (25 peněz, nekonečno kusů){Fore.RESET}", True], "DM": [f"{Fore.LIGHTBLACK_EX}DM = Dřevěný meč (3. level, 150 peněz, 1 kus){Fore.RESET}", True], "DŠ": [f"{Fore.LIGHTBLACK_EX}DŠ = Dřevěný štít (3. level, 200 peněz, 1 kus){Fore.RESET}", True], "BM": [f"{Fore.YELLOW}BM = Bronzový meč (7. level, 350 peněz, 1 kus){Fore.RESET}", True], "BŠ": [f"{Fore.YELLOW}BŠ = Bronzový štít (7. level, 400 peněz, 1 kus){Fore.RESET}", True], "XP": [f"{Fore.BLUE}XP = XP 1.2x multiplier (8. level, 500 peněz, {xp_multiplier_kusu} kusů){Fore.RESET}", False]}
koupeno = []

def vyprava():
	global zivoty
	global penize
	global xp
	ztraceno_zivotu = random.randint(stats[0], stats[1])
	ziskano_penez = random.randint(15, 30)
	ziskano_xp = random.randint(10, 25) * xp_multiplier
	zivoty -= ztraceno_zivotu
	penize += ziskano_penez
	xp += ziskano_xp
	return {"ztraceno_zivotu": ztraceno_zivotu, "ziskano_penez": ziskano_penez, "ziskano_xp": ziskano_xp}

def rank_up():
	global xp
	global level
	xp -= 50 * level
	level += 1
	print(f"{Fore.LIGHTBLUE_EX}Pepo, dostal jsi nový level! Jsi už na levelu " + str(level) + f"!{Fore.RESET}")

def koupit(vec):
	global penize
	potrebny_level = 1
	# Cena věcí
	match vec:
		case "L":
			cena = 25
		case "DM":
			cena = 150
			potrebny_level = 3
		case "DŠ":
			cena = 200
			potrebny_level = 3
		case "BM":
			cena = 350
			potrebny_level = 7
		case "BŠ":
			cena = 400
			potrebny_level = 7
		case "XP":
			cena = 500
			potrebny_level = 8
	if level >= potrebny_level:
		if penize >= cena:
			penize -= cena
			# Atributy věcí
			match vec:
				case "L":
					global zivoty
					zivoty = 100
				case "DM":
					stats[0] = 10
					shop.pop(vec)
					koupeno.append(vec)
					print(f"{Fore.GREEN}Úspěšně zakoupen Dřevěný meč!{Fore.RESET}")
				case "DŠ":
					stats[1] = 40
					shop.pop(vec)
					koupeno.append(vec)
					print(f"{Fore.GREEN}Úspěšně zakoupen Dřevěný štít!{Fore.RESET}")
				case "BM":
					stats[0] = 5
					shop.pop(vec)
					koupeno.append(vec)
					print(f"{Fore.GREEN}Úspěšně zakoupen Bronzový meč!{Fore.RESET}")
				case "BŠ":
					stats[1] = 30
					shop.pop(vec)
					koupeno.append(vec)
					print(f"{Fore.GREEN}Úspěšně zakoupen Bronzový štít!{Fore.RESET}")
				case "XP":
					global xp_multiplier_kusu
					if shop.get("XP")[-1] == True:
						if xp_multiplier_kusu == 0:
							shop.pop(vec)
						xp_multiplier_kusu -= 1
						xp_multiplier += 0.2
						koupeno.append(vec)
						print(f"{Fore.GREEN}Úspěšně zakoupen XP 1.2x multiplier!{Fore.RESET}")
					else:
						print(f"{Fore.LIGHTRED_EX}Nepřededbíhej, Pepo!{Fore.RESET}")
		else:
			print(f"{Fore.RED}Nemáš doatatek peněz, Pepo!{Fore.RESET}")
	else:
		print(f"{Fore.RED}Nemáš dostatek levelů, Pepo!{Fore.RESET}")
	return cena

# Herní smyčka
while True:
	if xp >= 50 * level:
		rank_up()
	if "DM" in koupeno and "DŠ" in koupeno or "BM" in koupeno or "BŠ" in koupeno:
		shop.get("XP")[-1] = True
	print(f"Pepo, máš {Fore.RED}{zivoty} životů{Fore.RESET} a {Fore.LIGHTMAGENTA_EX}{penize} peněz{Fore.RESET}. Máš {Fore.LIGHTBLUE_EX}level {level}{Fore.BLUE} ({xp} / {50 * int(level)} XP){Fore.RESET}\nChceš se vydat na výpravu? A = Ano, S = Shop: ", end="")
	rozhodnuti = input().upper()
	if rozhodnuti == "A":
		posledni_vyprava = vyprava()
		if zivoty <= 0:
			print(f"{Fore.LIGHTRED_EX}Bohužel, Pepa umřel na výpravě.{Fore.RESET}")
			mixer.music.load("hudba když zemřeš.mp3")
			mixer.music.play()
			time.sleep(10)
			break
		print(f"{Fore.LIGHTCYAN_EX}Pepo, to bylo ofous! Ztratil jsi {Fore.RED}" + str(posledni_vyprava.get("ztraceno_zivotu")) + f" životů{Fore.RESET}{Fore.LIGHTCYAN_EX} a získal jsi {Fore.LIGHTMAGENTA_EX}" + str(posledni_vyprava.get("ziskano_penez")) + f" peněz{Fore.RESET}{Fore.LIGHTCYAN_EX}.\nDostal jsi {Fore.BLUE}" + str(posledni_vyprava.get("ziskano_xp")) + f" XP{Fore.RESET}{Fore.LIGHTCYAN_EX}!{Fore.RESET}{Fore.LIGHTGREEN_EX}\nStiskněte COKOLI pro pokračování: {Fore.RESET}", end="")
		input()
	elif rozhodnuti == "S":
		print(f"{Fore.MAGENTA}Co chceš koupit?{Fore.RESET}\n", end="")
		for i in shop:
			if i != list(shop.keys())[-1]:
				print("\n" + shop.get(i)[0], end="")
			elif shop.get(i)[-1]:
				print("\n" + shop.get(i)[0], end=": ")
			else:
				print(end=": ")
		vec = input().upper()
		if vec in shop:
			koupit(vec)
		else:
			print("Zpět!\n")
	else:
		print("What?\n")