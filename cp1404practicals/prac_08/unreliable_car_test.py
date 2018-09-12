# test Unreliable car class

from cp1404practicals.prac_08.unreliable_car import UnreliableCar

def run_tests():
    car = UnreliableCar("Car 1", 100, 50.0)
    car.drive(40)
    print(car)


run_tests()