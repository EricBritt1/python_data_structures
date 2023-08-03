def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    new_dict = {}
    for letter in phrase:
        print(letter)
        
        if new_dict.get(letter) == None:
            new_dict[letter] = phrase.count(letter)
    return new_dict
            #new_dict[letter] = 1
       # elif letter in new_dict == True:
            #new_dict[letter] += 1

    


    