#import random
#
#hry = {
#    "New Studio": [1989],
#    "Agent": [1995, 2011, 2013, 2019],
#    "Blastoff": [1999, 2004, 2021]
#}
#hra = random.choice(list(hry))
#print(str(hry.get(hra)).replace("[", "").replace(", ", "\n").replace("]", ""))
import math
x = 9
print(min(min(math.sqrt(x), 5) + max(math.sqrt(x), 5) ** 2, 30))