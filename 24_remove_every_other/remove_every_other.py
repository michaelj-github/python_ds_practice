def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    # print([a for a in lst if lst.index(a) % 2 == 0])
    return [a for a in lst if lst.index(a) % 2 == 0]


# remove_every_other([1, 2, 3, 4, 5])
