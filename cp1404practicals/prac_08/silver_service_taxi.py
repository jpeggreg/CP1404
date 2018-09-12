#Taxi Class
from cp1404practicals.prac_08.taxi import Taxi

class SilverServiceTaxi(Taxi):

    flagfall = 4.50

    def __init__(self, name, fuel):
        super().__init__(name, fuel)
        self.fanciness = 2
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def __str__(self):
        return super().__str__() + " plus flagfall of ${:.2f}".format(self.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall


