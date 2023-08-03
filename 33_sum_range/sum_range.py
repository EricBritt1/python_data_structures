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
    sum_tracker = 0;
    if end == None:
        if 0 <= start < len(nums) - 1 :
            for numbers in range(start, len(nums)):
                sum_tracker += nums[numbers]
            return sum_tracker
    elif 0 <= start < len(nums) - 1 and start < end <= len(nums):
        for numbers in range(start, end + 1):
                sum_tracker += nums[numbers]
        return sum_tracker
    elif end > len(nums)  - 1:
        if 0 <= start < len(nums) - 1 :
            for numbers in range(start, len(nums)):
                sum_tracker += nums[numbers]
            return sum_tracker
    

    
   
    
    # if 0 < end < len(nums):
      #  for numbers in range(start, len(nums)):
         #   if end == None:
            #    sum_tracker += nums[numbers]
           #  elif end == numbers:
             #   return sum_tracker\

        

    

    
            

    
    
    

            
        
    
            

