from abc import ABC, abstractmethod

class Vertex:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __repr__(self):
        return self.key

class Edge:
    def __init__(self, capacity, residual=False):
        self.capacity = capacity
        self.flow = 0
        self.residual = residual

        if residual:
            self.residual_capacity = 0
        else:
            self.residual_capacity = capacity

    def __repr__(self):
        return f"{self.capacity} {self.flow} {self.residual_capacity} {self.residual}"

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end=" -> ")
        for n, w in g.neighbours(v):
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
    
    def delete_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph or vertex2 not in self.graph:
            return 
        else:
            if vertex2 in self.graph[vertex1]:
                del self.graph[vertex1][vertex2]
    
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

def add_flow_edge(graph, vertex1, vertex2, capacity):
    graph.insert_edge(vertex1, vertex2, Edge(capacity, False))
    graph.insert_edge(vertex2, vertex1, Edge(0, True))

def bfs(graph, start, end):
    visited = set()
    parent = {}
    queue = []

    visited.add(start)
    queue.append(start)

    while queue:
        current = queue.pop(0)

        for neighbor, edge in graph.neighbours(current):
            if neighbor not in visited and edge.residual_capacity > 0:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

                if neighbor == end:
                    return parent

    return parent



if __name__ == "__main__":
    g = ListGraph()

    s = Vertex("s")
    u = Vertex("u")
    t = Vertex("t")

    g.insert_vertex(s)
    g.insert_vertex(u)
    g.insert_vertex(t)

    add_flow_edge(g, s, u, 2)
    add_flow_edge(g, u, t, 1)

    printGraph(g)
