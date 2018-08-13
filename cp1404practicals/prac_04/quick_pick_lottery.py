import random

NUMBER_DRAW = 6
MINIMUM = 1
MAXIMUM = 45

def main():
    quick_picks = int(input("How many quick picks? "))
    tickets = []
    for i in range(quick_picks):
        ticket = ticket_generator()
        tickets.append(ticket)
    for ticket in tickets:
        print(''.join(map(str, ticket)))

def ticket_generator():
    ticket = []
    while len(ticket) != NUMBER_DRAW:
        number = [random.randrange(MINIMUM, MAXIMUM, 1)]
        if number in ticket:
            pass
        else:
            ticket.append(number)
    ticket = sorted(ticket)
    return ticket

main()