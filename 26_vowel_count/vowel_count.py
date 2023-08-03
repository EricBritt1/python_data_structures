def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    lowercase_phrase = phrase.lower()
    vowels = 'aeiou';
    vowel_count = {};
    for i in vowels:
        if not i in vowel_count:
            if lowercase_phrase.count(i) > 0:
                vowel_count[i] = lowercase_phrase.count(i)
    return vowel_count;


