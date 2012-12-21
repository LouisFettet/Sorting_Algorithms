# Fettet, Louis
# Merge Sort Algorithm Implementation
# 12/17/12

def mergeSort(l):
    if len(l) <= 1:
        return l
    left, right = [], []
    middle = len(l)//2
    for i in range(0,middle):
        left.append(i)
    for i in range(middle, len(l)):
        right.append(i)
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    while (len(left) > 0) or (len(right) > 0):
        if (len(left) > 0) and (len(right) > 0):
            if left[0] <= right[0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)
        elif len(left) > 0:
            result.append(left[0])
            left.pop(0)
        elif len(right) > 0:
            result.append(right[0])
            right.pop(0)
        break
    return result
