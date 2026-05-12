from graf_mst import graf
from abc import ABC, abstractmethod

class Vertex:
    def __init__(self, key,weight = None):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __repr__(self):
        return self.key

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------") 

class Graph(ABC):
    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def insert_vertex(self, vertex):
        pass

    @abstractmethod
    def insert_edge(self, vertex1, vertex2, edge):
        pass

    @abstractmethod
    def delete_vertex(self, vertex):
        pass

    @abstractmethod
    def delete_edge(self, vertex1, vertex2):
        pass

    @abstractmethod
    def get_edge(self, vertex1, vertex2):
        pass

    @abstractmethod
    def vertices(self):
        pass

    @abstractmethod
    def neighbours(self, vertex_id):
        pass

    @abstractmethod
    def get_vertex(self, vertex_id):
        pass

class ListGraph(Graph):
    def __init__(self):
        self.graph = {}

    def is_empty(self):
        if len(self.graph) == 0:
            return True
        else:
            return False
    
    def insert_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}
        else:
            return
    
    def insert_edge(self, vertex1, vertex2, edge = None):
        if vertex1 not in self.graph or vertex2 not in self.graph:
            return 
        else:
            self.graph[vertex1][vertex2] = edge
            self.graph[vertex2][vertex1] = edge
    
    def delete_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph or vertex2 not in self.graph:
            return 
        else:
            if vertex2 in self.graph[vertex1]:
                del self.graph[vertex1][vertex2]
            if vertex1 in self.graph[vertex2]:
                del self.graph[vertex2][vertex1]
    
    def delete_vertex(self, vertex):
        if vertex not in self.graph:
            return 
        else:
            del self.graph[vertex]

            for v in self.graph:
                if vertex in self.graph[v]:
                    del self.graph[v][vertex]
            
    def get_edge(self,vertex1, vertex2):
        if vertex1 not in self.graph or vertex2 not in self.graph:
            return None
        else:
            if vertex2 in self.graph[vertex1]:
                return self.graph[vertex1][vertex2]
            else:
                return None
            
    def vertices(self):
        if len(self.graph) == 0:
            return []
        else:
            return list(self.graph.keys())
    
    def neighbours(self, vertex_id):
        if vertex_id not in self.graph:
            return []
        else:
            ans = []
            for neighbor in self.graph[vertex_id]:
                ans.append((neighbor, self.graph[vertex_id][neighbor]))
            return ans
    
    def get_vertex(self, vertex_id):
        if vertex_id not in self.graph:
            return None
        else:
            return vertex_id

def prim(g):
    if g.is_empty():
        return ListGraph()

    intree = {v: False for v in g.vertices()}
    distance = {v: float('inf') for v in g.vertices()}
    parent = {v: None for v in g.vertices()}

    MST = ListGraph()
    for vertex in g.vertices():
        MST.insert_vertex(vertex)

    actual_vertex = g.vertices()[0]
    MST.insert_vertex(actual_vertex)

    while actual_vertex not in intree or not intree[actual_vertex]:
        intree[actual_vertex] = True
        for neighbor, weight in g.neighbours(actual_vertex):
            if weight < distance[neighbor] and not intree[neighbor]:
                distance[neighbor] = weight
                parent[neighbor] = actual_vertex
        min_distance = float('inf')
        next_vertex = None

        for vertex in g.vertices():
            if not intree[vertex] and distance[vertex] < min_distance:
                min_distance = distance[vertex]
                next_vertex = vertex
        if next_vertex is None:
            break
        
        MST.insert_edge(parent[next_vertex], next_vertex, distance[next_vertex])
        actual_vertex = next_vertex
    
    return MST


def create_graph(data):
    g = ListGraph()
    vertices = {}

    for v1, v2, weight in data:
        if v1 not in vertices:
            vertices[v1] = Vertex(v1)
            g.insert_vertex(vertices[v1])

        if v2 not in vertices:
            vertices[v2] = Vertex(v2)
            g.insert_vertex(vertices[v2])

        g.insert_edge(vertices[v1], vertices[v2], weight)

    return g
            
if __name__ == "__main__":
    g = create_graph(graf)
    mst = prim(g)
    printGraph(mst)
