"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When Input is not an integer
2. When will a ZeroDivisionError occur? when input is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator < 0:
        fraction = numerator / denominator
        print(fraction)
    else:
        denominator = int(input("Enter a denominator greater than zero: "))
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")