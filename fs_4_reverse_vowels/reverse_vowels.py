from re import S


def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    ls = list(s)
    lsv = [v for v in s if v.lower() in ['a', 'e', 'i', 'o', 'u']]
    if len(lsv) == 0:
        # print(s)
        return s
    lsv.reverse()
    z = 0
    for x in range(len(lsv)):
        for y in range(z, len(ls)):
            z += 1
            if ls[y].lower() in ['a', 'e', 'i', 'o', 'u']:
                ls[y] = lsv[x]
                x = len(lsv) + 1
                break
    # print("".join(ls))
    return "".join(ls)

reverse_vowels("Hello!")
reverse_vowels("Tomatoes")
reverse_vowels("Reverse Vowels In A String")
reverse_vowels("aeiou")
reverse_vowels("why try, shy fly?")