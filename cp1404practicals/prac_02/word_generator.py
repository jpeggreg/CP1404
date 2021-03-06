"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

WORD_FORMAT = "cv"
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

#word_format = input("Enter a word format, v for Vowel and c for Consonant. eg: ccvcvvc: ").lower()
word_format = ''.join(random.choice(WORD_FORMAT) for x in range(8))
word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)

print(word)