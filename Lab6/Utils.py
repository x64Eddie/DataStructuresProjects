from GraphAL import GraphAL

def getGraph(fileName):
    e = []
    f = open(fileName, 'r')
    for l in f:
        e.append(list(map(int, l.split(","))))
    graph = GraphAL(len(e))
    for l in e:
        graph.add_edge(l[0], l[1], l[2])
    return graph
        