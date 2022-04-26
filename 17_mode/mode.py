def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    modeNums = nums[0]
    maxCount = 1 # assuming there is always at least one item in the list
    numsSet = set(nums)
    for n in numsSet:
        thisCount = nums.count(n)
        if thisCount > maxCount:
            maxCount = thisCount
            modeNums = n
    # print(modeNums)
    return modeNums

# mode([1, 2, 1])
# mode([2, 2, 3, 3, 2])

