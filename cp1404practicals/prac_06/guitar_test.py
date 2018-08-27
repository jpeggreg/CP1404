

from cp1404practicals.prac_06.guitar import Guitars

def main():

    gibson= Guitars("Gibson L-5 CES", 1922, 16035.40)
    another = Guitars("Another Guitar", 2012, 399.95)

    print(gibson)
    print(another)

    print("{} get_age() - Expected {}. Got {}".format(gibson.name, 96, gibson.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(another.name, 6, another.get_age()))

    print("{} is_vintage() - Expected {}. Got {}".format(gibson.name, True, gibson.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(another.name, False, another.is_vintage()))


main()