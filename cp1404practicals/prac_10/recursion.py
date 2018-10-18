"""
CP1404/CP5632 Practical
Recursion
"""


'''def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# TODO: 1. count down from 5 to 0 then count up to 5
# TODO: 2. use the debugger to step through and see what's actually happening
# print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n > 0:
        print(n ** 2)
    do_something(n - 1)

# 3. counts down to below zero where it starts printing the squares of each negative number
# 4. use the debugger to step through and see what's actually happening
do_something(4)

# 5. fix do_something() so that it works according to the docstring'''

def calculate_blocks(rows):
    """Calculate blocks needed for a given number of rows of a 2D pyramid."""
    # base case: we need zero blocks for zero (or fewer!) rows
    if rows <= 0:
        return 0
    # recursive case: each row contains the number of blocks as its row number
    # ... plus the rest of it
    return rows + calculate_blocks(rows - 1)

def build_pyramid():
    """Get user's pyramid size in rows and output the blocks needed."""
    # chosen_rows = 6
    chosen_rows = int(input("How many rows is your pyramid: "))
    print("For {} rows, you need {} blocks".format(chosen_rows,
                                                   calculate_blocks(
                                                       chosen_rows)))

build_pyramid()