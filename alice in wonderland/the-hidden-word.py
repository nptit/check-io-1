class NotFound(Exception):
    """Word not found in text"""
    pass


def transpose_text(text):
    """Transpose text"""
    return [''.join([x[i] if len(x) >= i + 1 else ' ' for x in text]) for i in range(max([len(y) for y in text]))]


def search_word(text, word):
    """Find word in given list of text"""
    for i, row in enumerate(text):
        start = row.lower().find(word.lower())
        if start != -1:
            return i + 1, start + 1
    raise NotFound


def checkio(text, word):
    text = text.replace(' ', '').split('\n')
    result = [0, 0, 0, 0]

    # Try find key word in rows of text
    try:
        row, column = search_word(text, word)
        result = [row, column, row, column + len(word) - 1]
    except NotFound:
        # If not founded in rows. Search in columns
        try:
            row, column = search_word(transpose_text(text), word)
            result = [column, row, column + len(word) - 1, row]
        except NotFound:
            pass

    return result


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
