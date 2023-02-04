import random
random.seed()
while True:
    od = int(input("Od jakého čísla chceš hádat?"))
    do = int(input("Do jakeho čísla chces hadat?"))
    rozmyslen = input("jsi rozmyslen? ENTER = ukončit,  napsat ano = pokracovat")
    if(rozmyslen == "ano"):
        print("číslo, ktere jsi měl uhodnout bylo {0:d}".format(random.randint(od,do)))
    else:
        print("OK, někdy příště!")
        break