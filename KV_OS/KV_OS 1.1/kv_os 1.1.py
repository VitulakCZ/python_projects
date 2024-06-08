import os
import time
import math
from colorama import init, Fore, Style
from cryptography.fernet import Fernet
from pygame import mixer
mixer.init()
init()
clear = "clear" if os.name == "posix" else "cls"

def convert_time(endtime):
	endtime_hrs = endtime // 3600
	endtime_mins = endtime % 3600 // 60
	endtime_secs = endtime - endtime_hrs * 3600 - endtime_mins * 60
	endtime_str = f"{endtime_hrs}h {endtime_mins}min {endtime_secs}s"
	return endtime_str

def load_key():
	try:
		with open("key.key", "rb") as file:
			key = file.read()
		return key
	except FileNotFoundError:
		key = Fernet.generate_key()
		with open("key.key", "wb") as key_file:
			key_file.write(key)
		with open("key.key", "rb") as file:
			key = file.read()
		return key
key = load_key()
fer = Fernet(key)

user = None
language = "en"
os.system(clear)
while True:
	print(f"{Fore.GREEN}KV system 1.1\n©1995 - 2022 ALL RIGHTS RESERVED!{Fore.RESET}\n")
	if user == None:
		if language == "en":
			print(f"{Fore.RED}YOU ARE NOT LOGGED IN!{Style.RESET_ALL}")
			print(f"G = Game\nP = Programming in KV script beta\nN = Patch notes\n{Fore.CYAN}R = Register\nL = Login{Fore.RESET}\nO = Options\nE = Shutdown: ", end="")
		elif language == "cz":
			print(f"{Fore.RED}NEJSTE PŘIHLÁŠENI!{Style.RESET_ALL}")
			print(f"G = Hra\nP = Programování v KV scriptu beta\nN = Novinky\n{Fore.CYAN}R = Registrovat se\nL = Přihlásit se{Fore.RESET}\nO = Nastavení\nE = Vypnout: ", end="")
		elif language == "de":
			print(f"{Fore.RED}DU BIST NICHT EINGELOGGT!{Style.RESET_ALL}")
			print(f"G = Spiel\nP = Programmierung in KV-Skript-Beta\nN = Patchnotizen\n{Fore.CYAN}R = Registrieren\nL = Anmelden {Fore.RESET}\nO = Optionen\nE = Herunterfahren: ", end="")
		home = input().upper()
	else:
		if language == "en":
			print(f"{Style.BRIGHT}{Fore.YELLOW}You are now logged in as {user}!{Style.RESET_ALL}")
			home = input("G = Game\nP = Programming in KV script beta\nN = Patch notes\nL = Logout\nO = Options\nE = Shutdown: ").upper()
		elif language == "cz":
			print(f"{Style.BRIGHT}{Fore.YELLOW}Jsi přihlášen jako {user}!{Style.RESET_ALL}")
			home = input("G = Hra\nP = Programování v KV scriptu beta\nN = Novinky\nL = Odhlásit se\nO = Nastavení\nE = Vypnout: ").upper()
		elif language == "de":
			print(f"{Style.BRIGHT}{Fore.YELLOW}Sie sind jetzt angemeldet als {user}!{Style.RESET_ALL}")
			home = input("G = Spiel\nP = Programmierung in KV-Skript-Beta\nN = Patchnotizen\nL = Abmelden\nO = Optionen\nE = Herunterfahren: ").upper()
	os.system(clear)
	if home == "G":
		if language == "en":
			game = input("__________________\n       Game\n__________________\nprocesing...\npress S = Singleplayer\n      M = Multiplayer\n      L = Load the game\nL = Leaderboards: ").upper()
		elif language == "cz":
			game = input("__________________\n        Hra\n__________________\nnačítání...\nstiskněte S = Singleplayer\n          M = Multiplayer      L = Načíst hru\nL = Žebříčky: ").upper()
		elif language == "de":
			game = input("_________________\n      Spiel\n_________________\nWird geladen...\ndrücke S = Singleplayer\n       M = Multiplayer       L = Laden Sie das Spiel\nL = Bestenlisten: ").upper()
		os.system(clear)
		if game == "S":
			obtiznost = None
			speedrun_mod = False
			hrat = True
			while True:
				if language == "en":
					obtiznost = input("On which difficulty do you want to play?\nE = Easy\nN = Normal\nH = Hard\n" + (Fore.LIGHTRED_EX if not speedrun_mod else Fore.LIGHTGREEN_EX) + "S = Speedrun mode " + ("off" if not speedrun_mod else "on") + Fore.RESET + ": ").upper()
				elif language == "cz":
					obtiznost = input("Na jakou chceš hrát obtížnost?\nE = Easy\nN = Normal\nH = Hard\n" + (Fore.LIGHTRED_EX if not speedrun_mod else Fore.LIGHTGREEN_EX) + "S = Speedrun režim " + ("vypnutý" if not speedrun_mod else "zapnutý") + Fore.RESET + ": ").upper()
				elif language == "de":
					obtiznost = input("Auf welchem Schwierigkeitsgrad möchtest du spielen?\nE = Easy\nN = Normal\nH = Hard\n" + (Fore.LIGHTRED_EX if not speedrun_mod else Fore.LIGHTGREEN_EX) + "S = Speedrun-Modus " + ("ausgeschaltet" if not speedrun_mod else "aktiviert") + Fore.RESET + ": ").upper()
				os.system(clear)
				if obtiznost == "S":
					if user is not None:
						speedrun_mod = not speedrun_mod
					else:
						if language == "en":
							print(f"{Fore.RED}You have to be logged in to be able to play Speedrun mode!{Fore.RESET}\n")
						elif language == "cz":
							print(f"{Fore.RED}Musíte být přihlášení, abyste mohli hrát Speedrun režim!{Fore.RESET}\n")
						elif language == "de":
							print(f"{Fore.RED}Sie müssen angemeldet sein, um den Speedrun-Modus spielen zu können!{Fore.RESET}\n")
				elif obtiznost == "E":
					if language == "en":
						input("""\
EASY difficulty
- You start with 3 mld. money
- You start with 2000 soldiers
- Until you don't invest, you get 2 mld. money per round
- If you want to win, you have to have 28 areas
- You can invest to 10 money per round
- Invensions come each 10 rounds to your country
- Invasions are always per 1000 soldiers
Press any key to continue: """)
					elif language == "cz":
						input("""\
EASY obtížnost
- Začínáte s 3 mld. penězi
- Začínáte s 2000 vojáky
- Dokud neinvestujete, získáváte 2 mld. peněz za kolo
- Chcete-li vyhrát, musíte získat 28 území
- Investovat můžete do 10 peněz za kolo
- Invaze do vaší země se konají každých 10 kol
- Invaze jsou vždy po 1000 vojácích
Jakoukoli klávesou pokračujte: """)
					elif language == "de":
						input("""\
EINFACHE Schwierigkeit
- Sie beginnen mit 3 mld. Geld
- Sie beginnen mit 2000 Soldaten
- Bis Sie nicht investieren, erhalten Sie 2 mld. Geld pro Runde
- Wenn du gewinnen willst, musst du 28 Gebiete haben
- Sie können bis zu 10 Geld pro Runde investieren
- Erfindungen kommen alle 10 Runden in dein Land
- Invasionen sind immer pro 1000 Soldaten
Drücken Sie eine beliebige Taste, um fortzufahren: """)
					break
				elif obtiznost == "N":
					if language == "en":
						input("""\
NORMAL difficulty
- You start with 3 mld. money
- You don't start with any soldiers
- Until you don't invest, you get 2 mld. money per round
- If you want to win, you have to have 59 areas
- You can invest to 5 money per round
- Invasions come each 5 rounds to your country
- Invasions are always per 1000 soldiers
Press any key to continue: """)
					elif language == "cz":
						input("""\
NORMAL obtížnost
- Začínáte s 3 mld. penězi
- Nezačínáte s žádnými vojáky
- Dokud neinvestujete, získáváte 2 mld. peněz za kolo
- Chcete-li vyhrát, musíte získat 59 území
- Investovat můžete do 5 peněz za kolo
- Invaze do vaší země se konají každých 5 kol
- Invaze jsou vždy po 1000 vojácích
Jakoukoli klávesou pokračujte: """)
					elif language == "de":
						input("""\
NORMALE Schwierigkeit
- Sie beginnen mit 3 mld. Geld
- Du fängst nicht mit irgendwelchen Soldaten an
- Bis Sie nicht investieren, erhalten Sie 2 mld. Geld pro Runde
- Wenn du gewinnen willst, musst du 59 Gebiete haben
- Sie können bis zu 5 Geld pro Runde investieren
- Invasionen kommen alle 5 Runden in dein Land
- Invasionen sind immer pro 1000 Soldaten
Drücken Sie eine beliebige Taste, um fortzufahren: """)
					break
				elif obtiznost == "H":
					if language == "en":
						input("""\
HARD difficulty
- You don't start with any money
- You don't start with any soldiers
- Until you don't invest, you get 2 mld. money per round
- If you want to win, you have to have 70 areas
- You can invest to 5 money per round
- Invasions come each 5 rounds to your country
- Invasions are always per 2000 soldiers
Press any key to continue: """)
					elif language == "cz":
						input("""\
HARD obtížnost
- Nezačínáte s žádnými penězi
- Nezačínáte s žádnými vojáky
- Dokud neinvestujete, získáváte 2 mld. peněz za kolo
- Chcete-li vyhrát, musíte získat 70 území
- Investovat můžete do 5 peněz za kolo
- Invaze do vaší země se konají každých 5 kol
- Invaze jsou vždy po 2000 vojácích
Jakoukoli klávesou pokračujte: """)
					elif language == "de":
						input("""\
SCHWERE Schwierigkeit
- Sie beginnen nicht mit Geld
- Du fängst nicht mit irgendwelchen Soldaten an
- Bis Sie nicht investieren, erhalten Sie 2 mld. Geld pro Runde
- Wenn du gewinnen willst, musst du 70 Gebiete haben
- Sie können bis zu 5 Geld pro Runde investieren
- Invasionen kommen alle 5 Runden in dein Land
- Invasionen sind immer pro 2000 Soldaten
Drücken Sie eine beliebige Taste, um fortzufahren: """)
					break
				else:
					print("Another key!")
					hrat = False
					break
			if not hrat:
				continue
			os.system(clear)
			mixer.music.load("kv_war_simulator_soundtrack.wav")
			mixer.music.play(-1)
			if language == "en":
				print(f"{Fore.YELLOW}This is upgraded version of the game textova_hra.py. If you want to have old feelings, download KV OS 0.6.{Fore.RESET}")
				if speedrun_mod:
					print(f"{Fore.YELLOW}{Style.BRIGHT}You are playing Speedrun mode, your time and vicory round will be put on the leaderboards. Good luck!{Fore.RESET}{Style.RESET_ALL}")
			elif language == "cz":
				print(f"{Fore.YELLOW}Toto je vylepšená verze hry textova_hra.py. Jestli chcete mít zážitek ze hry textova_hra, jako takový, stáhněte si KV OS BETA 0.6.{Fore.RESET}")
				if speedrun_mod:
					print(f"{Fore.YELLOW}{Style.BRIGHT}Hrajete ve Speedrun režimu, váš čas a vítězné kolo budou zapsány na žebříčky. Hodně štěstí!{Fore.RESET}{Style.RESET_ALL}")
			elif language == "de":
				print(f"{Fore.YELLOW}Dies ist eine aktualisierte Version des Spiels textova_hra.py. Wenn Sie alte Gefühle haben wollen, laden Sie KV OS 0.6 herunter.{Fore.RESET}")
				if speedrun_mod:
					print(f"{Fore.YELLOW}{Style.BRIGHT}Du spielst den Speedrun-Modus, deine Zeit und die Siegrunde werden in die Bestenlisten eingetragen. Viel Glück!{Fore.RESET}{Style.RESET_ALL}")
			while True:
				if language == "en":
					menu = input("Welcome, do you want to play this game? A = yes, N = no: ").upper()
				elif language == "cz":
					menu = input("Vítej, cheš hrát tuto hru? A = ano N = ne: ").upper()
				elif language == "de":
					menu = input("Willkommen, möchten Sie dieses Spiel spielen? A = ja, N = nein: ").upper()
				if menu == "A":
					if speedrun_mod:
						starttime = time.time()
					if obtiznost == "H":
						penize = 0
					else:
						penize = 3
					if obtiznost == "E":
						vojaci = 2000
					else:
						vojaci = 0
					kola = 1
					if obtiznost == "E":
						obsadit = 28
					elif obtiznost == "N":
						obsadit = 59
					elif obtiznost == "H":
						obsadit = 70
					banka = 0
					penize_za_kolo = 2
					while True:
						if obsadit == 0:
							mixer.music.load("teticka_song.wav")
							mixer.music.play(-1)
							if speedrun_mod:
								endtime = math.ceil((time.time() - starttime))
								endtime_str = convert_time(endtime)
								if language == "en":
									print(f"Time: {endtime_str}")
								elif language == "cz":
									print(f"Čas: {endtime_str}")
								elif language == "de":
									print(f"Zeit: {endtime_str}")
								list_jmen = []
								try:
									with open('data11.txt', 'r') as f:
										for line in f.readlines():
											data = line.rstrip()
											list_jmen.append(data.split("|")[0])
								except FileNotFoundError:
									pass
								with open('data11.txt', 'a') as f:
									user_cpy = user
									pocet = 1
									while user_cpy in list_jmen:
										pocet += 1
										user_cpy = user + " " + str(pocet)
									f.write(user_cpy + "|" + fer.encrypt(endtime_str.encode()).decode() + "|" + fer.encrypt(str(kola).encode()).decode() + "|" + obtiznost + "\n")
							if language == "en":
								input("CONGRATULATIONS!!! You finished the game!! You are good!!\nPress any key to continue: ")
							elif language == "cz":
								input("GRATULACE!!! Dohrál jsi hru!! Jsi dobrý!!\nStiskni cokoli pro pokračování: ")
							elif language == "de":
								input("HERZLICHE GLÜCKWÜNSCHE!!! Du hast das Spiel beendet!! Du bist gut!!\nDrücken Sie eine beliebige Taste, um fortzufahren: ")
							mixer.music.load("kv_war_simulator_soundtrack.wav")
							mixer.music.play(-1)
							os.system(clear)
							break
						elif kola == 5 and obtiznost in ["N", "H"]:
							if vojaci >= 1000 and obtiznost == "N":
								vojaci -= 1000
							elif vojaci >= 2000 and obtiznost == "H":
								vojaci -= 2000
							else:
								if language == "en":
									print("They attacked you, you don't have enough soldiers to counterattack.\nGAME OVER")
								elif language == "cz":
									print("Zaútočili na tebe, nemáš dostatek vojáků na protiútok.\nGAME OVER")
								elif language == "de":
									print("Sie haben dich angegriffen, du hast nicht genug Soldaten für einen Gegenangriff.\nGAME OVER")
								break
							if language == "en":
								print("They attacked you! You have " + str(vojaci) + " soldiers left!")
							elif language == "cz":
								print("Zaútočili na tebe! Nově máš " + str(vojaci) + " vojáků!")
							elif language == "de":
								print("Sie haben dich angegriffen! Sie haben " + str(vojaci) + " Soldaten übrig!")
							kola += 1
						elif kola == 10:
							if vojaci >= 1000 and obtiznost in ["E", "N"]:
								vojaci -= 1000
							elif vojaci >= 2000 and obtiznost == "H":
								vojaci -= 2000
							else:
								if language == "en":
									print("They attacked you, you don't have enough soldiers to counterattack.\nGAME OVER")
								elif language == "cz":
									print("Zaútočili na tebe, nemáš dostatek vojáků na protiútok.\nGAME OVER")
								elif language == "de":
									print("Sie haben dich angegriffen, du hast nicht genug Soldaten für einen Gegenangriff.\nGAME OVER")
								break
							if language == "en":
								print("They attacked you! You have " + str(vojaci) + " soldiers left!")
							elif language == "cz":
								print("Zaútočili na tebe! Nově máš " + str(vojaci) + " vojáků!")
							elif language == "de":
								print("Sie haben dich angegriffen! Sie haben " + str(vojaci) + " Soldaten übrig!")
							kola += 1
						elif kola == 15 and obtiznost in ["N", "H"]:
							if vojaci >= 1000 and obtiznost == "N":
								vojaci -= 1000
							elif vojaci >= 2000 and obtiznost == "H":
								vojaci -= 2000
							else:
								if language == "en":
									print("They attacked you, you don't have enough soldiers to counterattack.\nGAME OVER")
								elif language == "cz":
									print("Zaútočili na tebe, nemáš dostatek vojáků na protiútok.\nGAME OVER")
								elif language == "de":
									print("Sie haben dich angegriffen, du hast nicht genug Soldaten für einen Gegenangriff.\nGAME OVER")
								break
							if language == "en":
								print("They attacked you! You have " + str(vojaci) + " soldiers left!")
							elif language == "cz":
								print("Zaútočili na tebe! Nově máš " + str(vojaci) + " vojáků!")
							elif language == "de":
								print("Sie haben dich angegriffen! Sie haben " + str(vojaci) + " Soldaten übrig!")
							kola += 1
						elif kola == 20:
							if vojaci >= 1000 and obtiznost in ["E", "N"]:
								vojaci -= 1000
							elif vojaci >= 2000 and obtiznost == "H":
								vojaci -= 2000						
							else:
								if language == "en":
									print("They attacked you, you don't have enough soldiers to counterattack.\nGAME OVER")
								elif language == "cz":
									print("Zaútočili na tebe, nemáš dostatek vojáků na protiútok.\nGAME OVER")
								elif language == "de":
									print("Sie haben dich angegriffen, du hast nicht genug Soldaten für einen Gegenangriff.\nGAME OVER")
								break
							if language == "en":
								print("They attacked you! You have " + str(vojaci) + " soldiers left!")
							elif language == "cz":
								print("Zaútočili na tebe! Nově máš " + str(vojaci) + " vojáků!")
							elif language == "de":
								print("Sie haben dich angegriffen! Sie haben " + str(vojaci) + " Soldaten übrig!")
							kola += 1
						elif kola == 25 and obtiznost in ["N", "H"]:
							if vojaci >= 1000 and obtiznost == "N":
								vojaci -= 1000
							elif vojaci >= 2000 and obtiznost == "H":
								vojaci -= 2000
							else:
								if language == "en":
									print("They attacked you, you don't have enough soldiers to counterattack.\nGAME OVER")
								elif language == "cz":
									print("Zaútočili na tebe, nemáš dostatek vojáků na protiútok.\nGAME OVER")
								elif language == "de":
									print("Sie haben dich angegriffen, du hast nicht genug Soldaten für einen Gegenangriff.\nGAME OVER")
								break
							if language == "en":
								print("They attacked you! You have " + str(vojaci) + " soldiers left!")
							elif language == "cz":
								print("Zaútočili na tebe! Nově máš " + str(vojaci) + " vojáků!")
							elif language == "de":
								print("Sie haben dich angegriffen! Sie haben " + str(vojaci) + " Soldaten übrig!")
							kola += 1
						elif kola == 30:
							if vojaci >= 1000 and obtiznost in ["E", "N"]:
								vojaci -= 1000
							elif vojaci >= 2000 and obtiznost == "H":
								vojaci -= 2000
							else:
								if language == "en":
									print("They attacked you, you don't have enough soldiers to counterattack.\nGAME OVER")
								elif language == "cz":
									print("Zaútočili na tebe, nemáš dostatek vojáků na protiútok.\nGAME OVER")
								elif language == "de":
									print("Sie haben dich angegriffen, du hast nicht genug Soldaten für einen Gegenangriff.\nGAME OVER")
								break
							if language == "en":
								print("They attacked you! You have " + str(vojaci) + " soldiers left!")
							elif language == "cz":
								print("Zaútočili na tebe! Nově máš " + str(vojaci) + " vojáků!")
							elif language == "de":
								print("Sie haben dich angegriffen! Sie haben " + str(vojaci) + " Soldaten übrig!")
							kola += 1
						elif kola == 35 and obtiznost in ["N", "H"]:
							if vojaci >= 1000 and obtiznost == "N":
								vojaci -= 1000
							elif vojaci >= 2000 and obtiznost == "H":
								vojaci -= 2000
							else:
								if language == "en":
									print("They attacked you, you don't have enough soldiers to counterattack.\nGAME OVER")
								elif language == "cz":
									print("Zaútočili na tebe, nemáš dostatek vojáků na protiútok.\nGAME OVER")
								elif language == "de":
									print("Sie haben dich angegriffen, du hast nicht genug Soldaten für einen Gegenangriff.\nGAME OVER")
								break
							if language == "en":
								print("They attacked you! You have " + str(vojaci) + " soldiers left!")
							elif language == "cz":
								print("Zaútočili na tebe! Nově máš " + str(vojaci) + " vojáků!")
							elif language == "de":
								print("Sie haben dich angegriffen! Sie haben " + str(vojaci) + " Soldaten übrig!")
							kola += 1
						elif kola == 40:
							if vojaci >= 1000 and obtiznost in ["E", "N"]:
								vojaci -= 1000
							elif vojaci >= 2000 and obtiznost == "H":
								vojaci -= 2000
							else:
								if language == "en":
									print("They attacked you, you don't have enough soldiers to counterattack.\nGAME OVER")
								elif language == "cz":
									print("Zaútočili na tebe, nemáš dostatek vojáků na protiútok.\nGAME OVER")
								elif language == "de":
									print("Sie haben dich angegriffen, du hast nicht genug Soldaten für einen Gegenangriff.\nGAME OVER")
								break
							if language == "en":
								print("They attacked you! You have " + str(vojaci) + " soldiers left!")
							elif language == "cz":
								print("Zaútočili na tebe! Nově máš " + str(vojaci) + " vojáků!")
							elif language == "de":
								print("Sie haben dich angegriffen! Sie haben " + str(vojaci) + " Soldaten übrig!")
							kola += 1
						elif kola == 45 and obtiznost in ["N", "H"]:
							if vojaci >= 1000 and obtiznost == "N":
								vojaci -= 1000
							elif vojaci >= 2000 and obtiznost == "H":
								vojaci -= 2000
							else:
								if language == "en":
									print("They attacked you, you don't have enough soldiers to counterattack.\nGAME OVER")
								elif language == "cz":
									print("Zaútočili na tebe, nemáš dostatek vojáků na protiútok.\nGAME OVER")
								elif language == "de":
									print("Sie haben dich angegriffen, du hast nicht genug Soldaten für einen Gegenangriff.\nGAME OVER")
								break
							if language == "en":
								print("They attacked you! You have " + str(vojaci) + " soldiers left!")
							elif language == "cz":
								print("Zaútočili na tebe! Nově máš " + str(vojaci) + " vojáků!")
							elif language == "de":
								print("Sie haben dich angegriffen! Sie haben " + str(vojaci) + " Soldaten übrig!")
							kola += 1
						elif kola == 50:
							if language == "en":
								print("You didn't manage to finish the game under 50 rounds.\nGAME OVER")
							elif language == "cz":
								print("Nestihl jsi dohrát hru pod 50 kol.\nGAME OVER")
							elif language == "de":
								print("Du hast es nicht geschafft, das Spiel unter 50 Runden zu beenden.\nGAME OVER")
							break
						if language == "en":
							hra = input(str(kola) + ". ROUND!\nK = Buy soldiers, V = War, I = Invest, B = Bank, D = Next round, E = exit: ").upper()
						elif language == "cz":
							hra = input(str(kola) + ". KOLO!\nK = Koupit vojáky, V = Válka, I = Investovat, B = Banka, D = Další kolo, E = Pryč: ").upper()
						elif language == "de":
							hra = input(str(kola) + ". RUNDE!\nK = Soldaten kaufen, V = Krieg, I = Investieren, B = Bank, D = Nächste Runde, E = Ausgang: ").upper()
						if hra == "E":
							if language == "en":
								print("You left the game.")
							elif language == "cz":
								print("Odešel jsi ze hry.")
							elif language == "de":
								print("Du hast das Spiel verlassen.")
							break
						elif hra == "K":
							if language == "en":
								voj = input("You have " + str(vojaci) + " soldiers, " + str(penize) + " money, price for 1000 soldiers is 1 mld, for 2000 soldiers 2 mld, for 3000 soldiers 3 mld etc... How many do you want to buy? ")
							elif language == "cz":
								voj = input("Máš " + str(vojaci) + " vojáků, peněz " + str(penize) + ", cena za 1000 vojáků je 1 mld, za 2000 vojáků 2 mld, za 3000 vojáků 3 mld atd... Kolik jich chceš koupit? ")
							elif language == "de":
								voj = input("Sie haben " + str(vojaci) + " Soldaten, " + str(penize) + " Geld, Preis für 1000 Soldaten ist 1 mld, für 2000 Soldaten 2 mld, für 3000 Soldaten 3 mld usw... Wie viele möchten Sie kaufen? ")
							try:
								voj = int(voj)
								if voj % 1000 == 0:
									if penize >= voj // 1000:
										penize -= voj // 1000
										vojaci += voj
										if language == "en":
											print(f"You bought {voj} soldiers, total amount of them is " + str(vojaci) + ", you have " + str(penize) + " money left.")
										elif language == "cz":
											print(f"Nakoupeno {voj} vojáků, celkem jich máš " + str(vojaci) + ", zbývá ti " + str(penize) + " peněz.")
										elif language == "de":
											print(f"Sie haben {voj} Soldaten gekauft, der Gesamtbetrag von ihnen ist " + str(vojaci) + ", Sie haben " + str(penize) + " Geld übrig.")
									else:
										if language == "en":
											print("YOU DON'T HAVE ENOUGH MONEY\n")
										elif language == "cz":
											print("NEMÁŠ DOSTATEK FINANCÍ\n")
										elif language == "de":
											print("SIE HABEN NICHT GENUG GELD\n")
								else:
									if language == "en":
										print("You didn't enter a number divisible by 1000.\nYou have " + str(vojaci) + " soldiers, you have " + str(penize) + " money left.")
									elif language == "cz":
										print("Nezadal jsi číslo dělitelné 1000.\nCelkem máš " + str(vojaci) + " vojáků, zbývá ti " + str(penize) + " peněz.")
									elif language == "de":
										print("Sie haben keine Zahl eingegeben, die durch 1000 teilbar ist. Sie haben " + str(vojaci) + " Soldaten, Sie haben " + str(penize) + " Geld übrig.")
							except ValueError:
								if language == "en":
									print("You entered wrong input! Please, numbers!")
								elif language == "cz":
									print("Zadal jsi špatné zadání! Prosím, používejte čísla!")
								elif language == "de":
									print("Sie haben eine falsche Eingabe eingegeben! Bitte, Zahlen!")
						elif hra == 'D':
							kola += 1
							penize += penize_za_kolo
							penize -= banka
							banka = 0
						elif hra == 'V':
							if language == "en":
								valka = input("You still have to occupy " + str(obsadit) + " areas. On a one area you have to have 2000 soldiers, do you want to attack? A = yes, N = no ").upper()
							elif language == "cz":
								valka = input("musíš obsadit ještě " + str(obsadit) + " území. Na jedno území potřebuješ 2000 vojáků, chceš zaútočit? A = ano, N = ne ").upper()
							elif language == "de":
								valka = input("Sie müssen immer noch " + str(obsadit) + " Bereiche besetzen. Auf einem Gebiet muss man 2000 Soldaten haben, will man angreifen? A = ja, N = nein ").upper()
							if valka == 'A':
								if vojaci >= 2000:
									vojaci -= 2000
									obsadit -= 1
									if language == "en":
										print("You attacked! You have " + str(vojaci) + " soldiers left.")
									elif language == "cz":
										print("Zaútočil jsi! zbývá ti " + str(vojaci) + " vojáků.")
									elif language == "de":
										print("Du hast angegriffen! Sie haben " + str(vojaci) + " Soldaten übrig.")
								else:
									if language == "en":
										print("YOU DON'T HAVE ENOUGH SOLDIERS!\n")
									elif language == "cz":
										print("NEMÁŠ DOSTATEK VOJÁKŮ!\n")
									elif language == "de":
										print("DU HAST NICHT GENUG SOLDATEN!\n")
							elif valka == 'N':
								pass
							else:
								if language == "en":
									print("Wrong input!\n")
								elif language == "cz":
									print("Špatné zadání!\n")
								elif language == "de":
									print("Falsche Eingabe!\n")
						elif hra == 'B':
							if banka <= 3:
								if language == "en":
									bank = input("How much do you want to borrow? 1, 2, 3 mld? ")
								elif language == "cz":
									bank = input("Kolik si chceš půjčit? 1, 2, 3 mld? ")
								elif language == "de":
									bank = input("Wie viel möchten Sie leihen? 1, 2, 3 mld? ")
								if bank == "1":
									penize += 1
									banka += 2
									if language == "en":
										print("You debt is now at " + str(banka) + " mld.")
									elif language == "cz":
										print("Dluh v tento moment máš " + str(banka) + " mld.")
									elif language == "de":
										print("Ihre Schuld ist jetzt bei " + str(banka) + " mld.")
								elif bank == "2":
									penize += 2
									banka += 4
									if language == "en":
										print("You debt is now at " + str(banka) + " mld.")
									elif language == "cz":
										print("Dluh v tento moment máš " + str(banka) + " mld.")
									elif language == "de":
										print("Ihre Schuld ist jetzt bei " + str(banka) + " mld.")
								elif bank == "3":
									penize += 3
									banka += 6
									if language == "en":
										print("You debt is now at " + str(banka) + " mld.")
									elif language == "cz":
										print("Dluh v tento moment máš " + str(banka) + " mld.")
									elif language == "de":
										print("Ihre Schuld ist jetzt bei " + str(banka) + " mld.")
							else:
								if language == "en":
									print("You borrowed the maximum, you can!")
								elif language == "cz":
									print("Už sis půjčil maximum, co jde!")
								elif language == "de":
									print("Sie haben das Maximum geliehen, Sie können!")
						elif hra == "I":
							if language == "en":
								investice = input("How many do you want to invest?\n6 (+1 money per round)\n10 (+2 money per round): ")
							elif language == "cz":
								investice = input("Kolik chceš investovat?\n6 (+1 peníz za kolo)\n10 (+2 peníze za kolo): ")
							elif language == "de":
								investice = input("Wie viele möchten Sie investieren?\n6 (+1 Geld pro Runde)n10 (+2 Geld pro Runde): ")
							if investice == "6":
								if penize_za_kolo < 10 and obtiznost == "E":
									if penize >= 6:
										penize -= 6
										penize_za_kolo += 1
										if language == "en":
											print(str(penize_za_kolo) + " money per round")
										elif language == "cz":
											print(str(penize_za_kolo) + " peněz za kolo")
										elif language == "de":
											print(str(penize_za_kolo) + " Geld pro Runde")
									else:
										if language == "en":
											print("YOU DON'T HAVE ENOUGH MONEY!!\n")
										elif language == "cz":
											print("NEMÁŠ DOSTATEK FINANCÍ!!\n")
										elif language == "de":
											print("DU HAST NICHT GENUG GELD!!\n")
								elif penize_za_kolo < 5 and obtiznost in ["N", "H"]:
									if penize >= 6:
										penize -= 6
										penize_za_kolo += 1
										if language == "en":
											print(str(penize_za_kolo) + " money per round")
										elif language == "cz":
											print(str(penize_za_kolo) + " peněz za kolo")
										elif language == "de":
											print(str(penize_za_kolo) + " Geld pro Runde")
									else:
										if language == "en":
											print("YOU DON'T HAVE ENOUGH MONEY!!\n")
										elif language == "cz":
											print("NEMÁŠ DOSTATEK FINANCÍ!!\n")
										elif language == "de":
											print("DU HAST NICHT GENUG GELD!!\n")
								else:
									if language == "en":
										print("You've already invested too much money!")
									elif language == "cz":
										print("Už jsi investoval až moc peněz!")
									elif language == "de":
										print("Sie haben bereits zu viel Geld investiert!")
							elif investice == "10":
								if penize_za_kolo < 9 and obtiznost == "E":
									if penize >= 10:
										penize -= 10
										penize_za_kolo += 2
										if language == "en":
											print(str(penize_za_kolo) + " money per round")
										elif language == "cz":
											print(str(penize_za_kolo) + " peněz za kolo")
										elif language == "de":
											print(str(penize_za_kolo) + " Geld pro Runde")
									else:
										if language == "en":
											print("YOU DON'T HAVE ENOUGH MONEY!!\n")
										elif language == "cz":
											print("NEMÁŠ DOSTATEK FINANCÍ!!\n")
										elif language == "de":
											print("DU HAST NICHT GENUG GELD!!\n")
								elif penize_za_kolo < 4 and obtiznost in ["N", "H"]:
									if penize >= 10:
										penize -= 10
										penize_za_kolo += 2
										if language == "en":
											print(str(penize_za_kolo) + " money per round")
										elif language == "cz":
											print(str(penize_za_kolo) + " peněz za kolo")
										elif language == "de":
											print(str(penize_za_kolo) + " peněz za kolo")
									else:
										if language == "en":
											print("YOU DON'T HAVE ENOUGH MONEY!!\n")
										elif language == "cz":
											print("NEMÁŠ DOSTATEK FINANCÍ!!\n")
										elif language == "de":
											print("DU HAST NICHT GENUG GELD!!\n")
								else:
									if language == "en":
										print("You already invested too much money!")
									elif language == "cz":
										print("Už jsi investoval až moc peněz!")
									elif language == "de":
										print("Sie haben bereits zu viel Geld investiert!")
							else:
								if language == "en":
									print("This investment doesn't exist!\n")
								elif language == "cz":
									print("Taková investice není na výběr!\n")
								elif language == "de":
									print("Diese Investition gibt es nicht!\n")
						else:
							if language == "en":
								print("Wrong input!\n")
							elif language == "cz":
								print("Špatné zadání!\n")
							elif language == "de":
								print("Falsche Eingabe!\n")
				elif menu == 'N':
					if language == "en":
						print("That's a pitty :( Bye then!")
					elif language == "cz":
						print("To je škoda :( Tak ahoj! ")
					elif language == "de":
						print("Das ist eine erbärmliche :( Tschüss!")
					mixer.music.stop()
					os.system(clear)
					break
				else:
					if language == "en":
						print("Wrong input!\n")
					elif language == "cz":
						print("Špatné zadání!\n")
					elif language == "de":
						print("Falsche Eingabe!\n")
		elif game == "L":
			if language == "en":
				print("Leaderboards:")
			try:
				leaderboards_easy = {}
				leaderboards_normal = {}
				leaderboards_hard = {}
				with open("data11.txt", "r") as f:
					for line in f.readlines():
						data = line.rstrip()
						jmeno, zasifrovany_cas, zasifrovane_kolo, obtiznost = data.split("|")
						if obtiznost == "E":
							leaderboards_easy[jmeno] = [fer.decrypt(zasifrovany_cas).decode(), int(fer.decrypt(zasifrovane_kolo).decode())]
						elif obtiznost == "N":
							leaderboards_normal[jmeno] = [fer.decrypt(zasifrovany_cas).decode(), int(fer.decrypt(zasifrovane_kolo).decode())]
						elif obtiznost == "H":
							leaderboards_hard[jmeno] = [fer.decrypt(zasifrovany_cas).decode(), int(fer.decrypt(zasifrovane_kolo).decode())]
				leaderboards_easy = dict(sorted(leaderboards_easy.items(), key=lambda item: item[1][1]))
				leaderboards_normal = dict(sorted(leaderboards_normal.items(), key=lambda item: item[1][1]))
				leaderboards_hard = dict(sorted(leaderboards_hard.items(), key=lambda item: item[1][1]))
				nejdelsi_jmeno = ""
				for jmeno in leaderboards_easy.keys():
					if len(jmeno) > len(nejdelsi_jmeno):
						nejdelsi_jmeno = jmeno
				print(f"{Style.BRIGHT}EASY:{Style.RESET_ALL}\nName" + " "*(len(nejdelsi_jmeno) - 4) + "\tRound\tTime")

				for i, jmeno in enumerate(leaderboards_easy.keys()):
					print(f"{jmeno}" + " "*(len(nejdelsi_jmeno) - len(jmeno)) + f"\t{list(leaderboards_easy.values())[i][1]}\t{list(leaderboards_easy.values())[i][0]}")
				nejdelsi_jmeno = ""
				for jmeno in leaderboards_normal.keys():
					if len(jmeno) > len(nejdelsi_jmeno):
						nejdelsi_jmeno = jmeno
				print(f"{Style.BRIGHT}NORMAL:{Style.RESET_ALL}\nName" + " "*(len(nejdelsi_jmeno) - 4) + "\tRound\tTime")

				for i, jmeno in enumerate(leaderboards_normal.keys()):
					print(f"{jmeno}" + " "*(len(nejdelsi_jmeno) - len(jmeno)) + f"\t{list(leaderboards_normal.values())[i][1]}\t{list(leaderboards_normal.values())[i][0]}")
				nejdelsi_jmeno = ""
				for jmeno in leaderboards_normal.keys():
					if len(jmeno) > len(nejdelsi_jmeno):
						nejdelsi_jmeno = jmeno
				print(f"{Style.BRIGHT}HARD:{Style.RESET_ALL}\nName" + " "*(len(nejdelsi_jmeno) - 4) + "\tRound\tTime")

				for i, jmeno in enumerate(leaderboards_hard.keys()):
					print(f"{jmeno}" + " "*(len(nejdelsi_jmeno) - len(jmeno)) + f"\t{list(leaderboards_hard.values())[i][1]}\t{list(leaderboards_hard.values())[i][0]}")
			except FileNotFoundError:
				print("NEE!")
		elif game == "M":
			if language == "en":
				print(f"{Fore.YELLOW}WARNING: This is the multiplayer game, that insn't translated!\nBe sure, you know, what are you doing, or learn czech!{Fore.RESET}")
			elif language == "de":
				print(f"{Fore.YELLOW}WARNUNG: Dies ist das Multiplayer-Spiel, das nicht übersetzt ist!\nSeien Sie sicher, Sie wissen, was Sie tun, oder lernen Sie Tschechisch!{Fore.RESET}")
			while True:
				player1 = input("Zadejte jméno hráče 1: ")
				if player1 == "" or " " in player1:
					print(f"{Fore.RED}Musíte zadat jméno, ve jméně nesmí být mezera!{Fore.RESET}")
				else:
					break
			while True:
				player2 = input("Zadejte jméno hráče 2: ")
				if player2 == "" or " " in player2:
					print(f"{Fore.RED}Musíte zadat jméno, ve jméně nesmí být mezera!{Fore.RESET}")
				else:
					break
			mixer.music.load("kv_war_simulator_soundtrack.wav")
			mixer.music.play(-1)
			kolo = 1
			na_rade = 1
			utocil = False
			# Hráč 1
			penize1 = 2
			dluhy1 = 0
			vojaci1 = 2000
			uzemi1 = 20
			penize_za_kolo1 = 2
			
			# Hráč 2
			penize2 = 2
			dluhy2 = 0
			vojaci2 = 2000
			uzemi2 = 20
			penize_za_kolo2 = 2
			while True:
				# Kontrola
				if uzemi1 == 40 or uzemi2 == 40:
					mixer.music.load("teticka_song.wav")
					mixer.music.play(-1)
					print(f"Vyhrál jsi hru, pane {Style.BRIGHT}{player1}{Style.RESET_ALL}! Jsi dobrý!\nStiskni cokoli pro pokračování: " if uzemi1 == 40 else f"Vyhrál jsi hru, pane {Style.BRIGHT}{player2}{Style.RESET_ALL}! Jsi dobrý!\nStiskni cokoli pro pokračování: ", end="")
					input()
					mixer.music.stop()
					os.system(clear)
					break
				# Hra
				if na_rade == 1: print(f"{kolo}. KOLO!\nNa řadě je {Style.BRIGHT}{player1}{Style.RESET_ALL}!\n\n- Peněz: {penize1}\n- Vojáků: {vojaci1}\n- Dluh: {dluhy1}\n- Území: {uzemi1}\nK = Koupit vojáky, V = Válka, I = Investovat, B = Banka, D = Další kolo, E = Exit " if dluhy1 == 0 else f"{kolo}. KOLO!\nNa řadě je {Style.BRIGHT}{player1}{Style.RESET_ALL}!\n{Style.BRIGHT}{Fore.MAGENTA}Máte nezaplacené dluhy!{Style.RESET_ALL}\n\n- Peněz: {penize1}\n- Vojáků: {vojaci1}\n- Dluh: {dluhy1}\n- Území: {uzemi1}\nK = Koupit vojáky, V = Válka, I = Investovat, B = Banka, D = Další kolo, E = Exit ", end="")
				elif na_rade == 2: print(f"{kolo}. KOLO!\nNa řadě je {Style.BRIGHT}{player2}{Style.RESET_ALL}!\n\n- Peněz: {penize2}\n- Vojáků: {vojaci2}\n- Dluh: {dluhy2}\n- Území: {uzemi2}\nK = Koupit vojáky, V = Válka, I = Investovat, B = Banka, D = Další kolo, E = Exit " if dluhy2 == 0 else f"{kolo}. KOLO!\nNa řadě je {Style.BRIGHT}{player1}{Style.RESET_ALL}!\n{Style.BRIGHT}{Fore.MAGENTA}Máte nezaplacené dluhy!{Style.RESET_ALL}\n\n- Peněz: {penize2}\n- Vojáků: {vojaci2}\n- Dluh: {dluhy2}\n- Území: {uzemi2}\nK = Koupit vojáky, V = Válka, I = Investovat, B = Banka, D = Další kolo, E = Exit ", end="")
				start = input().upper()
				if start == "K":
					koupit = input("Kolik vojáků chceš koupit? 1000 vojáků stojí 1 peníz, Kupuj po 1000: ")
					try:
						koupit = int(koupit)
						if koupit % 1000 == 0:
							if na_rade == 1 and penize1 >= koupit // 1000:
								penize1 -= koupit // 1000
								vojaci1 += koupit
								print(f"{Fore.GREEN}Úspěšně jsi koupil vojáky!{Fore.RESET}")
							elif na_rade == 1 and penize1 < koupit // 1000:
								print(f"{Fore.RED}Nemáš dostatek peněz na koupení tohoto počtu vojáků!{Fore.RESET}")
							elif na_rade == 2 and penize2 >= koupit // 1000:
								penize2 -= koupit // 1000
								vojaci2 += koupit
								print(f"{Fore.GREEN}Úspěšně jsi koupil vojáky!{Fore.RESET}")
							elif na_rade == 2 and penize2 < koupit // 1000:
								print(f"{Fore.RED}Nemáš dostatek peněz na koupení tohoto počtu vojáků!{Fore.RESET}")
						else:
							print(f"{Style.BRIGHT}{Fore.RED}Kupuj vojáky po tisících, např. 1000, 2000, 3000, atd.!{Style.RESET_ALL}")
					except ValueError:
						print(f"{Fore.LIGHTBLACK_EX}Toto není číslo!{Fore.RESET}")
				elif start == "V":
					if utocil:
						print(f"{Fore.RED}Toto kolo jsi již útočil!{Fore.RESET}")
						continue
					while True:
						pocet_do_utoku = input(f"Vašemu protihráči zbývá {uzemi2} území. Kolika vojáky chcete zaútočit? Q = Quit: " if na_rade == 1 else f"Vašemu protihráči zbývá {uzemi1} území. Kolika vojáky chcete zaútočit? Q = Quit: ")
						if pocet_do_utoku.upper() == "Q":
							break
						try:
							pocet_do_utoku = int(pocet_do_utoku)
							if pocet_do_utoku % 1000 != 0:
								print(f"{Style.BRIGHT}{Fore.RED}Posílejte vojáky po 1000!{Style.RESET_ALL}")
							elif na_rade == 1 and pocet_do_utoku <= vojaci1:
								if pocet_do_utoku > vojaci2:
									zbytky = pocet_do_utoku - vojaci2
									vojaci1 -= pocet_do_utoku
									vojaci1 += zbytky
									uzemi2 -= 1
									uzemi1 += 1
									vojaci2 = 0

									print(f"Porazil jsi armádu hráče {Fore.RED}{player2}{Fore.RESET}, vrátilo se ti {Fore.YELLOW}{zbytky}{Fore.RESET} vojáků!")
									utocil = True
									break
								elif pocet_do_utoku < vojaci2:
									vojaci1 -= pocet_do_utoku
									vojaci2 -= pocet_do_utoku
									print(f"Tvoje armáda bohužel neporazila armádu hráče {Fore.RED}{player2}{Fore.RESET}!")
									utocil = True
									break
								else:
									vojaci1 -= pocet_do_utoku
									vojaci2 -= pocet_do_utoku
									print(f"S hráčem {Fore.RED}{player2}{Fore.RESET} dopadla bitva {Fore.YELLOW}remízou{Fore.RESET}!")
									utocil = True
									break
								
							elif na_rade == 1 and pocet_do_utoku > vojaci1:
								print(f"Tolik vojáků nemáš!")
							elif na_rade == 2 and pocet_do_utoku <= vojaci2:
								if pocet_do_utoku > vojaci1:
									zbytky = pocet_do_utoku - vojaci1
									vojaci2 -= pocet_do_utoku
									vojaci2 += zbytky
									uzemi1 -= 1
									uzemi2 += 1
									vojaci1 = 0
									
									print(f"Porazil jsi armádu hráče {Fore.RED}{player1}{Fore.RESET}, vrátilo se ti {Fore.YELLOW}{zbytky}{Fore.RESET} vojáků!")
									utocil = True
									break
								elif pocet_do_utoku < vojaci1:
									vojaci2 -= pocet_do_utoku
									vojaci1 -= pocet_do_utoku
									print(f"Tvoje armáda bohužel neporazila armádu hráče {Fore.RED}{player1}{Fore.RESET}!")
									utocil = True
									break
								else:
									vojaci2 -= pocet_do_utoku
									vojaci1 -= pocet_do_utoku
									print(f"S hráčem {Fore.RED}{player1}{Fore.RESET} dopadla bitva {Fore.YELLOW}remízou{Fore.RESET}!")
									utocil = True
									break

							elif na_rade == 2 and pocet_do_utoku > vojaci2:
								print(f"Tolik vojáků nemáš!")
						except ValueError:
							print(f"{Fore.LIGHTBLACK_EX}Toto není číslo!{Fore.RESET}")
				elif start == "I":
					investice = input(f"Vyděláváš {penize_za_kolo1} peněz za kolo\n6 peněz (1 peníz za kolo)\n10 peněz (2 peníze za kolo): " if na_rade == 1 else f"Vyděláváš {penize_za_kolo2} peněz za kolo\n6 peněz (1 peníz za kolo)\n10 peněz (2 peníze za kolo): ")
					if investice == "6" or investice == "10":
						if na_rade == 1 and penize1 >= int(investice):
							penize1 -= int(investice)
							if int(investice) == 6 and penize_za_kolo1 < 10:
								penize_za_kolo1 += 1
							elif int(investice) == 10 and penize_za_kolo1 < 9:
								penize_za_kolo1 += 2
							else:
								print(f"{Style.BRIGHT}{Fore.RED}Už nemůžeš investovat tolik peněz!{Style.RESET_ALL}")
						elif na_rade == 1 and penize1 < int(investice):
							print(f"{Fore.RED}Nemáš dostatek financí!{Fore.RESET}")
						elif na_rade == 2 and penize2 >= int(investice):
							penize2 -= int(investice)
							if int(investice) == 6 and penize_za_kolo2 < 10:
								penize_za_kolo2 += 1
							elif int(investice) == 10 and penize_za_kolo2 < 9:
								penize_za_kolo2 += 2
							else:
								print(f"{Style.BRIGHT}{Fore.RED}Už nemůžeš investovat tolik peněz!{Style.RESET_ALL}")
						elif na_rade == 2 and penize2 < int(investice):
							print(f"{Fore.RED}Nemáš dostatek financí!{Fore.RESET}")
					else:
						try:
							investice = int(investice)
							print(f"{Fore.RED}Taková investice není na výběr!{Fore.RESET}")
						except ValueError:
							print(f"{Fore.LIGHTBLACK_EX}Toto není číslo!{Fore.RESET}")
				elif start == "B":
					if (na_rade == 1 and penize1 >= 0) or (na_rade == 2 and penize2 >= 0):
						pujcit = input("Kolik peněz chceš půjčit? Úrok je 100 % (např. když si půjčíte 2 peníze, úrok je 4 peníze).\nMaximálně si můžete půjčit 10 peněz: ")
					else:
						print(f"{Style.BRIGHT}{Fore.RED}Nemůžeš si půjčit, když jsi v mínusu!{Style.RESET_ALL}")
						continue
					try:
						pujcit = int(pujcit)
						if na_rade == 1 and pujcit + dluhy1 / 2 <= 10:
							penize1 += pujcit
							dluhy1 += pujcit * 2
							print(f"{Fore.GREEN}Úspěšně sis půjčil {pujcit} peněz!{Fore.RESET}")
						elif na_rade == 2 and pujcit + dluhy2 / 2 <= 10:
							penize2 += pujcit
							dluhy2 += pujcit * 2
							print(f"{Fore.GREEN}Úspěšně sis půjčil {pujcit} peněz!{Fore.RESET}")
						else:
							print(f"{Fore.RED}Tolik si již nemůžeš půjčit!{Fore.RESET}")
					except ValueError:
						print(f"{Fore.LIGHTBLACK_EX}Toto není číslo!{Fore.RESET}")
				elif start == "D":
					if na_rade == 1:
						na_rade = 2
					else:
						kolo += 1
						penize1 += penize_za_kolo1
						penize2 += penize_za_kolo2
						na_rade = 1
						if dluhy1 > 0:
							penize1 -= dluhy1
							dluhy1 = 0
						elif dluhy2 > 0:
							penize2 -= dluhy2
							dluhy2 = 0
					utocil = False
				elif start == "E":
					mixer.music.stop()
					os.system(clear)
					break
				else:
					print("Špatné zadání!\n")
		elif game == "L":
			# Otevřít links_beta.py
			try:
				exec(open("links_beta.py", encoding="utf-8").read()	)
			except FileNotFoundError:
				print(f"{Fore.LIGHTRED_EX}Soubor \"{Fore.RED}links_beta.py{Fore.LIGHTRED_EX}\" nebyl nalezen.\nStáhněte si ho přes KV stránky (sekce KV Linky) a vložte ho do složky KV_OS 1.1.{Fore.RESET}")
	elif home == "P":
		promenne = {}
		while True:
			prg = input(">>> ")
			if prg == "write()":
				write = input(">>>> ")
				print(write)
			elif prg == "write(dfn)":
				write_var = input(">>>> ")
				if write_var in promenne:
					print(promenne.get(write_var))
				else:
					print(f"{Fore.RED}This isn't a variable!{Fore.RESET}")
			elif prg.startswith("write(\"") and prg.endswith("\")"):
				novy_write = prg.split("write(\"", maxsplit=1)[1].split("\")")[0]
				if "\"" in novy_write:
					print(f"{Fore.RED}You can't have \" in your text!{Fore.RESET}")
				else:
					print(novy_write)
			elif prg.startswith("write(") and not prg.startswith("write(\"") and prg.endswith(")") and not prg.endswith("\")"):
				w_dfn = prg.split("write(", maxsplit=1)[1].split(")")[0]
				if w_dfn in promenne:
					print(promenne.get(w_dfn))
				else:
					print(f"{Fore.RED}This isn't a variable!{Fore.RESET}")
			elif prg == "dfn()":
				dfn = input(">>>> ")
				dfn_jako = input("= ")
				promenne[dfn] = dfn_jako
			elif prg == "dfn(show)":
				for promenna in promenne:
					print(f"{promenna} = {promenne.get(promenna)}")
			elif prg.startswith("dfn(") and prg.endswith(")") and " = " in prg and prg != "dfn()":
				novy_dfn = prg.split("dfn(", maxsplit=1)[1].split(" = ", maxsplit=1)
				promenne[novy_dfn[0]] = novy_dfn[1][:-1]
			elif prg == "while true":
				kolo = input(">>>> ")
				ready = input("If you are ready, press B: ").upper()
				if ready == "B":
					while True:
						print(kolo)
				else:
					print("Another key!")
			elif prg == "cls" or prg == "clear":
				os.system(clear)
			elif prg == "exit" or prg == "exit()":
				os.system(clear)
				break
			else:
				print("Another key!")
	elif home == "N":
		if language == "en":
			print(f"""\
0.2 BETA UPDATE:
  • We added new KV OS function called Patch notes
  • We added new KV script function dfn()
  • You can put your input in lower or upper characters
  • We changed some texts
0.3 BETA UPDATE:
  • We created the login fuction
0.3 BUG REPORT UPDATE:
  • Shutdown function is now fixed
0.4 BETA UPDATE:
  • We fixed bug, where any incorrect input turn off the OS
  • You can finally use function dfn() for some reasons:
    - You can write your variables with function write(dfn)
    - You can write all your variables with function dfn(show)
0.5 BETA UPDATE:
  • Function write() has got a new update:
    - write("Hello!") should write "Hello!" to the console
  • We remake the login system (data is in file data05.txt)
  • We aded an options menu:
    - In the options menu you can change the language
0.6 BETA UPDATE
  • We added a game for Czech
0.7 BETA UPDATE:
  • We fixed some bugs in the game (textova_hra.py):
    - 0 money bug in investing is now fixed
    - Bank is now fixed
    - If you die, you can see why
    - If you exit the game, you will go to menu
  • We rewrote the write("*") system
  • We added some {Style.BRIGHT}{Fore.YELLOW}colors{Style.RESET_ALL} to the OS
  • You can now use dfn(something = something) like that
0.7 BUG REPORT UPDATE:
  • Bank in the game is no longer OP
0.8 BETA UPDATE:
  • We fixed a bug, where in any windows cmd colors didn't work
  • In the game, you can now choose a difficulty
  • We encrypted the login system
0.8 SHUTDOWN UPDATE:
  • No spamming shutdown screen
0.8 SONG & COLOR UPDATE:
  • There is no longer problems with colors in Windows' and Mac's terminal
  • We added the soundtrack to the game
0.9 BETA UPDATE:
  • We updated the song in the game
  • You can't write " to your text in programming
  • You can write syntax write(*some_variable*), this will write a variable, if exists
  • We finally completed the multiplayer to the game
1.0 UPDATE
  • We fixed the bug, where you could register as "|" and then OS crashed
  • We upgraded the old version of buying soldiers in the singleplayer. Now, you can buy any number of soldiers (per 1000)
  • We finally translated the game in Singleplayer
  • When you win, Tetička song will play
  • You can't have spaces in your username now
  • You can't have spaces in the multiplayer now
  • The system can now clear the behind text
  • We added clear function to the programming
  • We've re-written the logic of all the strings in the multiplayer
PRESS ANY KEY TO CONTINUE: """, end="")
		elif language == "cz":
			print(f"""\
0.2 BETA AKTUALIZACE:
  • Přidali jsme novou KV OS funkci, která se jmenuje Novinky
  • Přidali jsme novou KV script funkci dfn()
  • Můžete psát velkým i malým písmenem
  • Změnili jsme texty
0.3 BETA AKTUALIZACE:
  • Vytvořili jsme přihlašovací systém
0.3 BUG REPORT:
  • Vypnutí již funguje
0.4 BETA AKTUALIZACE:
  • Opravili jsme chybu, kdy každý špatný input vypnul OS
  • Konečně máte proč využít dfn() funkci:
    - Můžete napsat proměnnou pomocí write(dfn)
    - Můžete zobrazit všechny vaše proměnné pomocí dfn(show)
0.5 BETA AKTUALIZACE:
  • Funkce write() dostala novou aktualizaci:
    - write("Ahoj!") by mělo napsat "Ahoj!" do konzole
  • Předělali jsme přihlašovací systém (data jsou ve složce data05.txt)
  • Přidali jsme options menu:
    - Můžete si vybrat jazyk
0.6 BETA AKTUALIZACE:
  • Přidali jsme hru pro češtinu
0.7 BETA AKTUALIZACE:
  • Opravili jsme nějaké chyby ve hře (textova_hra.py):
    - 0 peněz chyba v investování byla opravena
    - Banka byla opravena
    - Když umřete, uvidíte proč
    - Když opustíte hru, vrátíte se do menu
  • Předělali jsme write("*") systém
  • Přidali jsme {Style.BRIGHT}{Fore.YELLOW}barvy{Style.RESET_ALL} do OS
  • Už můžete napsat dfn(něco = něco) přesně takto
0.7 BUG REPORT:
  • Banka v této hře už není OP
0.8 BETA AKTUALIZACE:
  • Opravili jsme chybu, kde na jakémkoliv Windows cmd nefungovaly barvy
  • Ve hře si můžete změnit obtížnost
  • Zašifrovali jsme přihlašovací systém
0.8 VYPÍNACÍ AKTUALIZACE:
  • Nespamovací obrazovka při vypnutí
0.8 HUDEBNÍ A BAREVNÁ AKTUALIZACE:
  • Odebrali jsme problémy s barvami na Windows a Mac terminálu
  • Přidali jsme hudební podklad do hry
0.9 BETA AKTUALIZACE:
  • Zlepšili jsme hudbu ve hře
  • Nemůžete napsat " do vašeho textu v programování
  • Můžete mapsat syntaxi write(*nějaká_proměnná*), to vám napíše proměnnou, pokud existuje
  • Konečně jsme dokončili multiplayer do hry
1.0 AKTUALIZACE
  • Opravili jsme bug, kde jste se mohli registrovat jako "|" a poté OS přestal pracovat
  • Ve hře jsme zlepšili starý systém kupování vojáků, můžete tedy koupit jakékoli množství vojáků (po 1000)
  • Konečně jsme přeložili hru v Singleplayeru
  • Když vyhrajete, spustí se Tetička song
  • Od teď ve vašem jméně nesmí být mezery!
  • Od teď v multiplayeru nesmí být mezery ve jménech!
  • Systém teď může mazat zbylý zadní text
  • Přidali jsme funkci pro mazání
  • Přepsali jsme logiku textu v Multiplayeru
POKRAČUJTE STISKEM LIBOVOLNÉ KLÁVESY: """, end="")
		elif language == "de":
			print(f"""\
0.2 BETA-UPDATE:
   • Wir haben eine neue KV OS-Funktion namens Patchnotes hinzugefügt
   • Wir haben die neue KV-Skriptfunktion dfn() hinzugefügt
   • Sie können Ihre Eingabe in Klein- oder Großbuchstaben eingeben
   • Wir haben einige Texte geändert
0.3 BETA-UPDATE:
   • Wir haben die Login-Funktion erstellt
0.3 AKTUALISIERUNG DES FEHLERBERICHTS:
   • Shutdown-Funktion ist jetzt behoben
0.4 BETA-UPDATE:
   • Wir haben einen Fehler behoben, bei dem jede falsche Eingabe das Betriebssystem ausschaltet
   • Sie können endlich die Funktion dfn() aus einigen Gründen verwenden:
     - Sie können Ihre Variablen mit der Funktion write(dfn) schreiben
     - Sie können alle Ihre Variablen mit der Funktion dfn(show) schreiben
0.5 BETA-UPDATE:
   • Funktion write() hat ein neues Update bekommen:
     - write("Hallo!") sollte "Hallo!" schreiben. zur Konsole
   • Wir machen das Login-System neu (Daten sind in der Datei data05.txt)
   • Wir haben ein Optionsmenü hinzugefügt:
     - Im Optionsmenü können Sie die Sprache ändern
0.6 BETA-UPDATE:
  • Wir haben ein Spiel für Tschechisch hinzugefügt
0.7 BETA-UPDATE:
  • Wir haben einige Fehler im Spiel behoben (textova_hra.py):
    - 0 Geldfehler beim Investieren ist jetzt behoben
    - Bank ist jetzt repariert
    - Wenn du stirbst, kannst du sehen warum
    - Wenn Sie das Spiel verlassen, gelangen Sie zum Menü
  • Wir haben das write("*")-System umgeschrieben
  • Wir haben einige {Style.BRIGHT}{Fore.YELLOW}Farben{Style.RESET_ALL} zum Betriebssystem hinzugefügt
  • Sie können dfn(etwas = etwas) jetzt so verwenden
0.7 AKTUALISIERUNG DES FEHLERBERICHTS:
  • Bank im Spiel ist nicht mehr OP
0.8 BETA-UPDATE:
  • Wir haben einen Fehler behoben, bei dem in allen Windows cmd Farben nicht funktionierten
  • Im Spiel können Sie jetzt einen Schwierigkeitsgrad auswählen
  • Wir haben das Login-System verschlüsselt
0.8 AKTUALISIERUNG DES HERUNTERFAHRENS:
  • kein Spam-Shutdown-Bildschirm
0.8 SONG UND FARB-UPDATE:
  • Es gibt keine Probleme mehr mit Farben im Windows- und Mac-Terminal
  • Wir haben den Soundtrack zum Spiel hinzugefügt
0.9 BETA-UPDATE:
  • Wir haben den Song im Spiel aktualisiert
  • Sie können in der Programmierung nicht " zu Ihrem Text schreiben
  • Sie können die Syntax write(*etwas_variabel*) schreiben, dies schreibt eine Variable, falls vorhanden
  • Wir haben endlich den Multiplayer zum Spiel abgeschlossen
1.0 UPDATE
  • Wir haben den Fehler behoben, bei dem Sie sich als "|" registrieren konnten. und dann stürzte das Betriebssystem ab
  • Wir haben die alte Version des Soldatenkaufs aktualisiert. Jetzt können Sie eine beliebige Anzahl von Soldaten (pro 1000) kaufen
  • Wir haben das Spiel schließlich in Singleplayer übersetzt
  • Wenn Sie gewinnen, wird das Tetička-Lied gespielt
  • Sie können jetzt keine Leerzeichen in Ihrem Benutzernamen haben
  • Sie können jetzt keine Leerzeichen im Multiplayer haben
  • Das System kann nun den Hintertext löschen
  • Wir haben der Programmierung eine klare Funktion hinzugefügt
  • Wir haben alle Saiten im Multiplayer neu geschrieben
DRÜCKEN SIE EINE BELIEBIGE TASTE, UM FORTZUFAHREN: """, end="")
		input()
		os.system(clear)
	elif home == "E":
		if language == "en":
			print("Shutdowning, wait a minute please...")
		elif language == "cz":
			print("Vypínám, počkejte...")
		elif language == "de":
			print("Herunterfahren, warten Sie bitte eine Minute...")
		u = 1
		while True:
			u += 1
			if u == 80000000:
				if language == "en":
					print("bye")
				elif language == "cz":
					print("ahoj")
				elif language == "de":
					print("auf wiedersehen")
				exit()
	elif home == "R" and user == None:
		w_username = input("Username: ")
		if w_username == "":
			if language == "en":
				print(f"{Fore.RED}Something went wrong... Your username can't be empty!\n{Fore.RESET}")
			elif language == "cz":
				print(f"{Fore.RED}Něco dopadlo špatně...Vaše užvatelské jméno nesmí být prázdné!\n{Fore.RESET}")
			elif language == "de":
				print(f"{Fore.RED}Etwas ist schief gelaufen... Dein Benutzername darf nicht leer sein!\n{Fore.RESET}")
			continue
		elif " " in w_username:
			if language == "en":
				print(f"{Fore.RED}Something went wrong... You can't have spaces in your username!\n{Fore.RESET}")
			elif language == "cz":
				print(f"{Fore.RED}Něco dopadlo špatně... Nesmíte mít mezery ve vašem jméně!\n{Fore.RESET}")
			elif language == "de":
				print(f"{Fore.RED}Etwas ist schief gelaufen... Du darfst keine Leerzeichen in deinem Benutzernamen haben!\n{Fore.RESET}")
			continue
		w_password = input("Password: ")
		os.system(clear)
		if w_password == "":
			if language == "en":
				print(f"{Fore.RED}Something went wrong... Your password can't be empty!\n{Fore.RESET}")
			elif language == "cz":
				print(f"{Fore.RED}Něco dopadlo špatně...Vaše heslo nesmí být prázdné!\n{Fore.RESET}")
			elif language == "de":
				print(f"{Fore.RED}Etwas ist schief gelaufen... Ihr Passwort darf nicht leer sein!\n{Fore.RESET}")
			continue
		try:
			if ("|" not in w_username) and ("|" not in w_password):
				with open('data05.txt', 'a') as f:
					f.write(w_username + "|" + fer.encrypt(w_password.encode()).decode() + "\n")
			else:
				if language == "en":
					print(f"{Fore.RED}Something went wrong... Please, try it again with another characters!\n{Fore.RESET}")
				elif language == "cz":
					print(f"{Fore.RED}Něco dopadlo špatně...Prosím, zkuste to s jinými písmeny!\n{Fore.RESET}")
				elif language == "de":
					print(f"{Fore.RED}Etwas ist schief gelaufen... Bitte versuchen Sie es erneut mit einem anderen Zeichen!\n{Fore.RESET}")
		except:
			if language == "en":
				print(f"{Fore.RED}Something went wrong... Please, try it again with another characters!\n{Fore.RESET}")
			elif language == "cz":
				print(f"{Fore.RED}Něco dopadlo špatně...Prosím, zkuste to s jinými písmeny!\n{Fore.RESET}")
			elif language == "de":
				print(f"{Fore.RED}Etwas ist schief gelaufen... Bitte versuchen Sie es erneut mit einem anderen Zeichen!\n{Fore.RESET}")
	elif home == "L" and user == None:
		try:
			with open('data05.txt', 'r') as f:
				asi_username = input("Username: ")
				asi_password = input("Password: ")
				os.system(clear)
				for line in f.readlines():
					data = line.rstrip()
					username, zasifrovany_password = data.split("|")
					password = fer.decrypt(zasifrovany_password.encode()).decode()
					if asi_username == username and asi_password == password:
						user = username
						if language == "en":
							print(f"You are now log in as {user}!\n")
						elif language == "cz":
							print(f"Jste přihlášeni jako {user}!\n")
						elif language == "de":
							print(f"Sie sind nun eingeloggt als {user}!\n")
						break
		except FileNotFoundError:
			if language == "en":
				print(f"You haven't got any accounts yet, please, register!\n")
			elif language == "cz":
				print("Nemáte zatím žádné účty, prosím, zaregistrujte se!\n")
			elif language == "de":
				print("Sie haben noch keine Konten, bitte registrieren Sie sich!\n")
	elif home == "L" and user != None:
		user = None
		if language == "en":
			print("You are now log out!\n")
		elif language == "cz":
			print("Jste odhlášeni!\n")
		elif language == "de":
			print("Sie sind nun abgemeldet!\n")
	elif home == "O":
		while True:
			if language == "en":
				nastaveni = input("What do you like to change? L = Language, Q = Go to menu: ").upper()
			elif language == "cz":
				nastaveni = input("Co byste chtěli změnit? L = Jazyk, Q = Jít do menu: ").upper()
			elif language == "de":
				nastaveni = input("Was möchten Sie ändern? L = Sprache, Q = Gehe zum Menü: ").upper()
			os.system(clear)
			if nastaveni == "L":
				while True:
					if language == "en":
						jazykovy_vyber = input("What language would you like?\nCZ = Czech\nEN = English\nDE = Deutsch: ").upper()
					elif language == "cz":
						jazykovy_vyber = input("Jaký jazyk byste chtěli?\nCZ = Český\nEN = Anglický\nDE = Německy: ").upper()
					elif language == "de":
						jazykovy_vyber = input("Welche Sprache möchten Sie?\nCZ = Tschechisch\nEN = Englisch\nDE = Deutsch: ").upper()
					os.system(clear)
					if jazykovy_vyber == "CZ":
						if language != "cz":
							language = "cz"
							print("Úspěšně změněno!\n")
							break
						else:
							print("Tento jazyk už máš vybraný!\n")
							break
					elif jazykovy_vyber == "EN":
						if language != "en":
							language = "en"
							print("Successfully changed!\n")
							break
						else:
							print("You already chose that language!\n")
							break
					elif jazykovy_vyber == "DE":
						if language != "de":
							language = "de"
							print("Erfolgreich geändert!\n")
							break
						else:
							print("Sie haben diese Sprache bereits gewählt!\n")
							break
			elif nastaveni == "Q":
				break
	elif home == "A":
		print("AAA")
