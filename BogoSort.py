# Fettet, Louis
# bogosort
# 12/20/12

from random import shuffle

def bogosort(l):
    """
    Takes parameter list 'l' and randomly swaps elements until the list is
    sorted.
    """
    while sorted(l) != l:
        shuffle(l)
    return l
        
