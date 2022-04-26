def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    list_phrase = list(phrase)
    x = 0
    for c in list_phrase:
        if c.lower() == to_swap.lower():
            list_phrase[x] = c.swapcase()
        x+=1
    # print("".join(list_phrase))
    return "".join(list_phrase)

# flip_case('Aaaahhh', 'a')
# flip_case('Aaaahhh', 'A')
# flip_case('Aaaahhh', 'h')