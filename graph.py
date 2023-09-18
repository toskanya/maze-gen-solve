class Graph():
    def __init__(self):
        self.graph = {}
    
    def addVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
        
    def addEdge(self, u, v):
        if u not in self.graph:
            self.addVertex(u)
        if v not in self.graph:
            self.addVertex(v)
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def neighbour(self, vertex):
        return self.graph[vertex]

    def print(self):
        print(self.graph)
        
    def getVertex(self, index):
        count = 0
        for vertex in self.graph.keys():
            if count == index:
                return vertex
            count += 1