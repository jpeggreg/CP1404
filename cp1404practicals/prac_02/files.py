
# Program 1
OUTPUT_FILE = "name.txt"
name = input("What is your name?: ")
out_file = open(OUTPUT_FILE, 'w')
print(name, file=out_file)
out_file.close()

#Program 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
print("Your name is", name)
in_file.close()

#Program 3
in_file  = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1 + number2)
in_file.close()

#3 extended
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()