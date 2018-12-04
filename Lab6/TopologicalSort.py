from GraphAL import GraphAL

'''
This is going to sort a graph depending in the direction of the nodes
'''
def topologicalSort(g, size):
    v = [False] * size
    s = []
    def topologicalUtil(j):
        v[j] = True
        for i in g.get_vertices_reachable_from(j):
            if not v[i]:
                topologicalUtil(i)
        s.insert(0, j)
    for i in range(size):
        if not v[i]:
            topologicalUtil(i)
    print(s)

graph = GraphAL(4, True)
graph.add_edge(0, 1, 4)
graph.add_edge(1, 2, 5)
graph.add_edge(2, 3, 7)
graph.add_edge(3, 0, 3)
graph.add_edge(3, 1, 2)
graph.add_edge(0, 2, 1)

topologicalSort(graph, 4)