MINIMUM_LENGTH = 6

def main():
    password = get_password()
    display_asterix(password)


def display_asterix(password):
    print('*' * len(password))


def get_password():
    password = input("Enter a password with at least {} characters ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        password = input("Enter a password with at least {} characters ".format(MINIMUM_LENGTH))
    return password


main()