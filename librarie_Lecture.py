"""from random import choice

coin = choice(["heads", "tails"])
print(coin)"""


"""import random

numver = ["j","q", "j"]
random.shuffle(numver)
for i in numver: 
 print(i)"""


"""import statistics

print(statistics.mean([100,90]))"""

import sys
import cowsay

"""if len(sys.argv)<2:
    sys.exit("too few arguments")
elif len(sys.argv)>2:
    sys.exit("too many arguments")


print("hello, my name is", sys.argv[1])"""

"""if len (sys.argv)<2:
    print("to few arguments")

for argv in sys.argv[1:]:
    print("hello mu name is", argv)"""

if len (sys.argv) == 2:
    cowsay.trex("hello" + sys.argv[1])

 





