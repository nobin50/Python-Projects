import string
import random

letter_input_1 = input("Write (v) for vowel, (c) for consonant, & (l) for random")
letter_input_2 = input("Write (v) for vowel, (c) for consonant, & (l) for random")
letter_input_3 = input("Write (v) for vowel, (c) for consonant, & (l) for random")
letter_input_4 = input("Write (v) for vowel, (c) for consonant, & (l) for random")

vowels = 'aeiou'
consonant = 'bcdfghjklmnpqrstvwxyz'
l = string.ascii_lowercase


def generator():
    if letter_input_1 == 'v':
        letter1 = random.choice(vowels)
    elif letter_input_1 == 'c':
        letter1 = random.choice(consonant)
    elif letter_input_1 == 'l':
        letter1 = random.choice(l)
    else:
        letter1 = letter_input_1

    if letter_input_2 == 'v':
        letter2 = random.choice(vowels)
    elif letter_input_2 == 'c':
        letter2 = random.choice(consonant)
    elif letter_input_2 == 'l':
        letter2 = random.choice(l)
    else:
        letter2 = letter_input_2

    if letter_input_3 == 'v':
        letter3 = random.choice(vowels)
    elif letter_input_3 == 'c':
        letter3 = random.choice(consonant)
    elif letter_input_3 == 'l':
        letter3 = random.choice(l)
    else:
        letter3 = letter_input_3

    if letter_input_4 == 'v':
        letter4 = random.choice(vowels)
    elif letter_input_4 == 'c':
        letter4 = random.choice(consonant)
    elif letter_input_4 == 'l':
        letter4 = random.choice(l)
    else:
        letter4 = letter_input_4

    letter = letter1 + letter2 + letter3 + letter4

    print(letter)

print("Here are the baby names we suggest for you...")
for babyname in range(20):
    generator()
	
	
"""
print(string.ascii_lowercase)
print(string.ascii_letters)

print(random.choice(string.ascii_lowercase))
print(random.choice("Pull a letter from here including whitespace"))


def generator():
    letter1 = random.choice(string.ascii_lowercase)
    letter2 = random.choice(string.ascii_lowercase)
    letter3 = random.choice(string.ascii_lowercase)
    letter4 = random.choice(string.ascii_lowercase)
    name = letter1 + letter2 + letter3 + letter4
    print(name)

generator()
"""