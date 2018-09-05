"""
Implement the function unique_in_order which takes as argument a 
sequence and returns a list of items without any elements with the same value next to each other and preserving the original order 
of elements.
"""

def unique_in_order(iterable):
    hold = []
    for index, each in enumerate(iterable):
        cur = each
        if index+1 < len(iterable):
            nxt = iterable[index+1]
            if cur == nxt:
                pass
            else:
                hold.append(cur)
        else:
            hold.append(cur)
    return hold
