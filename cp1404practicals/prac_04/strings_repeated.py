
string_list = []
string_input = input("Enter a word: ")
while string_input != "":
    string_input = input("Enter a word: ")
    string_list.append(string_input)
else:
    for i in range(1, len(string_list)):
        if string_list[i] == string_list[i - 1]:
            print("Strings repeated: {}".format(string_list[i]))
        else:
            print("No repeated strings entered")

