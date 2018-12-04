from DSF import DisjointSet
from GraphAL import GraphAL
import Utils
import unittest


'''
This algorithm is going to find the least spanning tree by adding the endges that
contian the less weight and checking that the two nodes are not connected already.
'''
def kruskalAlgorithm(g, size):
    dsf = DisjointSet(size)
    e = bubbleSort(g.get_edges())
    for i in range(len(e)):
        if not dsf.are_in_same_set(e[i].src, e[i].dest):
            dsf.merge_sets(e[i].src, e[i].dest)
            print(e[i].src, e[i].dest, e[i].weight)
    
def bubbleSort(edges):
    n = len(edges)
    for i in range(n):
        for j in range(0, n-i-1):
            if edges[j].weight > edges[j+1].weight:
                edges[j], edges[j+1] = edges[j+1], edges[j]      
    return edges

#First I am going to create a Graph
graph = GraphAL(4, False)
graph.add_edge(0, 1, 4)
graph.add_edge(1, 2, 5)
graph.add_edge(2, 3, 7)
graph.add_edge(3, 0, 3)
graph.add_edge(3, 1, 2)
graph.add_edge(0, 2, 1)


kruskalAlgorithm(graph, 4)