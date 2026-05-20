from abc import ABC, abstractmethod
from copy import deepcopy

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
    
    def insert_edge(self, vertex1, vertex2, edge=1):
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


def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")


def build_graph(edge_list):
    graph = MatrixGraph()
    vertices = {}

    for vertex1_key, vertex2_key, edge in edge_list:
        if vertex1_key not in vertices:
            vertices[vertex1_key] = Vertex(vertex1_key)
            graph.insert_vertex(vertices[vertex1_key])

        if vertex2_key not in vertices:
            vertices[vertex2_key] = Vertex(vertex2_key)
            graph.insert_vertex(vertices[vertex2_key])

        graph.insert_edge(vertices[vertex1_key], vertices[vertex2_key], edge)

    return graph

def generate_m_matricies(used_columns, current_row,M,variants):
    rows, cols = M.size()

    if current_row == rows:
        variants.append(deepcopy(used_columns))
        return

    for col in range(cols):
        if col not in used_columns:
            used_columns[col] = True

            for j in range(cols):
                M[current_row][j] = 0
            M[current_row][col] = 1

            generate_m_matricies(used_columns, current_row + 1,M,variants)
            used_columns[col] = False

def is_isomorphism(M,P,G):
    return P == (M * G * transpose(M))

def ullman_algorithm_v1(used_columns, current_row, M, P, G, isomorphisms,calls = 0):

    calls += 1
    rows, cols = M.size()

    if current_row == rows:
        if is_isomorphism(M, P, G):
            isomorphisms.append(deepcopy(M))
        return calls
    
    for col in range(cols):
        if col not in used_columns:
            used_columns[col] = True

            for j in range(cols):
                M[current_row][j] = 0
            M[current_row][col] = 1

            calls = ullman_algorithm_v1(used_columns, current_row + 1, M, P, G, isomorphisms,calls)
            used_columns[col] = False
    return calls

def vertex_degree(adjacency_matrix, row_index):
    degree = 0
    for value in adjacency_matrix[row_index]:
        if value != 0:
            degree += 1
    return degree

def create_M0(P_matrix, G_matrix):
    rows = P_matrix.size()[0]
    cols = G_matrix.size()[0]
    M0 = matrix((rows, cols), 0)

    for i in range(rows):
        degree_p = vertex_degree(P_matrix, i)
        for j in range(cols):
            degree_g = vertex_degree(G_matrix, j)
            if degree_p <= degree_g:
                M0[i][j] = 1

    return M0


def ullmann_v2(used_columns, current_row, M, P_matrix, G_matrix, isomorphisms, calls=0):
    calls += 1
    rows, cols = M.size()

    if current_row == rows:
        if is_isomorphism(M, P_matrix, G_matrix):
            isomorphisms.append(deepcopy(M))
        return calls

    for col in range(cols):
        if not used_columns[col] and M[current_row][col] != 0:
            used_columns[col] = True

            M_copy = deepcopy(M)
            for j in range(cols):
                M_copy[current_row][j] = 0
            M_copy[current_row][col] = 1

            calls = ullmann_v2(
                used_columns,
                current_row + 1,
                M_copy,
                P_matrix,
                G_matrix,
                isomorphisms,
                calls
            )

            used_columns[col] = False

    return calls

if __name__ == "__main__":
    graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
    graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]

    G = build_graph(graph_G)
    P = build_graph(graph_P)

    M = matrix((P.matrix.size()[0], G.matrix.size()[0]), 0)
    isomorphisms_v1 = []
    calls_v1 = ullman_algorithm_v1([False] * G.matrix.size()[0],0,M,P.matrix,G.matrix,isomorphisms_v1)

    M0 = create_M0(P.matrix, G.matrix)
    isomorphisms_v2 = []
    calls_v2 = ullmann_v2(
        [False] * G.matrix.size()[0],
        0,
        M0,
        P.matrix,
        G.matrix,
        isomorphisms_v2
    )

    print(len(isomorphisms_v1), calls_v1)
    print(len(isomorphisms_v2), calls_v2)
