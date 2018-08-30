from cp1404practicals.prac_06.car import Car

# car driving simulator
def main():

    print("Let's drive!")
    name = input("Enter your car name: ")
    car = Car(name, 100)
    car.odometer = 0
    menu_choice = print_menu(name, car)
    while menu_choice != "q":

        if menu_choice == "d":
            drive_distance = ""
            while drive_distance == "":
                try:
                    drive_distance = int(input("How many km do you wish to drive? "))
                    if drive_distance >= 0:
                        distance_driven = car.drive(drive_distance)
                        print("The car drove {}km".format(distance_driven), end="")
                        if car.fuel == 0:
                            print(" and ran out of fuel.", end="")
                        menu_choice = print_menu(name, car)
                    else:
                        print("Distance must be >= 0")
                except ValueError:
                    print("Distance must be a number")

        elif menu_choice == "r":
            add_fuel = ""
            while add_fuel == "":
                try:
                    add_fuel = int(input("How many units of fuel do you want to add to the car? "))
                    if add_fuel >= 0:
                        car.add_fuel(add_fuel)
                        print("Added {} units of fuel.\n".format(add_fuel))
                        menu_choice = print_menu(name, car)
                    else:
                        print("Fuel amount must be >= 0")
                except ValueError:
                    print("Amount must be a number")
        else:
            print("Invalid choice\n")
            menu_choice = print_menu(name, car)
    else:
        print("\nGood bye {}'s driver.".format(name))


# shows menu options and returns user menu choice
def print_menu(name, car):
    print("\n" + name + ", fuel={self.fuel}, odometer={self.odometer}".format(car, self=car))
    print("Menu:\nd) drive\nr) refuel\nq) quit")
    menu_choice = str(input("Enter your choice: ").lower())
    return menu_choice



main()