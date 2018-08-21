from datetime import datetime, date

name_age_dict = {}
PEOPLE = 5

while len(name_age_dict) < PEOPLE:
    name = input("Enter name: ")
    dob = datetime.strptime(input("Enter Date of Birth DD MM YYYY: "), "%d %m %Y")
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    name_age_dict[name] = age

for key, value in name_age_dict.items():
    print(key, value)


#function to take two parrallel lists as input parameters and returns dictionary where key from first list matches values from second list
names = ["Jack", "Jill", "Harry"]
dates_of_birth = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]

names_dob_dict = dict(zip(names, dates_of_birth))
print(names_dob_dict)

