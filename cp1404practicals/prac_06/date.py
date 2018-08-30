
DAY = 30
MONTH = 8
YEAR = 2018


class Date:

    def __init__(self, day=00, month=00, year=0000):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return("{}/{}/{}".format(self.day, self.month, self.year))

    def current_date(self):
        return("{}/{}/{}".format(DAY, MONTH, YEAR))