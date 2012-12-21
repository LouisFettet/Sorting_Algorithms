# Fettet, Louis
# Bubble Sort
# 12/15/12

def bubbleSort(l):
    """
    Returns list 'l' as a sorted list in O(n**2) runtime no matter what.
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l
