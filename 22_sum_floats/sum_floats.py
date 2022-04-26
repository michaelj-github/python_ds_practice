def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """

    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!

    the_floats = [num for num in nums if isinstance(num, float)]
    the_sum = 0
    for a_float in the_floats:
        the_sum += a_float
    # print(the_floats, the_sum)
    return the_sum

# sum_floats([1.5, 2.4, 'awesome', [], 1])
# sum_floats([1, 2, 3])