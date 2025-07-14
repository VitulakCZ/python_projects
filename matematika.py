import math

# Dobrý den, tohoto komentáře si prosím nevšímejte, jelikož se jedná o test gitu. Děkujeme za pochopení.
def mody(obvod_obsah, tvar, obracene):
	input_text2 = None
	if not obracene:
		match tvar:
			case "Č":
				input_text = "Kolik je strana čtverce (v metrech)? [M pro jiný mód, Z = Zpět]: " if obvod_obsah != "os" else "Kolik je obvod čtverce (v metrech)? [M pro jiný mód, Z = Zpět]: "
			case "O":
				input_text = "Kolik je 1. strana obdélníku (v metrech)? [M pro jiný mód, Z = Zpět]: " if obvod_obsah != "os" else "Kolik je obvod obdélníku (v metrech)? [M pro jiný mód, Z = Zpět]: "
				if obvod_obsah != "os":
					input_text2 = "Kolik je 2. strana obdélníku (v metrech)? [M pro jiný mód, Z = Zpět]: "
		obracene = True
		return (input_text, input_text2, obracene)

	if obvod_obsah == "o":
		input_text = "Kolik je obvod čtverce (v metrech)? [M pro jiný mód, Z = Zpět]: " if tvar == "Č" else "Kolik je obvod obdélníku (v metrech)? [M pro jiný mód, Z = Zpět]: "
	if obvod_obsah == "s" or obvod_obsah == "os":
		input_text = "Kolik je obsah čtverce (v metrech^2)? [M pro jiný mód, Z = Zpět]: " if tvar == "Č" else "Kolik je obsah obdélníku (v metrech)? [M pro jiný mód, Z = Zpět]: "
	obracene = False
	return (input_text, input_text2, obracene)

def krizovatka(tvar, obvod_obsah):
	obracene = False
	(input_text, input_text2, obracene) = mody(obvod_obsah, tvar, obracene)
	while True:
		try:
			value = input(input_text).upper()
			value2 = None
			if value == "M":
				mody(obvod_obsah, tvar, obracene)
				(input_text, input_text2, obracene) = mody(obvod_obsah, tvar, obracene)
				continue
			if value == "Z":
				geometrie()
			value = float(value)
			if value < 0:
				raise ValueError
			if input_text2 is not None:
				value2 = input(input_text2).upper()
				value2 = float(value_2)
				if value2 < 0:
					raise ValueError
			match tvar:
				case "Č":
					ctverec(obvod_obsah, value, obracene)
				case "O":
					obdelnik(obvod_obsah, value, value2, obracene)
				case "T":
					trojuhelnik()
		except ValueError:
			print("Toto není číslo (potažmo číslo záporné)!")
			geometrie()

def ctverec(obvod_obsah, value, obracene):
	value = float(value)
	if not obracene:
		if obvod_obsah == "os":
			print("Obvod čtverce je {:.2f} m.\n".format(math.sqrt(value)*4))
			geometrie()
		print("Strana čtverce je {:.2f} m.\n".format(value/4) if obvod_obsah == "o" else "Strana čtverce je {:.2f} m.\n".format(math.sqrt(value)))
		geometrie()
	if obvod_obsah == "os":
		print("Obsah čtverce je {:.2f} m^2.\n".format((value/4)**2))
		geometrie()
	print("Obvod čtverce je {:.2f} m.\n".format(value*4) if obvod_obsah == "o" else "Obsah čtverce je {:.2f} m^2.\n".format(value**2))
	geometrie()

def obdelnik(obvod_obsah, value, value2, obracene):
	value = float(value)
	value2 = float(value2) if value2 is not None else None
	if not obracene:
		if obvod_obsah == "os":
			print("Obvod obdélníku je {:.2f} m.\n".format(math.sqrt(value)*4))
			geometrie()
		print("Strany obdélníku se nedají definovat.")
		geometrie()
	if obvod_obsah == "os":
		print("Obsah obdélníku je {:.2f} m^2.\n".format((value/4)**2))
		geometrie()
	print("Obvod obdélníku je {:.2f} m.\n".format(2*(value + value2)) if obvod_obsah == "o" else "Obsah obdélníku je {:.2f} m^2.\n".format(value*value2))
	geometrie()

def obvod_trojuhelniku():
	while True:
		try:
			strana_a = input("Strana A: ")
			strana_a = float(strana_a)
			if strana_a < 0:
				raise ValueError
			strana_b = input("Strana B: ")
			strana_b = float(strana_b)
			if strana_b < 0:
				raise ValueError
			strana_c = input("Strana C: ")
			strana_c = float(strana_c) 
			if strana_c < 0:
				raise ValueError
			print(f"Obvod obdélníku je {strana_a+strana_b+strana_c:.2f}")
			break
		except ValueError:
			print("Toto není číslo!")
			return

def obsah_trojuhelniku():
	while True:
		try:
			strana = input("Strana: ")
			strana = float(strana)
			if strana < 0:
				raise ValueError
			vyska  = input("Výška k ní: ")
			vyska  = float(vyska)
			if vyska < 0:
				raise ValueError
			print(f"Obsah obdélníku je {strana*vyska/2:.2f}")
			break
		except ValueError:
			print("Toto není číslo!")
			return

def strana_trojuhelniku():
	pravouhly = input("Je tento trojúhelník pravoúhlý? [Y/n] ").upper()
	if pravouhly == "Y":
		prepona = None
		try:
			while True:
				if prepona != "1":
					strana_1 = input("Strana A (P = Označit jako přeponu): ").upper()
					if strana_1 == "P":
						prepona = "1"
						continue
				else:
					strana_1 = input("Strana A (O = Označit jako odvěsnu): ").upper()
					if strana_1 == "O":
						prepona = None
						continue
					strana_1 = float(strana_1)
					if strana_1 < 0:
						raise ValueError
					prepona = strana_1
					strana_1 = None
					break
				strana_1 = float(strana_1)
				if strana_1 < 0:
					raise ValueError
				break
			while True:
				if prepona == "1" or prepona is None:
					strana_2 = input("Strana B (P = Označit jako přeponu): ").upper()
					if strana_2 == "P":
						prepona = "2"
						continue
				elif prepona == "2":
					strana_2 = input("Strana B (O = Označit jako odvěsnu): ").upper()
					if strana_2 == "O":
						prepona = None
						continue
					strana_2 = float(strana_2)
					if strana_2 < 0:
						raise ValueError
					prepona = strana_2
					strana_2 = None
					break
				else:
					strana_2 = input("Strana B: ").upper()
				strana_2 = float(strana_2)
				if strana_2 < 0:
					raise ValueError
				break
			if (prepona is not None and strana_1 is not None and strana_1 > prepona) or (prepona is not None and strana_2 is not None and strana_2 > prepona):
				print("ERROR: Odvěsna je větší, než přepona!")
				return
			if prepona is None:
				prepona = math.sqrt(strana_1**2 + strana_2**2)
			elif strana_1 is None:
				strana_1 = math.sqrt(prepona**2 - strana_2**2)
			elif strana_2 is None:
				strana_2 = math.sqrt(prepona**2 - strana_1**2)
			print(f"Přepona: {prepona:.2f}\nOdvěsna 1: {strana_1:.2f}\nOdvěsna 2: {strana_2:.2f}")
		except ValueError:
			print("Toto není číslo!")
			return
	elif pravouhly == "N":
		pass
	else:
		print("Zpět!")

def trojuhelnik():
	while True:
		troj = input("Co chcete v trojúhelníku spočítat?\n\nO = Obvod\nS = Obsah\nC = Stranu\nU = Úhel\nZ = Zpět: ").upper()
		if troj == "Z":
			return
		if troj == "O":
			obvod_trojuhelniku()
			return
		elif troj == "S":
			obsah_trojuhelniku()
			return
		elif troj == "C":
			strana_trojuhelniku()
			return
		elif troj == "U":
			uhel_trojuhelniku()
			return

def geometrie():
	tvar = input("Co chceš spočítat?\n\nČ = Čtverec\nO = Obdélník\nT = Trojúhelník\nZ = Zpět: ").upper()
	if tvar not in ["Č", "O", "T", "Z"]:
		print("Tvar není legální!\n")
		geometrie()
	if tvar == "Z":
		zaklad()
	if tvar == "T":
		trojuhelnik()
		geometrie()
	obvod_obsah = input("Chcete vypočítat obvod, obsah nebo obvod na obsah? [o/S/oS]: ").lower()
	if obvod_obsah not in ["o", "s", "os"]:
		print("OBVOD NEBO OBSAH TEDA?!")
		geometrie()
	krizovatka(tvar, obvod_obsah)

def zaklad():
	while True:
		pocty = input("Vítej v mega super KV kalkulačce, která dokáže spočítat cokoliv :)\n\nG = Geometrie\nE = Exit: ").upper()
		if pocty == "G":
			geometrie()
		elif pocty == "E":
			exit()
zaklad()
