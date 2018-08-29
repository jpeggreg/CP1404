


def main():
    number_of_items = get_item_number()
    total = 0
    i, total = calculate_total(number_of_items, total)
    if total > 100:
        total = total * 0.9
        print("The total price for " + str(i + 1) + " items is $" + "{:.2f}".format(total))
    else:
        print("The total price for " + str(i + 1) + " items is $" + "{:.2f}".format(total))


def calculate_total(number_of_items, total):
    for i in range(number_of_items):
        price = float(input("Please enter the price of item " + str(i + 1) + ": "))
        total = price + total
    return i, total


def get_item_number():
    number_of_items = int(input("Please enter the number of items: "))
    while number_of_items < 0:
        print("Invalid number of items!")
        number_of_items = int(input("Please enter the number of items: "))
    return number_of_items


main()