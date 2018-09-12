# Car Class

from cp1404practicals.prac_08.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string representation of a Car object."""
        return "{}, fuel={}, odometer={}".format(self.name, self.fuel,
                                                 self.odometer)

    def drive_reliability(self):
        # generates random number between 1 and 100
        # if that number is less than the reliability number the car will drive
        drive_reliability = random.randrange(0, 100)
        if drive_reliability < self.reliability:
            return True
        else:
            return False

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        self.drive_reliability()
        if self.drive_reliability() == True:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
            return distance
        else:
            distance = 0
            return distance