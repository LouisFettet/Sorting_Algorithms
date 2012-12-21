# Fettet, Louis
# Heap Sort Algorithm Implementation
# 12/16/12

from random import randint

class HeapArray():
    def __init__(self):
        self.data = []
        self.data.append(None)

    def parent(self, item):
        if item == (0 or 1):
            return None
        return item//2

    def leftChild(self, item):
        if item == 0:
            return None
        return item*2

    def rightChild(self, item):
        if item == 0:
            return None
        return item * 2 + 1

    def siftUp(self):
        i = len(self.data) - 1
        while i >= 1:
            p = self.parent(i)
            if p == None:
                break
            if self.data[p] > self.data[i]:
                self.data[p], self.data[i] = self.data[i], self.data[p]
                i = p
            else:
                break
                
    def siftDown(self):
        i = 1
        n = len(self.data) - 1
        while 2 * i <= n:
            c = self.leftChild(i)
            if c + 1 <= n:
                if self.data[c + 1] < self.data[c]:
                    c = c + 1
            if self.data[i] > self.data[c]:
                self.data[i], self.data[c] = self.data[c], self.data[i]
                i = c
            else:
                i += 1

    def insert(self, l):
        self.data.append(l)
        self.siftUp()        

    def extract(self):
        l = self.data[1]
        self.data[1]=self.data[len(self.data) - 1]
        self.data.pop(1)
        self.siftDown()
        return l


def heapSort(a, n):
    h = HeapArray()
    b = []
    for i in range(0, n):
        h.insert(a[i])
        print (h.data)
    for i in range(0,n):
        b.append(h.extract())
        print (h.data)
    return b


def genUnsortedList(size):
    l = []
    for i in range(size):
        l.append(randint(0, 100000))
    return l


def heapTest():    
    l = genUnsortedList(50)
    print("Our unsorted list contains the following values:")
    print(l)
    h = heapSort(l, len(l))     
    print(h)
