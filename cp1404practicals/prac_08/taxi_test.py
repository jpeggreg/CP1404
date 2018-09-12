
from cp1404practicals.prac_08.taxi import Taxi


def run_tests():
    #Test Tax class
    taxi = Taxi("Prius 1", 100)
    taxi.start_fare()
    taxi.drive(100)
    print(taxi)
    fare = taxi.get_fare()
    print(fare)

run_tests()