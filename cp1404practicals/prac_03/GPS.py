import random

GOPHER_POPULATION = 1000  # starting population of gophers
MINIMUM_BIRTH_RANGE = 0.1  # 10%
MAXIMUM_BIRTH_RANGE = 0.2  # 20%
MINIMUM_DEATH_RANGE = 0.05  # 5%
MAXIMUM_DEATH_RANGE = 0.25  # 25%
YEARS = 10

# Main simulates total population change over given number of years using random births and deaths
def main():
    gopher_total = GOPHER_POPULATION
    print("Welcome to the Gopher Population Simulator!")
    print("Starting Population {} ".format(gopher_total))
    for i in range(YEARS):
        print("Year " + str(i + 1))
        gophers_born = gopher_births(gopher_total)
        gophers_died = gopher_deaths(gopher_total)
        gopher_total = (gopher_total + gophers_born - gophers_died)
        print("\n{:.0f} gophers were born. {:.0f} died.".format(gophers_born, gophers_died))
        print("Population: {:.0f}".format(gopher_total))

# determines how many gohpers are born based on random total 10% to 20% of current total population
def gopher_births(gopher_total):
    gophers_born = random.uniform(MINIMUM_BIRTH_RANGE * gopher_total, MAXIMUM_BIRTH_RANGE * gopher_total)
    return gophers_born

# determines how many gohpers died based on random total 5% to 25% of current total population
def gopher_deaths(gopher_total):
    gophers_died = random.uniform(MINIMUM_DEATH_RANGE * gopher_total, MAXIMUM_DEATH_RANGE * gopher_total)
    return gophers_died

main()