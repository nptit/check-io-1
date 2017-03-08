import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def is_vowel(c: str):
    """
    Check character is vowel
    :param c: Character
    :return: True or False
    """
    return c.upper() in VOWELS


def is_consonant(c: str):
    """
    Check character is consonant
    :param c: Character
    :return: True or False
    """
    return c.upper() in CONSONANTS


def is_striped(word: str):
    """
    Check if given word is striped
    :param word:
    :return:
    """
    # Mark switcher is 0b0 if prev letter be vowel and 0b1 if prev be consonant
    switch = 0b1 if is_vowel(word[0]) else 0b0
    for c in word:
        if not c.isalpha():
            return False
        if switch == 0b0 and is_vowel(c):
            return False
        elif switch == 0b1 and is_consonant(c):
            return False
        switch ^= 0b1

    return True


def checkio(text):
    """
    Count striped words in given text
    :param text: Text with punctuation marks delimiters
    :return: count of striped words
    """
    counter = 0
    for word in re.split('[\s.,!?:;-]+', text):
        if len(word) < 2:
            continue
        counter += is_striped(word)

    return counter


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
