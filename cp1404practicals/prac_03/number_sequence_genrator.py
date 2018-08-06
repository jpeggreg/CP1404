x = int(input("Please enter your first number: "))
y = int(input("Please enter your second number: "))
print("\n1. Show the even numbers from x to y \n2. Show the odd numbers from x to y \n3. Show the squares from x to y \n4. Exit the program")
choice = str(input(""))
while choice != '4':
    if choice == '1':
        for num in range(x, y + 1):
            if num % 2 == 0:
                print(num)
    elif choice == '2':
        for num in range(x - 1, y + 1):
            if num % 2 != 0:
                print(num)
    elif choice == '3':
        for num in range(x, y + 1):
            squares = num * num
            print(squares)
    else:
        print("Invalid menu choice")
    print("\n1. Show the even numbers from x to y \n2. Show the odd numbers from x to y \n3. Show the squares from x to y \n4. Exit the program")
    choice = str(input(""))
print("Goodbye")