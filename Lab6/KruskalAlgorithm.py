from DSF import DisjointSet
from GraphAL import GraphAL
'''
This algorithm is going to find the least spanning tree by adding the endges that
contian the less weight and checking that the two nodes are not connected already.
'''
def kruskalAlgorithm(g, size):
    e = bubbleSort(g.get_edges())
    
    
def bubbleSort(edges):
    n = len(edges)
    for i in range(n):
        for j in range(0, n-i-1):
            if edges[j].weight > edges[j+1].weight:
                edges[j], edges[j+1] = edges[j+1], edges[j]      
    return edges



#First I am going to create a Graph
graph = GraphAL(4, False)#Graph with 10 vertices and non-directed
graph.add_edge(0, 1, 4)
graph.add_edge(1, 2, 5)
graph.add_edge(2, 3, 7)
graph.add_edge(3, 0, 3)
graph.add_edge(3, 1, 2)
graph.add_edge(0, 2, 1)

kruskalAlgorithm(graph, 4)