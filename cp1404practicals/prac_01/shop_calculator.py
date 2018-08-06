

number_of_items = int(input("Please enter the number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Please enter the number of items: "))
total = 0
for i in range(number_of_items):
    price = float(input("Please enter the price of item " + str(i + 1) + ": "))
    total = price + total
if total > 100:
    total = total * 0.9
    print("The total price for " + str(i + 1) + " items is $" + "{:.2f}".format(total))
else:
    print("The total price for " + str(i + 1) + " items is $" + "{:.2f}".format(total))