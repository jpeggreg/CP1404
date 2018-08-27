

from cp1404practicals.prac_06.guitar import Guitars

def main():
    #guitar program for prac 6
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitars(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

    guitars.append(Guitars("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitars("Line 6 JTV-59", 2010, 1512.9))

    guitars.sort()
    print("These are my guitars:")

    if guitars is not None:
        for i, guitar in enumerate(guitars):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print("Guitar {0}: {1.name:>30} ({1.year}), worth ${1.cost:10,.2f}\{2}".format(i + 1, guitar, vintage_string))
    else:
        print("No guitar entered")


main()