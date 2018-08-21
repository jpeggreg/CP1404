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
