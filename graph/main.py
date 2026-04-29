from abc import ABC, abstractmethod

class matrix:
    def __init__(self, data,fill = 0):
        if isinstance(data,tuple):
            rows, cols = data
            self.__matrix = [[fill for _ in range(cols)] for _ in range(rows)]
            self.__rows = rows
            self.__cols = cols
        else:
            self.__matrix = data
            self.__rows = len(self.__matrix)
            self.__cols = len(self.__matrix[0]) if self.__rows > 0 else 0

    def size(self):
        return (self.__rows, self.__cols)
    
    def __getitem__(self, key: int):
        return self.__matrix[key]


    def __add__(self, other: 'matrix') -> 'matrix':

        if self.size() != other.size():
            raise ValueError("Macierze musza miec takie same rozmiary do dodawania")

        rows, cols = self.size()
        result = matrix((rows, cols),fill = 0 )

        for i in range(rows):
            for j in range(cols):
                result[i][j] = self[i][j] + other[i][j]

        return result
   
    def __mul__(self, other :'matrix'):
        rows_a, cols_a = self.size()
        rows_b, cols_b = other.size()

        if cols_a != rows_b:
            raise ValueError("Liczba kolumn pierwszej macierzy musi byc rowna liczbie wierszy drugiej")

        result = matrix((rows_a, cols_b),fill = 0)

        for i in range(rows_a):
            for j in range(cols_b):
                s = 0
                for k in range(cols_a):
                    s += self[i][k] * other[k][j]
                result[i][j] = s

        return result
    
    def __eq__(self, other: 'matrix'):
        if self.size() != other.size():
            return False
        rows, cols = self.size()
        for i in range(rows):
            for j in range(cols):
                if self[i][j] != other[i][j]:
                    return False
        return True 
    
    def __str__(self):
        lines = []
        for row in self.__matrix:
            lines.append("|" + "   ".join(str(x) for x in row) + "|")
        return "\n".join(lines)
    
def transpose(m: matrix) -> matrix:
    rows, cols = m.size()
    result = matrix((cols, rows), 0)
    for i in range(rows):
        for j in range(cols):
            result[j][i] = m[i][j]
    return result


class Vertex:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __repr__(self):
        return self.key

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

class MatrixGraph(Graph):
    def __init__(self, init_value=0):
        self.vertices_list = []
        self.matrix = matrix((0, 0), init_value)
        self.init_value = init_value

    def is_empty(self):
        return len(self.vertices_list) == 0   

    def _get_vertex_index(self, vertex):
        for i, v in enumerate(self.vertices_list):
            if v == vertex:
                return i
        return None

    def insert_vertex(self, vertex):
        if self._get_vertex_index(vertex) is not None:
            return
        
        size_old = len(self.vertices_list)
        matrix_new = matrix((len(self.vertices_list) + 1, len(self.vertices_list) + 1), self.init_value)

        for i in range(size_old):
            for j in range(size_old):
                matrix_new[i][j] = self.matrix[i][j]

        self.vertices_list.append(vertex)
        self.matrix = matrix_new
    
    def insert_edge(self, vertex1, vertex2, edge):
        idv1 = self._get_vertex_index(vertex1)
        idv2 = self._get_vertex_index(vertex2)

        if idv1 is None or idv2 is None:
            return 
        else:
            self.matrix[idv1][idv2] = edge
            self.matrix[idv2][idv1] = edge
    
    def delete_edge(self, vertex1, vertex2):
        idv1 = self._get_vertex_index(vertex1)
        idv2 = self._get_vertex_index(vertex2)

        if idv1 is None or idv2 is None:
            return 
        else:
            self.matrix[idv1][idv2] = self.init_value
            self.matrix[idv2][idv1] = self.init_value
    
    def delete_vertex(self, vertex):
        idv = self._get_vertex_index(vertex)

        if idv is None:
            return
        else:
            del self.vertices_list[idv]
            matrix_new = matrix((len(self.vertices_list), len(self.vertices_list)), self.init_value)

            for i in range(len(self.vertices_list)):
                for j in range(len(self.vertices_list)):
                    if i < idv and j < idv:
                        matrix_new[i][j] = self.matrix[i][j]
                    elif i < idv and j >= idv:
                        matrix_new[i][j] = self.matrix[i][j + 1]
                    elif i >= idv and j < idv:
                        matrix_new[i][j] = self.matrix[i + 1][j]
                    else:
                        matrix_new[i][j] = self.matrix[i + 1][j + 1]

            self.matrix = matrix_new
    
    def get_edge(self, vertex1, vertex2):
        idv1 = self._get_vertex_index(vertex1)
        idv2 = self._get_vertex_index(vertex2)

        if idv1 is None or idv2 is None:
            return None

        edge = self.matrix[idv1][idv2]

        if edge == self.init_value:
            return None
        else:
            return edge

    def vertices(self):
        return self.vertices_list[:]

    def neighbours(self, vertex_id):
        idv = self._get_vertex_index(vertex_id)

        if idv is None:
            return []
        
        neighbours_list = []

        for i, edge in enumerate(self.matrix[idv]):
            if edge != self.init_value:
                neighbours_list.append((self.vertices_list[i], edge))

        return neighbours_list

    def get_vertex(self, vertex_id):
        idv = self._get_vertex_index(vertex_id)

        if idv is None:
            return None

        return self.vertices_list[idv]
        
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
    
    def insert_edge(self, vertex1, vertex2, edge):
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


def test_graph(graph_class):
    from polska import graf, draw_map

    graph = graph_class()
    vertices = {}

    for vertex1, vertex2 in graf:
        if vertex1 not in vertices:
            vertices[vertex1] = Vertex(vertex1)
            graph.insert_vertex(vertices[vertex1])

        if vertex2 not in vertices:
            vertices[vertex2] = Vertex(vertex2)
            graph.insert_vertex(vertices[vertex2])

        graph.insert_edge(vertices[vertex1], vertices[vertex2], 1)

    graph.delete_vertex(vertices["K"])
    graph.delete_edge(vertices["W"], vertices["E"])

    draw_map(graph)


if __name__ == "__main__":
    test_graph(ListGraph)
    test_graph(MatrixGraph)
