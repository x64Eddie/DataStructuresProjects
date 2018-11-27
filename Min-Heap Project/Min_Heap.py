import unittest

class Heap:
    def __init__(self):
        self.heap_array = []
    
    #Going to insert the item into the heap
    def insert(self, k):
        self.heap_array.append(k)
        self.reorderUp(k)

    #Going to reorder the heap from the bottom of the tree to the root
    def reorderUp(self, k):
        i = self.heap_array.index(k)
    
        while i > 0:
            p = self.get_parent(i)
            if(p >= 0):
                if(self.heap_array[i] < self.heap_array[p]):
                   self.swap(p, i)
            i = p
    
    #Going to reorder the heap from the root to the leafs, following only one peth
    def reorderDown(self, k):
        i = self.heap_array.index(k)
        while i < len(self.heap_array):
                l, r = self.get_childs(i)
                if(r < len(self.heap_array)):

                    #Going to see what child is the smalles,
                    #the parent will be swaped with the smallest child
                    if(self.heap_array[l] < self.heap_array[r] 
                    and self.heap_array[l] < self.heap_array[i]):
                        self.swap(i, l)
                        i = l
                        continue
                    elif(self.heap_array[r] < self.heap_array[l] 
                    and self.heap_array[r] < self.heap_array[i]):
                        self.swap(i, r)
                        i = r
                        continue
                i = r
    
    #Going to swap all the items given      
    def swap(self, i0, i1):
        t = self.heap_array[i0]
        self.heap_array[i0] = self.heap_array[i1]
        self.heap_array[i1] = t

    #Going to get the child of the given index
    def get_childs(self, k):
        return (k * 2) + 1, (k * 2) +2
    
    #Going to get the parent of the given index
    def get_parent(self, k):
        return (k - 1) // 2
    
    #Goind to extrac the min from the heap
    def extract_min(self):
        if self.is_empty():
            return None
        
        min_elem = self.heap_array[0]
        l = len(self.heap_array)
        self.heap_array[0] = self.heap_array[l - 1]
        self.reorderDown(self.heap_array[0])
        self.heap_array = self.heap_array[:l-1]
        

        return min_elem

    #Checking if the size of the heap is empty
    def is_empty(self):
        return len(self.heap_array) == 0

#Going to insert all the items in heap and extrac them all ordered.
def heapSort(l):
    h = Heap()
    for num in l:
        h.insert(num)
    while not h.is_empty() :
        print(h.extract_min())

#Going to read the numebers from the file
def getFileNums(fileName):
    f = open(fileName, "r")
    numbers = []
    for l in f:
        numbers.extend(list(map(int, l.split(","))))
    return numbers

#Going to sort the numbers in the file
heapSort(getFileNums("numbers.txt"))