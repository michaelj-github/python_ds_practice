def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    returnDict = {}
    for c in phrase.lower():
        if c not in returnDict and c in ['a', 'e', 'i', 'o', 'u']:
            returnDict[c] = phrase.lower().count(c)
    # print(returnDict)
    return returnDict

# vowel_count('rithm school')
# vowel_count('HOW ARE YOU? i am great!')