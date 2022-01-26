import sys


def num_vowels(text):
    num_vowels = 0
    for char in text.lower():
        if char in 'aeiouáéíóúü':
            num_vowels += 1
    return num_vowels


def num_whitespaces(text):
    num_whitespaces = 0
    for char in text:
        if char in ' ':
            num_whitespaces += 1
    return num_whitespaces


def num_digits(text):
    num_digits = 0
    for char in text:
        if char in '0123456789':
            num_digits += 1
    return num_digits


def num_words(text):
    docket = text.split()
    count = len(docket)
    return count


def reverse(text):
    string = text
    text_rev = text[::-1]
    return text_rev


def length(text):
    num_char = len(text)
    return num_char


def halfs(text):
    str_range = len(text)
    if str_range >= 2:
        mid = str_range // 2
        first_half = text[:mid]
        second_half = text[mid:]

    return " | ".join((first_half, second_half))


def upper_vowels(text):
    vowels = "AEIOU"
    uppvow = ""
    for char in text:
        if char.upper() in vowels:
            uppvow += char.upper()
        else:
            uppvow += char
    return uppvow


def sorted_by_words(text):
    docket = text.split()
    docket.sort()
    sorted = ' '.join(docket)
    return sorted



def length_of_words(text):
    text_docket = text.split()
    length_docket = []

    for char in text_docket:
        length = str(len(char))
        length_docket.append(length)
    word_len = " ".join(length_docket)

    return word_len


if __name__ == '__main__':
    text = sys.argv[1]
    print('Number of vowels:', num_vowels(text))
    print('Number of whitespaces:', num_whitespaces(text))
    print('Number of digits:', num_digits(text))
    print('Number of words:', num_words(text))
    print('Reverse of text:', reverse(text))
    print('Length of text:', length(text))
    print('Halfs of text:', halfs(text))
    print('Text with uppercased vowels:', upper_vowels(text))
    print('Sorted by words:', sorted_by_words(text))
    print('Length of words:', length_of_words(text))
