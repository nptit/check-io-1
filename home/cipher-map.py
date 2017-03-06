def recall_password(cipher_grille, ciphered_password):
    """
    Encrypt password with given mask and letters suite
    :param cipher_grille: Mask for password
    :param ciphered_password: Letters for password
    :return: Encrypt password
    """
    password = ''
    mask = [list(x) for x in cipher_grille]

    # Needs 4 iterations
    for in_loop in range(4):
        for i, row in enumerate(mask):
            for j, item in enumerate(row):
                if item == 'X':
                    password += ciphered_password[i][j]

        # Rotate mask on 90 degrees clockwise
        mask = list(zip(*mask[::-1]))

    return password


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
