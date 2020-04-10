# Tipper
# Displays the cost of a 15 or 20 percent tip when the user inputs their bill

bill = input("Enter your bill here: $")
bill = float(bill)
tip15 = bill * .15
tip20 = bill * .20
print("\nYour tip is $", tip15, "or if you're feeling generous $", tip20)
input("\n\nPress the enter key to exit.")
