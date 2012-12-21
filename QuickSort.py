# Fettet, Louis
# Quick Sort Algorithm Implementation
# 12/15/12


def quickSort(a, l, u):
    if l < u:
        p = partition(a, l, u)
        quickSort(a, l, p-1)
        quickSort(a, p+1, u)
        return a

def partition(a, l, u):
    t = randint(l,u)
    T = a[t]
    a[t],a[u] = a[u],a[t]
    m = l
    for i in range(l,u):
        if a[i] < T:
            a[i], a[m] = a[m], a[i]
            m += 1
    a[m], a[u] = a[u], a[m]
    return m
