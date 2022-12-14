def encryption(words):
    cryp_words = ''

    for syb in words:
        if syb == '.':
            cryp_words += '.'
        elif syb == ' ':
            cryp_words += ' '
        elif syb == 'ё':
           cryp_words += chr(ord('е') + 3)
        elif syb == 'Ё':
            cryp_words += chr(ord('Е') + 3)
        elif syb == 'э':
            cryp_words += chr(ord('а'))
        elif syb == 'Э':
            cryp_words += chr(ord('А'))
        elif syb == 'ю':
            cryp_words += chr(ord('а') + 1)
        elif syb == 'Ю':
            cryp_words += chr(ord('А') + 1)
        elif syb == 'я':
            cryp_words += chr(ord('а') + 2)
        elif syb == 'Я':
            cryp_words += chr(ord('А') + 2)
        elif syb == 'x':
            cryp_words += chr(ord('a'))
        elif syb == 'X':
            cryp_words += chr(ord('A'))
        elif syb == 'y':
            cryp_words += chr(ord('a') + 1)
        elif syb == 'Y':
            cryp_words += chr(ord('A') + 1)
        elif syb == 'z':
            cryp_words += chr(ord('a') + 2)
        elif syb == 'Z':
            cryp_words += chr(ord('A') + 2)
        else:
            cryp_words += chr(ord(syb) + 3)
    return cryp_words

if __name__ == '__main__':
    string = input('Введите сообщение: ')
    print('Зашифрованное сообщение:', encryption(string))
