promenne = {}
user = None
language = "en"
#je to beta případné problémy nebo bugy hlaste na kv support team nebo vývojářům
print("KV system 0.6 (beta)\n©1995 - 2021 ALL RIGHTS RESERVED!\n")
while True:
	if user == None:
		if language == "en":
			print("\nYOU ARE NOT LOGGED IN!")
		elif language == "cz":
			print("\nNEJSTE PŘIHLÁŠENI!")
		elif language == "de":
			print("\nDU BIST NICHT EINGELOGGT!")
		if language == "en":
			home = input("G = Game\nP = Programming in KV script beta\nN = Patch notes\nR = Register\nL = Login\nO = Options\nE = Shotdown: ").upper()
		elif language == "cz":
			home = input("G = Hra\nP = Programování v KV scriptu beta\nN = Novinky\nR = Registrovat se\nL = Přihlásit se\nO = Nastavení\nE = Vypnout: ").upper()
		elif language == "de":
			home = input("G = Spiel\nP = Programmierung in KV-Skript-Beta\nN = Patchnotizen\nR = Registrieren\nL = Anmelden\nO = Optionen\nE = Herunterfahren: ").upper()
	else:
		if language == "en":
			print(f"\nYou are now log in as {user}!")
		elif language == "cz":
			print(f"\nJsi přihlášen jako {user}!")
		elif language == "de":
			print(f"\nSie sind jetzt angemeldet als {user}!")
		if language == "en":
			home = input("G = Game\nP = Programming in KV script beta\nN = Patch notes\nL = Logout\nO = Options\nE = Shotdown: ").upper()
		elif language == "cz":
			home = input("G = Hra\nP = Programování v KV scriptu beta\nN = Novinky\nL = Odhlásit se\nO = Nastavení\nE = Vypnout: ").upper()
		elif language == "de":
			home = input("G = Spiel\nP = Programmierung in KV-Skript-Beta\nN = Patchnotizen\nL = Abmelden\nO = Optionen\nE = Herunterfahren: ").upper()
	if home == "G":
		while True:
			if language == "en":
				game = input("__________________\n      game       \n__________________\nprocesing...\npress S to start: ").upper()
			elif language == "cz":
				game = input("__________________\n      hra       \n__________________\nnačítání...\nstiskněte S, abyste začali: ").upper()
			elif language == "de":
				game = input("__________________\n      Spiel       \n__________________\nWird geladen...\ndrücke S zum Starten: ").upper()
			if game == "S":
				if language == "en":
					print("Game is only in czech!")
					exit()
				elif language == "cz":
					penize = 3
					vojaci = 2000
					kola = 1
					obsadit = 20
					banka = 0
					penize_za_kolo = 2
					while True:
						menu = input("Vítej, cheš hrát tuto hru? A = ano N = ne: ")
						if menu == 'A':
							while True:
								if banka > 0 and penize >= 1:
									penize -= 1
									banka -= 1
								elif obsadit == 0:
									print('GRATULACE!!! Dohrál jsi hru!! Jsi dobrý!!')
									exit()
								elif kola == 10:
									if vojaci >= 1000:
										vojaci -= 1000
										print('Zaůtočili na tebe! Nově máš ' + str(vojaci) + ' vojáků!')
										kola += 1
									elif vojaci < 1000:
										print('GAME OVER')
										exit()
								elif kola == 20:
									if vojaci >= 1000:
										vojaci -= 1000
										print('Zaůtočili na tebe! Nově máš ' + str(vojaci) + ' vojáků!')
										kola += 1
									elif vojaci < 1000:
										print('GAME OVER')
										exit()
								elif kola == 30:
									if vojaci >= 1000:
										vojaci -= 1000
										print('Zaůtočili na tebe! Nově máš ' + str(vojaci) + ' vojáků!')
										kola += 1
									elif vojaci < 1000:
										print('GAME OVER')
										exit()
								elif kola == 40:
									if vojaci >= 1000:
										vojaci -= 1000
										print('Zaůtočili na tebe! Nově máš ' + str(vojaci) + ' vojáků!')
										kola += 1
									elif vojaci < 1000:
										print('GAME OVER')
										exit()
								elif kola == 50:
									print('GAME OVER')
									exit()
								hra = input(str(kola) + '. KOLO!\nK = Koupit vojáky, V = Válka, I = Investovat, B = banka, D = Další kolo, E = exit ')
								if hra == 'E':
									print('Odešel jsi ze hry.')
									exit()
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
									bank = input('Kolik si chceš půjčit? 1, 2, 3 mld? ')
									if bank == 1:
										penize += 1
										banka += 2
										print('dluh v tento moment máš ' + str(banka) + ' mld.')
									elif bank == 2:
										penize += 2
										banka += 4
										print('dluh v tento moment máš ' + str(banka) + ' mld.')
									elif bank == 3:
										penize += 3
										banka += 6
										print('dluh v tento moment máš ' + str(banka) + ' mld.')
								elif hra == "I":
									if penize_za_kolo < 8:
										investice = input("Kolik chceš investovat?\n6 (+1 peníz za kolo)\n10 (+2 peníze za kolo)")
										if investice == "6":
											if penize >= 6:
												penize -= 6
												penize_za_kolo += 1
												print(str(banka) + ' peněz za kolo') 
											else:
												print("NEMÁŠ DOSTATEK FINANCÍ!!\n")
										elif investice == "10":
											if penize >= 10:
												penize -= 10
												penize_za_kolo += 2
												print(str(penize_za_kolo) + ' peněz za kolo')
											else:
												print("NEMÁŠ DOSTATEK FINANCÍ!!\n")
										else:
											print("Taková investice není na výběr!\n")
									else:
										print("INVESTOVAL JSI UŽ AŽ MOC PENĚZ!\n")
								else:
									print("Špatné zadání!\n")
						elif menu == 'N':
							print('To je škoda :( Tak ahoj! ')
							exit()
						else:
							print('Špatné zadání!\n')
				elif language == "de":
					print = input("Das Spiel ist nur auf Tschechisch verfügbar")
				exit()
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
				else:
					pass
			elif "write(" in prg and "\")" in prg:
				try:
					list_write = prg.split("write(\"", maxsplit=1)
					novy_write = list_write[1].split("\")", maxsplit=1)[0]
					if list_write[0] == "":
						print(novy_write)
					else:
						print("Another key!")
				except IndexError:
					print("Another key!")
			elif prg == "dfn()":
				dfn = input(">>>> ")
				dfn_jako = input("= ")
				promenne[dfn] = dfn_jako
			elif prg == "dfn(show)":
				for i in promenne:
					print(f"{i} = {promenne.get(i)}")
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
			print("""\
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
    0.6 beta update
    • We added a game for Czech
""")
		elif language == "cz":
			print("""\
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
0.6 update
  • Přidali jsme hru pro češtinu
""")
		elif language == "de":
			print("""\
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
   0.6 beta update
   • Wir haben ein Spiel für Tschechisch hinzugefügt
""")
	elif home == "E":
		u = 1
		while u < 80000:
			if language == "en":
				print("Shutdowning, wait a minute please...")
			elif language == "cz":
				print("Vypínám, počkejte...")
			elif language == "de":
				print("Herunterfahren, warten Sie bitte eine Minute...")
			u += 1
		else:
			if language == "en":
				print("bye")
			elif language == "cz":
				print("ahoj")
			elif language == "de":
				print("auf wiedersehen")
			exit()
	elif home == "R" and user == None:
		w_username = input("Username: ")
		w_password = input("Password: ")
		with open("data05.txt", "a") as f:
			f.write(f"{w_username} = {w_password}\n")
	elif home == "L" and user == None:
		try:
			with open("data05.txt", "r") as f:
				asi_username = input("Username: ")
				asi_password = input("Password: ")
				for line in f.readlines():
					username, password = line.split(" = ")
					if username.rstrip() == asi_username and password.rstrip() == asi_password:
						user = username.rstrip()
						if language == "en":
							print("You are logged in!")
						elif language == "cz":
							print("Jste přihlášeni!")
						elif language == "de":
							print("Du bist eingeloggt!")
		except FileNotFoundError:
			if language == "en":
				print("You haven't any accounts! Please, register!")
			elif language == "cz":
				print("Nemáš zatím žádné účty! Prosím, zaregistrujte se!")
			elif language == "de":
				print("Sie haben keine Konten! Bitte registrieren!")
	elif home == "L" and user != None:
		user = None
		if language == "en":
			print("You are now logged out!")
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
	else:
		print("Another key!")