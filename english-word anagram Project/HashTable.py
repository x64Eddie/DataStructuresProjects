from __future__ import division
class HT():
    l = []
    tableSize = -1
    numItems = 0
    
    def __init__(self, size):
        self.l = [None] * size
        self.tableSize = size
    
    #The load factor is going to be the numberOfItems
    #table size
    def getLoadFactor(self):
        return self.numItems / self.tableSize

    #Its going to separate the word into characters and get the number that
    #its represents, then by using folding method we are going to
    #get a number that we are going to get the module by the table size
    def get_position(self, word):
        return self.hashing2(word)

    #Inserting the word into the hashtable
    def insert(self, word):
        e = HTNode(word)
        pos = self.get_position(e.word)
        n = self.l[pos]
        if n is not None:
            e.next = n
            e.size = n.size
        self.l[pos] = e
        e.size += 1
        self.numItems += 1

    #We are going to search for the word in the hashtable
    def search(self, word):
        pos = self.get_position(word)
        n = self.l[pos]
        c = 0 #This is going to represent the comparisons that it took to find the word
        while n is not None:
            if n.word == word:
                 return n,c
            n = n.next
            c += 1
        return n,c

    def hashing0(self, word):
        n = 0
        l = list(word)
        for c in l:
            n += ord(c)
        return n % self.tableSize
    
    def hashing1(self, word):
        return len(word) % self.tableSize

    def hashing2(self, word):
        n = 0
        l = list(word)
        count = 1
        for c in l:
            n += (ord(c)*(count^len(word)*2)+len(word)*20)
            count += 1
        return n % self.tableSize

        

class HTNode():
    word = ""
    next = ""
    size = 0
    def __init__(self, word, next = None):
        self.word = word
        self.next = next