from colorama import init, Fore, Style
from cryptography.fernet import Fernet
from pygame import mixer
mixer.init()
init()

promenne = {}
user = None
language = "en"
#je to beta případné problémy nebo bugy hlaste na kv support team nebo vývojářům
print(f"{Fore.GREEN}KV system 0.8 (beta)\n©1995 - 2021 ALL RIGHTS RESERVED!{Fore.RESET}\n")
while True:
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
	if user == None:
		if language == "en":
			print(f"\n{Fore.RED}YOU ARE NOT LOGGED IN!{Style.RESET_ALL}")
		elif language == "cz":
			print(f"\n{Fore.RED}NEJSTE PŘIHLÁŠENI!{Style.RESET_ALL}")
		elif language == "de":
			print(f"\n{Fore.RED}DU BIST NICHT EINGELOGGT!{Style.RESET_ALL}")
		if language == "en":
			print(f"G = Game\nP = Programming in KV script beta\nN = Patch notes\n{Fore.CYAN}R = Register\nL = Login{Fore.RESET}\nO = Options\nE = Shotdown: ", end="")
			home = input().upper()
		elif language == "cz":
			print(f"G = Hra\nP = Programování v KV scriptu beta\nN = Novinky\n{Fore.CYAN}R = Registrovat se\nL = Přihlásit se{Fore.RESET}\nO = Nastavení\nE = Vypnout: ", end="")
			home = input().upper()
		elif language == "de":
			print(f"G = Spiel\nP = Programmierung in KV-Skript-Beta\nN = Patchnotizen\n{Fore.CYAN}R = Registrieren\nL = Anmelden {Fore.RESET}\nO = Optionen\nE = Herunterfahren: ", end="")
			home = input().upper()
	else:
		if language == "en":
			print(f"\n{Style.BRIGHT}{Fore.YELLOW}You are now log in as {user}!{Style.RESET_ALL}")
		elif language == "cz":
			print(f"\n{Style.BRIGHT}{Fore.YELLOW}Jsi přihlášen jako {user}!{Style.RESET_ALL}")
		elif language == "de":
			print(f"\n{Style.BRIGHT}{Fore.YELLOW}Sie sind jetzt angemeldet als {user}!{Style.RESET_ALL}")
		if language == "en":
			home = input("G = Game\nP = Programming in KV script beta\nN = Patch notes\nL = Logout\nO = Options\nE = Shotdown: ").upper()
		elif language == "cz":
			home = input("G = Hra\nP = Programování v KV scriptu beta\nN = Novinky\nL = Odhlásit se\nO = Nastavení\nE = Vypnout: ").upper()
		elif language == "de":
			home = input("G = Spiel\nP = Programmierung in KV-Skript-Beta\nN = Patchnotizen\nL = Abmelden\nO = Optionen\nE = Herunterfahren: ").upper()
	if home == "G":
		if language == "en":
			game = input("__________________\n      game       \n__________________\nprocesing...\npress S = Singleplayer\n      M = Multiplayer: ").upper()
		elif language == "cz":
			game = input("__________________\n      hra       \n__________________\nnačítání...\nstiskněte S = Singleplayer\n          M = Multiplayer: ").upper()
		elif language == "de":
			game = input("__________________\n      Spiel       \n__________________\nWird geladen...\ndrücke S = Singleplayer\n       M = Multiplayer: ").upper()
		if game == "S":
			obtiznost = None
			if language == "en":
				print(f"{Fore.RED}Game is only in czech!{Fore.RESET}")
			elif language == "cz":
				while True:
					obtiznost = input("Na jakou chceš hrát ontížnost?\nE = Easy\nN = Normal\nH = Hard: ").upper()
					if obtiznost == "E":
						input("""\
EASY obtížnost
- Začínáte s 3 mld. penězi
- Začínáte s 2000 vojáky
- Dokud neinvestujete, získáváte 2 mld. peněz za kolo
- Chcete-li vyhrát, musíte získat 25 území
- Investovat můžete do 10 peněz za kolo
- Invaze do vaší země se konají každých 10 kol
- Invaze jsou vždy po 1000 vojácích
Jakoukoli klávesou pokračujte: """)
						break
					elif obtiznost == "N":
						input("""\
NORMAL obtížnost
- Začínáte s 3 mld. penězi
- Nezačínáte s žádnými vojáky
- Dokud neinvestujete, získáváte 2 mld. peněz za kolo
- Chcete-li vyhrát, musíte získat 50 území
- Investovat můžete do 5 peněz za kolo
- Invaze do vaší země se konají každých 5 kol
- Invaze jsou vždy po 1000 vojácích
Jakoukoli klávesou pokračujte: """)
						break
					elif obtiznost == "H":
						input("""\
HARD obtížnost
- Nezačínáte s žádnými penězi
- Nezačínáte s žádnými vojáky
- Dokud neinvestujete, získáváte 2 mld. peněz za kolo
- Chcete-li vyhrát, musíte získat 75 území
- Investovat můžete do 5 peněz za kolo
- Invaze do vaší země se konají každých 5 kol
- Invaze jsou vždy po 2000 vojácích
Jakoukoli klávesou pokračujte: """)
						break
					else:
						obtiznost = ""
						print("Another key!")
				penize = None
				if obtiznost == "H":
					penize = 0
				else:
					penize = 3
				vojaci = None
				if obtiznost == "E":
					vojaci = 2000
				else:
					vojaci = 0
				kola = 1
				obsadit = None
				if obtiznost == "E":
					obsadit = 30
				elif obtiznost == "N":
					obsadit = 55
				elif obtiznost == "H":
					obsadit = 70
				banka = 0
				penize_za_kolo = 2
				mixer.music.load("kv_war_simulator_soundtrack.wav")
				mixer.music.play(-1)
				print(f"{Fore.YELLOW}Toto je vylepšená verze hry textova_hra.py. Jestli chcete mít zážitek ze hry textova_hra, jako takový, stáhněte si KV OS BETA 0.6{Fore.RESET}")
				while True:
					menu = input("Vítej, cheš hrát tuto hru? A = ano N = ne: ")
					if menu == 'A':
						while True:
							if obsadit == 0:
								print('GRATULACE!!! Dohrál jsi hru!! Jsi dobrý!!')
								break
							elif kola == 5 and obtiznost in ["N", "H"]:
								if vojaci >= 1000 and obtiznost in ["E", "N"]:
									vojaci -= 1000
									print('Zaútočili na tebe! Nově máš ' + str(vojaci) + ' vojáků!')
									kola += 1
								elif vojaci >= 2000 and obtiznost == "H":
									vojaci -= 2000
									print('Zaútočili na tebe! Nově máš ' + str(vojaci) + ' vojáků!')
									kola += 1
								else:
									print('Zaútočili na tebe, nemáš dostatek vojáků na protiútok\nGAME OVER')
									break
							elif kola == 10:
								if vojaci >= 1000 and obtiznost in ["E", "N"]:
									vojaci -= 1000
									print('Zaútočili na tebe! Nově máš ' + str(vojaci) + ' vojáků!')
									kola += 1
								elif vojaci >= 2000 and obtiznost == "H":
									vojaci -= 2000
									print('Zaútočili na tebe! Nově máš ' + str(vojaci) + ' vojáků!')
									kola += 1
								else:
									print('Zaútočili na tebe, nemáš dostatek vojáků na protiútok\nGAME OVER')
									break
							elif kola == 15 and obtiznost in ["N", "H"]:
								if vojaci >= 1000 and obtiznost == "N":
									vojaci -= 1000
									print('Zaútočili na tebe! Nově máš ' + str(vojaci) + ' vojáků!')
									kola += 1
								elif vojaci >= 2000 and obtiznost == "H":
									vojaci -= 2000
									print('Zaútočili na tebe! Nově máš ' + str(vojaci) + ' vojáků!')
									kola += 1
								else:
									print('Zaútočili na tebe, nemáš dostatek vojáků na protiútok\nGAME OVER')
									break
							elif kola == 20:
								if vojaci >= 1000 and obtiznost in ["E", "N"]:
									vojaci -= 1000
									print('Zaútočili na tebe! Nově máš ' + str(vojaci) + ' vojáků!')
									kola += 1
								elif vojaci >= 2000 and obtiznost == "H":
									vojaci -= 2000
									print('Zaútočili na tebe! Nově máš ' + str(vojaci) + ' vojáků!')
									kola += 1
								else:
									print('Zaútočili na tebe, nemáš dostatek vojáků na protiútok\nGAME OVER')
									break
							elif kola == 25 and obtiznost in ["N", "H"]:
								if vojaci >= 1000 and obtiznost == "N":
									vojaci -= 1000
									print('Zaútočili na tebe! Nově máš ' + str(vojaci) + ' vojáků!')
									kola += 1
								elif vojaci >= 2000 and obtiznost == "H":
									vojaci -= 2000
									print('Zaútočili na tebe! Nově máš ' + str(vojaci) + ' vojáků!')
									kola += 1
								else:
									print('Zaútočili na tebe, nemáš dostatek vojáků na protiútok\nGAME OVER')
									break
							elif kola == 30:
								if vojaci >= 1000 and obtiznost in ["E", "N"]:
									vojaci -= 1000
									print('Zaútočili na tebe! Nově máš ' + str(vojaci) + ' vojáků!')
									kola += 1
								elif vojaci >= 2000 and obtiznost == "H":
									vojaci -= 2000
									print('Zaútočili na tebe! Nově máš ' + str(vojaci) + ' vojáků!')
									kola += 1
								else:
									print('Zaútočili na tebe, nemáš dostatek vojáků na protiútok\nGAME OVER')
									break
							elif kola == 35 and obtiznost in ["N", "H"]:
								if vojaci >= 1000 and obtiznost == "N":
									vojaci -= 1000
									print('Zaútočili na tebe! Nově máš ' + str(vojaci) + ' vojáků!')
									kola += 1
								elif vojaci >= 2000 and obtiznost == "H":
									vojaci -= 2000
									print('Zaútočili na tebe! Nově máš ' + str(vojaci) + ' vojáků!')
									kola += 1
								else:
									print('Zaútočili na tebe, nemáš dostatek vojáků na protiútok\nGAME OVER')
									break
							elif kola == 40:
								if vojaci >= 1000 and obtiznost in ["E", "N"]:
									vojaci -= 1000
									print('Zaútočili na tebe! Nově máš ' + str(vojaci) + ' vojáků!')
									kola += 1
								elif vojaci >= 2000 and obtiznost == "H":
									vojaci -= 2000
									print('Zaútočili na tebe! Nově máš ' + str(vojaci) + ' vojáků!')
									kola += 1
								else:
									print('Zaútočili na tebe, nemáš dostatek vojáků na protiútok\nGAME OVER')
									break
							elif kola == 45 and obtiznost in ["N", "H"]:
								if vojaci >= 1000 and obtiznost == "N":
									vojaci -= 1000
									print('Zaútočili na tebe! Nově máš ' + str(vojaci) + ' vojáků!')
									kola += 1
								elif vojaci >= 2000 and obtiznost == "H":
									vojaci -= 2000
									print('Zaútočili na tebe! Nově máš ' + str(vojaci) + ' vojáků!')
									kola += 1
								else:
									print('Zaútočili na tebe, nemáš dostatek vojáků na protiútok\nGAME OVER')
									break
							elif kola == 50:
								print('Nestihl jsi dohrát hru pod 50 kol\nGAME OVER')
								break
							hra = input(str(kola) + '. KOLO!\nK = Koupit vojáky, V = Válka, I = Investovat, B = banka, D = Další kolo, E = exit ')
							if hra == "E":
								print('Odešel jsi ze hry.')
								break
							elif hra == 'K':
								voj = input('Máš ' + str(vojaci) + ' vojáků, peněz ' + str(penize) + ', cena za 1000 vojáků je 1 mld, za 2000 vojáků 2 mld, za 3000 vojáků 3 mld. Kolik jich chceš koupit? ')
								if voj == '1000':
									if penize >= 1:
										penize -= 1
										vojaci += 1000
										print('Nakoupeno 1000 vojáků, celkem jich máš ' + str(vojaci) + ', zbývá ti ' + str(penize) + ' peněz.')
									else:
										print("NEMÁŠ DOSTATEK FINANCÍ\n")
								elif voj == '2000':
									if penize >= 2:
										penize -= 2
										vojaci += 2000          
										print('Nakoupeno 2000 vojáků, celkem jich máš ' + str(vojaci) + ', zbývá ti ' + str(penize) + ' peněz.')
									else:
										print("NEMÁŠ DOSTATEK FINANCÍ\n")
								elif voj == '3000':
									if penize >= 3:
										penize -= 3
										vojaci += 3000
										print('Nakoupeno 3000 vojáků, celkem jich máš ' + str(vojaci) + ', zbývá ti ' + str(penize) + ' peněz.')
									else:
										print("NEMÁŠ DOSTATEK FINANCÍ\n")
								else:
									print('Zadal jsi špatné zadání, celkem máš ' + str(vojaci) + ' vojáků, zbývá ti ' + str(penize) + ' peněz.')
							elif hra == 'D':
								kola += 1
								penize += penize_za_kolo
								penize -= banka
								banka = 0
							elif hra == 'V':
								valka = input('musíš obsadit ještě ' + str(obsadit) + ' území. Na jedno území potřebuješ 2000 vojáků, chceš zaútočit? A = ano, N = ne ')
								if valka == 'A':
									if vojaci >= 2000:
										vojaci -= 2000
										obsadit -= 1
										print('Zaútočil jsi! zbývá ti ' + str(vojaci) + ' vojáků.')
									else:
										print("NEMÁŠ DOSTATEK VOJÁKŮ!\n")
								else:
									print("Špatné zadání!\n")
							elif hra == 'B':
								if banka <= 3:
									bank = input('Kolik si chceš půjčit? 1, 2, 3 mld? ')
									if bank == "1":
										penize += 1
										banka += 2
										print('dluh v tento moment máš ' + str(banka) + ' mld.')
									elif bank == "2":
										penize += 2
										banka += 4
										print('dluh v tento moment máš ' + str(banka) + ' mld.')
									elif bank == "3":
										penize += 3
										banka += 6
										print('dluh v tento moment máš ' + str(banka) + ' mld.')
								else:
									print("Už sis půjčil maximum, co jde!")
							elif hra == "I":
								investice = input("Kolik chceš investovat?\n6 (+1 peníz za kolo)\n10 (+2 peníze za kolo)")
								if investice == "6":
									if penize_za_kolo < 10 and obtiznost == "E":
										if penize >= 6:
											penize -= 6
											penize_za_kolo += 1
											print(f"{penize_za_kolo} peněz za kolo")
										else:
											print("NEMÁŠ DOSTATEK FINANCÍ!!\n")
									elif penize_za_kolo < 5 and obtiznost in ["N", "H"]:
										if penize >= 6:
											penize -= 6
											penize_za_kolo += 1
											print(str(penize_za_kolo) + ' peněz za kolo')
										
										else:
											print("NEMÁŠ DOSTATEK FINANCÍ!!\n")
									else:
										print("Už jsi investoval až moc peněz!")
								elif investice == "10":
									if penize_za_kolo < 9 and obtiznost == "E":
										if penize >= 10:
											penize -= 10
											penize_za_kolo += 2
											print(str(penize_za_kolo) + ' peněz za kolo')
										
										else:
											print("NEMÁŠ DOSTATEK FINANCÍ!!\n")
									elif penize_za_kolo < 4 and obtiznost in ["N", "H"]:
										if penize >= 10:
											penize -= 10
											penize_za_kolo += 2
											print(str(penize_za_kolo) + ' peněz za kolo')
										
										else:
											print("NEMÁŠ DOSTATEK FINANCÍ!!\n")
									else:
										print("Už jsi investoval až moc peněz!")
								else:
									print("Taková investice není na výběr!\n")
							else:
								print("Špatné zadání!\n")
					elif menu == 'N':
						print('To je škoda :( Tak ahoj! ')
						mixer.music.pause()
						break
					else:
						print('Špatné zadání!\n')
			elif language == "de":
				print(f"{Fore.RED}Das Spiel ist nur auf Tschechisch verfügbar{Fore.RESET}")
		elif game == "M":
			if language == "en":
				print(f"{Fore.RED}Game is only in czech!{Fore.RESET}")
			elif language == "cz":
				while True:
					player1 = input("Zadejte jméno hráče 1: ")
					if player1.startswith(" ") or player1.endswith(" ") or player1 == "":
						print(f"{Fore.RED}Musíte zadat jméno, ve jméně\nnesmí být mezera na začátku, ani na konci!{Fore.RESET}")
					else:
						break
				while True:
					player2 = input("Zadejte jméno hráče 2: ")
					if player2.startswith(" ") or player2.endswith(" ") or player2 == "":
						print(f"{Fore.RED}Musíte zadat jméno, ve jméně\nnesmí být mezera na začátku, ani na konci!{Fore.RESET}")
					else:
						break
				while True:
					print("ahoj")
			elif language == "de":
				print(f"{Fore.RED}Das Spiel ist nur auf Tschechisch verfügbar{Fore.RESET}")
	elif home == "P":
		while True:
			prg = input(">>> ")
			if prg == "write()":
				write = input(">>>> ")
				print(write)
			elif prg == "write(dfn)":
				write_var = input(">>>> ")
				if write_var in promenne:
					print(promenne.get(write_var))
			elif prg.startswith("write(\"") and prg.endswith("\")"):
				novy_write = prg.split("write(\"", maxsplit=1)[1].split("\")", maxsplit=1)[0]
				print(novy_write)
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
			elif prg == "exit" or prg == "exit()":
				exit()
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
  • There are no longer problems with colors in Windows' and Mac's terminal
  • We added the soundtrack to the game
""")
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
0.8 VYPÝNACÍ AKTUALIZACE:
  • Nespamovací obrazovka při vypnutí
0.8 HUDEBNÍ A BAREVNÁ AKTUALIZACE:
  • Odebrali jsme problémy s barvami na Windows a Mac terminálu
  • Přidali jsme hudební podklad do hry
""")
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
""")
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
					exit()
				elif language == "cz":
					print("ahoj")
					exit()
				elif language == "de":
					print("auf wiedersehen")
					exit()
	elif home == "R" and user == None:
		w_username = input("Username: ")
		if w_username == "":
			if language == "en":
				print(f"{Fore.RED}Something went wrong... Your username can't be empty!{Fore.RESET}")
			elif language == "cz":
				print(f"{Fore.RED}Něco dopadlo špatně...Vaše užvatelské jméno nesmí být prázdné!{Fore.RESET}")
			elif language == "de":
				print(f"{Fore.RED}Etwas ist schief gelaufen... Dein Benutzername darf nicht leer sein!{Fore.RESET}")
			continue
		w_password = input("Password: ")
		if w_password == "":
			if language == "en":
				print(f"{Fore.RED}Something went wrong... Your password can't be empty!{Fore.RESET}")
			elif language == "cz":
				print(f"{Fore.RED}Něco dopadlo špatně...Vaše heslo nesmí být prázdné!{Fore.RESET}")
			elif language == "de":
				print(f"{Fore.RED}Etwas ist schief gelaufen... Ihr Passwort darf nicht leer sein!{Fore.RESET}")
			continue
		try:
			with open('data05.txt', 'a') as f:
				f.write(w_username + "|" + fer.encrypt(w_password.encode()).decode() + "\n")
		except:
			if language == "en":
				print(f"{Fore.RED}Something went wrong... Please, try it again with another characters!{Fore.RESET}")
			elif language == "cz":
				print(f"{Fore.RED}Něco dopadlo špatně...Prosím, zkuste to s jinými písmeny!{Fore.RESET}")
			elif language == "de":
				print(f"{Fore.RED}Etwas ist schief gelaufen... Bitte versuchen Sie es erneut mit einem anderen Zeichen!{Fore.RESET}")
	elif home == "L" and user == None:
		try:
			with open('data05.txt', 'r') as f:
				asi_username = input("Username: ")
				asi_password = input("Password: ")
				for line in f.readlines():
					data = line.rstrip()
					username, zasifrovany_password = data.split("|")
					password = fer.decrypt(zasifrovany_password.encode()).decode()
					if asi_username == username and asi_password == password:
						user = username
						if language == "en":
							print(f"You are now log in as {user}!")
						elif language == "cz":
							print(f"Jste přihlášeni jako {user}!")
						elif language == "de":
							print(f"Sie sind nun eingeloggt als {user}!")
					else:
						continue
		except FileNotFoundError:
			if language == "en":
				print(f"You haven't any accounts yet, please, register!")
			elif language == "cz":
				print("Nemáte zatím žádné účty, prosím, zaregistrujte se!")
			elif language == "de":
				print("Sie haben noch keine Konten, bitte registrieren Sie sich!")
	elif home == "L" and user != None:
		user = None
		if language == "en":
			print("You are now log out!")
		elif language == "cz":
			print("Jste odhlášeni!")
		elif language == "de":
			print("Sie sind nun abgemeldet!")
	elif home == "O":
		while True:
			if language == "en":
				nastaveni = input("What do you like to change? L = Language, Q = Go to menu: ").upper()
			elif language == "cz":
				nastaveni = input("Co byste chtěli změnit? L = Jazyk, Q = Jít do menu: ").upper()
			elif language == "de":
				nastaveni = input("Was möchten Sie ändern? L = Sprache, Q = Gehe zum Menü: ").upper()
			if nastaveni == "L":
				while True:
					if language == "en":
						jazykovy_vyber = input("What language would you like?\nCZ = Czech\nEN = English\nDE = Deutsch: ").upper()
					elif language == "cz":
						jazykovy_vyber = input("Jaký jazyk byste chtěli?\nCZ = Český\nEN = Anglický\nDE = Německy: ").upper()
					elif language == "de":
						jazykovy_vyber = input("Welche Sprache möchten Sie?\nCZ = Tschechisch\nEN = Englisch\nDE = Deutsch: ").upper()
					if jazykovy_vyber == "CZ":
						if language != "cz":
							language = "cz"
							print("Úspěšně změněno!")
							break
						else:
							print("Tento jazyk už máš vybraný!")
							break
					elif jazykovy_vyber == "EN":
						if language != "en":
							language = "en"
							print("Successfully changed!")
							break
						else:
							print("You already chose that language!")
							break
					elif jazykovy_vyber == "DE":
						if language != "de":
							language = "de"
							print("Erfolgreich geändert!")
							break
						else:
							print("Sie haben diese Sprache bereits gewählt!")
							break
					else:
						print("WHAT?\n")
			elif nastaveni == "Q":
				break
			else:
				print("WHAT?\n")
	elif home == "A":
		print("AAA")
	else:
		print("Another key!")