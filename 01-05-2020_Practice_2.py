#Shopping Cart: Show the total price

from decimal import Decimal

price = input("What's the price? ")
print("Your total is {:4.2f}".format(float(price)*1.0625))

