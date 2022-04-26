def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    thesum = 0
    for x in range(len(matrix)):
        y = len(matrix) - (x + 1)
        thesum += matrix[x][x]
        thesum += matrix[x][y]
    # print(thesum)
    return thesum

# sum_up_diagonals([[1, 2], [30, 40]])
# sum_up_diagonals([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# sum_up_diagonals([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10], [8, 9, 10, 11]]) # 52
# sum_up_diagonals([[1, 2, 3, 4, 5], [4, 5, 6, 7, 8], [7, 8, 9, 10, 11], [8, 9, 10, 11, 12], [9, 10, 11, 12, 13]]) # 78