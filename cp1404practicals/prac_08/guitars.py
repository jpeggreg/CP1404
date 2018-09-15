from cp1404practicals.prac_06.guitar import Guitars


def main():
    """Read file of programming language details, save as objects, display."""
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitars(parts[0], parts[1], float(parts[2]))
        guitars.append(guitar)
    in_file.close()

    guitars.sort()

    # loop through and display all languages (using their str method)
    for guitar in guitars:
        print(guitar)


    # add new guitar to list
    new_guitar = []
    name = input("Name: ")
    while name == "":
        print("Input can not be blank")
        name = input("Name: ")
    else:
        new_guitar.append(name)
    year = input("Year: ")
    while year == "":
        print("Input can not be blank")
        year = input("Year: ")
    else:
        new_guitar.append(year)
    cost = 0
    while cost == 0:
        # validate int input for cost
        try:
            cost = float(input("Cost: "))
            if cost <= 0:
                print("Cost must be > 0")
        except ValueError:
            print("Invalid input; enter a valid number")
    else:
        new_guitar.append(float(cost))
    new_guitar = Guitars(name, year, cost)
    guitars.append(new_guitar)

    for guitar in guitars:
        print(guitar)

    # write new list to csv file
    with open("myguitars.csv", "w") as guitar_file:
        for guitar in guitars:
            guitar_file.write(str(guitar) + " \n")

main()