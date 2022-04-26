def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    # print(len([alist for alist in lst if not isinstance(alist, list)]) == 0)
    return len([alist for alist in lst if not isinstance(alist, list)]) == 0

# list_check([[1], [2, 3]])
# list_check([[1], "nope"])
