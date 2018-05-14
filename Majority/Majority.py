"""
Given a list of elements [a1, a2, an], with each ai being a string, write a function majority that returns the value that 
appears the most in the list. If there's no winner, the function should return None
"""

from collections import Counter

class majorityFinder(object):



    def majority(arr):
    """ 
        input: array of letters
        return: unique charset that appears most, None if list empty or a tie
    """
        count=Counter(arr)
        #if arr is empty, return none
        if not count:
            return None
        #find max value in list (# occurances)
        max_value = max(count.values()) 
        #extract key associated with max_value
        parse_max = [key for key, value in count.items() if value == max_value]
        #if there are multiple keys returned, there must be a tie, return none
        if len(parse_max) > 1:
            return None
        return(' '.join(parse_max))
