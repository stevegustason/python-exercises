# Mood Computer
# Demonstrates the elif clause

import random

print("I sense your energy. Your true emotions are coming through the keyboard.")
print("You are...")

mood = random.randint(1,3)

if mood == 1:
    # happy
    print(":)")
elif mood == 2:
    # neutral
    print(":|")
elif mood == 3:
    # sad
    print(":(")
else:
    print("Illegal mood value! (You must be in a really bad mood).")

print("...today.")

input("\n\nPress the enter key to exit.")
