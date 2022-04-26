def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    phrase_set = set(phrase)
    returnDict = {}
    for c in phrase:
        if c not in returnDict:
            returnDict[c] = phrase.count(c)
#     print(returnDict)
    return returnDict

# multiple_letter_count('yay')
# multiple_letter_count('Yay')