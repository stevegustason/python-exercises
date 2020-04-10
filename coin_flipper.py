# Coin Flipper
# Flips a coin 100 times and tells you the number of heads and tails

import random

print("What would happen if you flipped a coin 100 times? Let's find out.\n\n")

heads = 0
tails = 0
number = 0
flips = 0

while flips != 100:
    flips += 1
    number = random.randint(1, 2)
    if number == 1:
        heads += 1
    elif number == 2:
        tails += 1
    else:
        print("Error, coin only has 2 sides.")

print("You would've flipped", heads, "heads, and", tails, "tails.")

input("\n\nPress the enter key to exit.")
        
