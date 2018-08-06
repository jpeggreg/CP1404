

def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
    result = determine_result(score)
    print(str(result))

def determine_result(score):
    if score > 90:
        result = 'Excellent'
    elif score > 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

main()