import random

LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def main():
    """Program to get password length and number of each type required."""
    password_length = int(input("Enter the password length do you require? "))
    count_lower = int(input("How many lowercase letters? "))
    count_upper = int(input("How many UPPERCASE letters? "))
    count_special = int(input("How many special characters? "))
    # check the length of password is more than total number of characters user requires
    if password_length < (count_lower + count_upper + count_special):
        print("Password length is not long enough")
        password_length = int(input("Enter the password length do you require? "))
        count_lower = int(input("How many lowercase letters? "))
        count_upper = int(input("How many UPPERCASE letters? "))
        count_special = int(input("How many special characters? "))
    else:
        password = password_generator(password_length, count_upper, count_lower, count_special)
    print("Your password is " + str(password))

# Randomly generates password based on user requirements and stores in a list
# Shuffles list at end and returns random password to main as a string
def password_generator(password_length, count_upper, count_lower, count_special):
    password_list = []
    for i in range(count_lower):
        password_list.append(random.choice(LOWERCASE_LETTERS))
    for i in range(count_upper):
        password_list.append(random.choice(UPPERCASE_LETTERS))
    for i in range(count_special):
        password_list.append(random.choice(SPECIAL_CHARACTERS))
    for i in range(password_length - len(password_list)):
        password_list.append(random.choice(LOWERCASE_LETTERS))
    random.shuffle(password_list)
    password = "".join(password_list)
    return password

main()