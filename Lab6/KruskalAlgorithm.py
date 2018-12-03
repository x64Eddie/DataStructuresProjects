
class dsf():
    
    def __init__(self, size):
        self.nList = [-1] * size
        self.size = size
    
    #We are going to united two sets.
    def union(self, n0, n1):
        if n0 < 0 or n0 > self.size and n1 < 0 and n1 > self.size:
            return
        #first we are going to find the roots of the nodes
        while n0 > 0:
            n0 = self.nList[n0]
        while n1 > 0:
            n1 = self.nList[n1]
        

        



def kruskalAlgorithm():
    pass