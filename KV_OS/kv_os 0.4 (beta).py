promenne = {}
u = 1
#je to beta případné problémy nebo bugy hlaste na kv support team nebo vývojářům

print("KV system 0.4 (beta)\n©1995 - 2021 ALL RIGHTS RESERVED!\n")
while True:
	home = input("G = Game\nP = Programing in KV script beta\nN = Patch notes\nE = Shotdown\nL = login: ").upper()
	if home == "G":
		while True:
			game = input("__________________\n      game       \n__________________\nprocesing...\npress S to start ").upper()
			if game == "S":
				print = input("we are sorry\ngame is in progress...")
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
	""")
	elif home == "E":
		while u < 80000:
			print("Shutdowning, wait a minute please...")
			u += 1
		else:
			print("bye")
			exit()
	elif home == "L":
		login = input("user: ")
		if login == "user1":
			user1 = input("password: ")
			if user1 == "passoword1":
				print("nice to meet you user1")
		if login == "user2":
			user1 = input("password: ")
			if user1 == "passoword2":
				print("nice to meet you user2")
			else:
				print("invalid password")
	else:
		print("another key!")