"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from cp1404practicals.prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    limo = Car(100)
    limo.add_fuel(20)
    print("fuel =", limo.fuel)
    limo.drive(115)
    print("odo =", limo.odometer)
    print("Car, fuel={self.fuel}, odometer={self.odometer}".format(self=limo))

    print("Limo {}, {}".format(limo.fuel, limo.odometer))
    print("Limo {self.fuel}, {self.odometer}".format(self=limo))

    limo.add_fuel(199)
    limo.drive(162)
    print("Limo, fuel={self.fuel}, odometer={self.odometer}".format(self=limo))



main()
