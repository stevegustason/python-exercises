# Fortune Cookie

import random

number = random.randint(1, 5)

print("Hello young grasshopper, let's see what your fortune is today!\n\n")

if number == 1:
    print("You are going to be rich and stuck up.")
elif number == 2:
    print("You will be a hobo one day.")
elif number == 3:
    print("In 5 months, you will gain 75 lbs.")
elif number == 4:
    print("You will become very unpopular with your peers. Run away before it \
           is too late")
elif number == 5:
    print("You very lucky, fat man will raid your house soon.")
else:
    print("Too bad for you, no fortune today.")

input("\n\nPress the enter key to exit.")
