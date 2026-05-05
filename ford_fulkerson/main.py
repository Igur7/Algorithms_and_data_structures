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
    def delete_edge(self, vertex1, vertex2, residual=None):
        pass

    @abstractmethod
    def get_edge(self, vertex1, vertex2, residual=None):
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
            self.graph[vertex] = []
    
    def insert_edge(self, vertex1, vertex2, edge = None):
        if vertex1 not in self.graph or vertex2 not in self.graph:
            return 
        else:
            self.graph[vertex1].append((vertex2, edge))
    
    def delete_edge(self, vertex1, vertex2, residual=None):
        if vertex1 not in self.graph or vertex2 not in self.graph:
            return

        new_list = []
        removed = False

        for neighbor, edge in self.graph[vertex1]:
            if not removed and neighbor == vertex2:
                if residual is None or edge.residual == residual:
                    removed = True
                    continue
            new_list.append((neighbor, edge))

        self.graph[vertex1] = new_list

    
    def delete_vertex(self, vertex):
        if vertex not in self.graph:
            return 
        else:
            del self.graph[vertex]

            for v in self.graph:
                self.graph[v] = [
                    (neighbor, edge)
                    for neighbor, edge in self.graph[v]
                    if neighbor != vertex
                ]
            
    def get_edge(self, vertex1, vertex2, residual=None):
        if vertex1 not in self.graph or vertex2 not in self.graph:
            return None

        for neighbor, edge in self.graph[vertex1]:
            if neighbor == vertex2:
                if residual is None or edge.residual == residual:
                    return edge

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
            for neighbor, edge in self.graph[vertex_id]:
                ans.append((neighbor, edge))
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
                parent[neighbor] = (current, edge)
                queue.append(neighbor)

                if neighbor == end:
                    return parent

    return parent

def path_capacity(graph, start, end, parent):
    if end not in parent:
        return 0
    
    current = end
    min_capacity = float('inf')

    while current != start:
        prev, edge = parent[current]
        min_capacity = min(min_capacity, edge.residual_capacity)
        current = prev

    return min_capacity

def augment_path(graph, start, end, parent, min_capacity):
    if min_capacity == 0:
        return

    current = end

    while current != start:
        prev, edge = parent[current]

        if edge.residual:
            reverse_edge = graph.get_edge(current, prev, residual=False)
        else:
            reverse_edge = graph.get_edge(current, prev, residual=True)

        edge.residual_capacity -= min_capacity
        reverse_edge.residual_capacity += min_capacity

        if not edge.residual:
            edge.flow += min_capacity
        else:
            reverse_edge.flow -= min_capacity

        current = prev

def ford_fulkerson(graph, start, end):
    parent = bfs(graph, start, end)
    min_capacity = path_capacity(graph, start, end, parent)

    while min_capacity > 0:
        augment_path(graph, start, end, parent, min_capacity)
        parent = bfs(graph, start, end)
        min_capacity = path_capacity(graph, start, end, parent)

    max_flow = 0

    for v in graph.vertices():
        for neighbor, edge in graph.neighbours(v):
            if neighbor == end and not edge.residual:
                max_flow += edge.flow

    return max_flow

def build_graph(edges):
    graph = ListGraph()
    vertices = {}

    for v1, v2, capacity in edges:
        if v1 not in vertices:
            vertices[v1] = Vertex(v1)
            graph.insert_vertex(vertices[v1])

        if v2 not in vertices:
            vertices[v2] = Vertex(v2)
            graph.insert_vertex(vertices[v2])

        add_flow_edge(graph, vertices[v1], vertices[v2], capacity)

    return graph, vertices


def real_outflow(graph, vertex):
    total = 0

    for neighbor, edge in graph.neighbours(vertex):
        if not edge.residual:
            total += edge.flow

    return total



if __name__ == "__main__":
    graf_0 = [('s', 'u', 2), ('u', 't', 1), ('u', 'v', 3), ('s', 'v', 1), ('v', 't', 2)]

    graf_1 = [('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('a', 'b', 12),
              ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4)]

    graf_2 = [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1),
              ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]

    graf_3 = [('s', 'a', 3), ('s', 'd', 2), ('a', 'b', 4), ('b', 'c', 5), ('c', 't', 6),
              ('a', 'f', 3), ('f', 't', 3), ('d', 'e', 2), ('e', 'f', 2)]

    tests = [
        (graf_0, 'u'),
        (graf_1, 'a'),
        (graf_2, 'a'),
        (graf_3, 'a')
    ]

    for edges, out_vertex in tests:
        graph, vertices = build_graph(edges)
        result = ford_fulkerson(graph, vertices['s'], vertices['t'])

        print(result)
        printGraph(graph)
        print(real_outflow(graph, vertices[out_vertex]))

