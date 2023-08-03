def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those. DONE
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) DONE
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values: DONE

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    empty_list = {};
    if len(keys) <= len(values):
        return {keys[num] : values[num] for num in range(0, len(keys))}

    if len(keys) > len(values):
        for num in range(0, len(keys)):
            if num < len(values):
                empty_list[keys[num]] = values[num]
            if num >= len(values):
                empty_list[keys[num]] = None
        return empty_list


    



