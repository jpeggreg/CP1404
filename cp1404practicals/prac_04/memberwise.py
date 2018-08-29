from operator import add


list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

add_elements = list(map(add, list_1, list_2))

print(add_elements)

