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
    
    def delete_edqge(self, vertex1, vertex2):
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

class ListGraph(Graph):
    pass