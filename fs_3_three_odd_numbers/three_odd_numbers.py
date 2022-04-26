def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """

    for n in range(len(nums)):
        if len(nums) < 3:
            # print(False)
            return False
        for m in range(n, n + 2):
            if m + 3 > len(nums):
                # print(False)
                return False
            if (nums[m] + nums[m + 1] + nums[m + 2]) % 2 != 0:
                # print(True)
                return True
    # print(False)
    return False

three_odd_numbers([1, 2, 3, 4, 5])
three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
three_odd_numbers([5, 2, 1])
three_odd_numbers([1, 2, 3, 3, 2])