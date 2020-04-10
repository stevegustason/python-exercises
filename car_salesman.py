# Car Salesman
# Program adds fees to the base price of a car

car_price = int(input("Enter the base price of the selected model: $"))

license_fee = .05 * car_price
print("Add the license fee: $", license_fee)

dealer_prep = int(200)
print("Add the cost of the dealer to prep the car: $", dealer_prep)

destin_charge = int(350)
print("And the cost for us to ship your car: $", destin_charge)

tax = car_price * .065
print("And finally tax: $", tax)

total = car_price + license_fee + dealer_prep + destin_charge + tax
print("Bringing your total to: $", total)

input("\n\n Press the enter key to exit.")
