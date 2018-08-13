import random

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
    while len(ticket) != 6:
        number = [random.randrange(1, 46, 1)]
        if number in ticket:
            pass
        else:
            ticket.append(number)
    ticket = sorted(ticket)
    return ticket

main()