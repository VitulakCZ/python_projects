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
		value = input(input_text).upper()
		value2 = None
		if value == "M":
			mody(obvod_obsah, tvar, obracene)
			(input_text, input_text2, obracene) = mody(obvod_obsah, tvar, obracene)
			continue
		if value == "Z":
			geometrie()
		if input_text2 is not None:
			value2 = input(input_text2).upper()
		match tvar:
			case "Č":
				ctverec(obvod_obsah, value, obracene)
			case "O":
				obdelnik(obvod_obsah, value, value4, obracene)
			case "T":
				trojuhelnik(obvod_obsah, value, value2, obracene)

def ctverec(obvod_obsah, value, obracene):
	try:
		value = float(value)
		if not obracene:
			if obvod_obsah == "os":
				print("Obvod čtverce je {:.2f} m.\n".format(math.sqrt(value)*4))
				geometrie()
				return
			print("Strana čtverce je {:.2f} m.\n".format(value/4) if obvod_obsah == "o" else "Strana čtverce je {:.2f} m.\n".format(math.sqrt(value)))
			geometrie()
			return
		if obvod_obsah == "os":
			print("Obsah čtverce je {:.2f} m^2.\n".format((value/4)**2))
			geometrie()
			return
		print("Obvod čtverce je {:.2f} m.\n".format(value*4) if obvod_obsah == "o" else "Obsah čtverce je {:.2f} m^2.\n".format(value**2))
		geometrie()
		return
	except ValueError:
		print("Toto není číslo!")
		geometrie()
		return

def obdelnik(obvod_obsah, value, value2, obracene):
	try:
		value = float(value)
		value2 = float(value2) if value2 is not None else None
		if not obracene:
			if obvod_obsah == "os":
				print("Obvod obdélníku je {:.2f} m.\n".format(math.sqrt(value)*4))
				geometrie()
				return
			print("Strany obdélníku se nedají definovat.")
			geometrie()
			return
		if obvod_obsah == "os":
			print("Obsah obdélníku je {:.2f} m^2.\n".format((value/4)**2))
			geometrie()
			return
		print("Obvod obdélníku je {:.2f} m.\n".format(2*(value + value2)) if obvod_obsah == "o" else "Obsah obdélníku je {:.2f} m^2.\n".format(value*value2))
		geometrie()
		return
	except ValueError:
		print("Toto není číslo!")
		geometrie()
		return

def geometrie():
	tvar = input("Co chceš spočítat?\n\nČ = Čtverec\nO = Obdélník\nT = Trojúhelník\nZ = Zpět: ").upper()
	if tvar not in ["Č", "O", "T", "Z"]:
		print("Tvar není legální!\n")
		geometrie()
	if tvar == "Z":
		zaklad()
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
