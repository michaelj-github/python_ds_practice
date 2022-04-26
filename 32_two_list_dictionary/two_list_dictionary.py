def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    the_dict = {}
    x = 0
    for k in keys:
        if len(values) >= x + 1:
            the_dict[k] = values[x]
            x+=1
        else:
            the_dict[k] = None
    # print(the_dict)
    return the_dict

# two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
# two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
# two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])