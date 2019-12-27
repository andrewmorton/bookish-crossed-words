# for a valid word, find ones that are vowel consonant vowel in the middle


def return_letter_list(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = filter(lambda x: x not in vowels, map(chr, range(97, 123)))
    if string == "v":
        return vowels
    elif string == "c":
        return consonants


def is_vowel(letter):
    if letter in return_letter_list("v"):
        return letter
    else:
        return False


def is_consanant(letter):
    if letter in return_letter_list("c"):
        return letter
    else:
        return False
