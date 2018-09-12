# taxi simulator

from cp1404practicals.prac_08.car import Car
from cp1404practicals.prac_08.taxi import Taxi
from cp1404practicals.prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "(C)hoose Taxi\n(D)rive\n(Q)uit"

#Taxi simulator using Taxi and SilverServiceTaxi Classes
def main():

    total_cost = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Hummer", 200)]
    print(MENU)
    menu_choice = (input(">>> ")).upper()
    while menu_choice != 'Q':
        if menu_choice == 'C':
            show_taxis(taxis)
            taxi_choice = int(input("Choose Taxi: "))
            chosen_taxi = taxis[taxi_choice - 1]
            print(MENU)
            menu_choice = (input(">>> ")).upper()
        elif menu_choice == "D":
            chosen_taxi.start_fare()
            drive_distance = float(input("How far? "))
            chosen_taxi.drive(drive_distance)
            fare = chosen_taxi.get_fare()
            print("The total far in {} costs ${:.2f}".format(chosen_taxi.name, fare))
            total_cost += fare
            print(MENU)
            menu_choice = (input(">>> ")).upper()
        else:
            print("invalid Choice ")
            print(MENU)
            menu_choice = (input(">>> ")).upper()

    print("Total cost of all fares = ${:.2f}".format(total_cost))
    print("Taxis:")
    show_taxis(taxis)


# shows available taxis
def show_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} {}".format(i + 1, str(taxi)))

main()