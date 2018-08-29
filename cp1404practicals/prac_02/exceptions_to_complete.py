"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        pass
    except ValueError:
        print("Please enter a valid integer.")
    result = numerator + denominator
    print("Valid result is:", result)