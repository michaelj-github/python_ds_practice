def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    the_end = None
    if end != None:
        the_end = end + 1
    the_sum = 0
    for n in nums[start:the_end]:
        the_sum += n
    # print(the_sum)
    return the_sum


# sum_range([1, 2, 3, 4])
# sum_range([1, 2, 3, 4], 1)
# sum_range([1, 2, 3, 4], end=2)
# sum_range([1, 2, 3, 4], 1, 3)
# sum_range([1, 2, 3, 4], 1, 99)