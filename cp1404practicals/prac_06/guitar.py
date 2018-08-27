
CURRENT_YEAR = 2018
VINTAGE_AGE = 50

class Guitars:
    #guitar class for keeping details of guitars
    def __init__(self, name="", year=0, cost=0):
        #initialise a guitar
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        #returns string information of guitar
        return("{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost))

    def get_age(self):
        # determines age of guitar
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        #determines if vintage
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        #sort guitars by year
        return self.year < other.year