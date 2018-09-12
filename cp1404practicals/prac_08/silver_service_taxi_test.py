#test silver service taxi class
from cp1404practicals.prac_08.silver_service_taxi import SilverServiceTaxi


def run_tests():
    taxi = SilverServiceTaxi("Hummer", 200)
    print(taxi)
    taxi.start_fare()
    taxi.drive(18)
    print(taxi)
    fare = taxi.get_fare()
    print("${:.2f}".format(fare))


run_tests()