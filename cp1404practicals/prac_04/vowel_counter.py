# takes name and counts how many vowels are in the name along with how many total letters

count = 0
vowels = set("aeiou")
name = input("Name: ")
for letter in name:
    if letter.lower() in vowels:
        count += 1
print("Out of {} letters, {} has {} vowels".format(len(name), name, count))