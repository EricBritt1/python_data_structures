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

    tl_to_br = 0;
    tl_tracker = 0;
    bl_to_tr = 0;
    bl_tracker = 0;

    list_amount = len(matrix) 
    for i in matrix:
        if tl_tracker != list_amount:
            tl_to_br += i[tl_tracker]
            tl_tracker += 1

    for j in range(len(matrix)-1, -1, -1):
        if bl_tracker != list_amount:
            bl_to_tr += matrix[j][bl_tracker]
            bl_tracker += 1
    return tl_to_br + bl_to_tr
    

    



