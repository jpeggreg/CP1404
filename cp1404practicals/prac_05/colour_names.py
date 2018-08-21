# program to look up hexadecimal color codes from dictionary


COLOR_NAMES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
               "aquamarine1": "#7fffd4", "azure1": "#f0ffff",
               "bisque1": "#ffe4c4", "black": "#000000", "BlueViolet":
               "#8a2be2", "burlywood": "#deb887", "chocolate": "#d2691e",
               "coral": "#ff7f50" }
# print(COLOR_NAMES)

color = input("Enter color: ")
while color != "":
    if color in COLOR_NAMES:
        print(COLOR_NAMES[color])
    else:
        print("Invalid color")
    color = input("Enter color: ")