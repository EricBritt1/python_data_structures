def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]

    I referred to https://www.programiz.com/python-programming/examples/factor-number for help with this question. I totally forgot how to properly utilize range. This supplemented my answer. I thought maybe there would be a factoring method.
    """

    factor_list = [];
    for i in range(1, num + 1):
        if (num % i == 0):
            factor_list.append(i)
    return factor_list

