promenne = {}
u = 1
#je to beta případné problémy nebo bugy hlaste na kv support team nebo vývojářům

print("KV system 0.1 (beta)\n©1995 - 2021 ALL RIGHTS RESERVED!\n")
while True:
	home = input(">g = game, p = programing (kv script beta), e = shotdown< ")
	if home == "g":
		while True:
			game = input("__________________\n      game       \n__________________\nprocesing...\npress S to start ")
			if game == "S":
				print = input("we are sorry\ngame is in progress...")
				exit()
	elif home == "p":
		while True:
			prg = input(">>>")
			if prg == "write()":
				write = input(">>>>")
				print(write)
			elif prg == "while true":
				kolo = input(">>>>")
				ready = input("ready press b ")
				if ready == "b":
					while True:
						print(kolo)
				else:
					print("another key")
					exit()
			elif prg == "exit" or "exit()":
				exit()
	elif home == "e":
		while u < 80000:
			print("shutdowning wait a minute please")
			u += 1
		else:
			print("bye")
			exit()
	else:
		print("another key!")