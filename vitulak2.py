import random
random.seed()
while True:
    od = ord(input("Od jakeho pismene chces hadat?"))
    do = ord(input("Do jakeho pismene chces hadat?"))
    rozmyslen = input("jsi rozmyslen? ENTER = restartovat  napsat ANO = pokracovat")
    if rozmyslen == "ANO":
        break
print("pismeno, ktere jsi mel uhodnout bylo {0:s}".format(chr(random.randint(od,do))))