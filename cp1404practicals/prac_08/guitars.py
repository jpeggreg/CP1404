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

    # loop through and display all languages (using their str method)
    for guitar in guitars:
        print(guitar)

main()