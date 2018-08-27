

class ProgrammingLanguage:
        # Shows information about programming languages

    def __init__(self, name, typing, reflection, year):
        #different fields of particular language
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        #returns particular attributes of certain programming language
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        "check if lanugage os dynamic typed"
        return self.typing == "Dynamic"

def run_tests():
    # tests/demos on ProgrammingLanguage class
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()
