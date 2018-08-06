import random

WORD_FORMAT = "cv"
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def main():
    word_format = input("Enter a word format, v for Vowel and c for Consonant. eg: ccvcvvc: ").lower()
    while is_valid_format(word_format) == False:
        word_format = input("Enter a word format, v for Vowel and c for Consonant. eg: ccvcvvc: ").lower()
    else:
        word = ''
        word_format = ''.join(random.choice(WORD_FORMAT) for x in range(8))
        for kind in word_format:
            if kind == "c":
                word += random.choice(CONSONANTS)
            else:
                word += random.choice(VOWELS)

        print(word)

def is_valid_format(word_format):
    for char in word_format:
        if char in WORD_FORMAT:
            return True
        else:
            return False

main()