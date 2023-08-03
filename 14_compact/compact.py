def compact(lst):
    """Return a copy of lst with non-true elements removed.

Won't allow me to remove [] or ()

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    
    newLst = [value for value in lst if bool(value) != False]

    return newLst

   
    

        
    
       
