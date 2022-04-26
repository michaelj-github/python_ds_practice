def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    list_phrase = list(phrase)
    list_phrase[0] = list_phrase[0].upper()
    # print("".join(list_phrase))
    return "".join(list_phrase)

# capitalize('python')
# capitalize('only first word')