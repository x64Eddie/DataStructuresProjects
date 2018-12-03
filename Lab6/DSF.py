
class dsf():
    
    def __init__(self, size):
        self.nList = [-1] * size
        self.size = size
    
    #We are going to united two sets.
    def union(self, n0, n1):
        if n0 < 0 or n0 > self.size and n1 < 0 and n1 > self.size:
            return
        #first we are going to find the roots of the nodes
        while self.nList[n0] > 0:
            n0 = self.nList[n0]
        while self.nList[n1] > 0:
            n1 = self.nList[n1]
        if n0 == n1:
            return
        self.nList[n0] = n1

    '''
    This method is going to be used for the graph class, is going to tell me
    if two edges are already connected in the graph
    '''
    def areConnected(self, v0, v1):
        #We are first going to find the roots of the values, this is going to tells us if they are connected
        while self.nList[v0] > 0:
            v0 = self.nList[v0]
        while self.nList[v1] > 0:
            v0 = self.nList[v1]
        #If they are the same, then they are already connected
        if v0 == v1:
            return True
        else
            return False
        
