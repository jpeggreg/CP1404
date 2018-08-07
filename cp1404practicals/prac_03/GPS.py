import random

GOPHER_POPULATION = 1000  # starting population of gophers
MINIMUM_BIRTH_RANGE = 0.10  # 10%
MAXIMUM_BIRTH_RANGE = 0.20  # 20%
MINIMUM_DEATH_RANGE = 0.05  # 5%
MAXIMUM_DEATH_RANGE = 0.25  # 25%
YEARS = 10

def main():
    gopher_total = GOPHER_POPULATION
    print("Welcome to the Gopher Population Simulator!")
    for i in range(5):
        print("Year " + str(i + 1))
        gophers_born = gopher_births(gopher_total)
        gophers_died = gopher_deaths(gopher_total)
        gopher_total = int(gopher_total + gophers_born - gophers_died)
        print("{} gophers were born. {} died.".format(gophers_born, gophers_died))
        print("Population: {}".format(gopher_total))
    print("Population: {}".format(gopher_total))

# determines how many gohpers are born based on random total 10% to 20% of current total population
def gopher_births(gopher_total):
    gophers_born = int(abs(random.randrange(MINIMUM_BIRTH_RANGE * gopher_total, MAXIMUM_BIRTH_RANGE * gopher_total, 5)))
    return int(gophers_born)

# determines how many gohpers died based on random total 10% to 20% of current total population
def gopher_deaths(gopher_total):
    gophers_died = int(abs(random.randrange(MINIMUM_DEATH_RANGE * gopher_total, MAXIMUM_DEATH_RANGE * gopher_total, 5)))
    return int(gophers_died)

main()
