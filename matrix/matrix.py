class matrix:
    def __init__(self, data):
        if isinstance(data,tuple):
            rows, cols = data
            self.__matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        else:
            self.__matrix = data
        self.__rows = len(self.__matrix)
        self.__cols = len(self.__matrix[0]) 

    def size(self):
        return (self.__rows, self.__cols)
    
    def __getitem__(self, key: int):
        return self.__matrix[key]


    def __add__(self, other: 'matrix') -> 'matrix':

        if self.size() != other.size():
            raise ValueError("Macierze musza miec takie same rozmiary do dodawania")

        rows, cols = self.size()
        result = matrix((rows, cols))

        for i in range(rows):
            for j in range(cols):
                result[i][j] = self[i][j] + other[i][j]

        return result
   
    def __mul__(self, other :'matrix'):
        rows_a, cols_a = self.size()
        rows_b, cols_b = other.size()

        if cols_a != rows_b:
            raise ValueError("Liczba kolumn pierwszej macierzy musi byc rowna liczbie wierszy drugiej")

        result = matrix((rows_a, cols_b))

        for i in range(rows_a):
            for j in range(cols_b):
                s = 0
                for k in range(cols_a):
                    s += self[i][k] * other[k][j]
                result[i][j] = s

        return result
        
    def __eq__(self, other: 'matrix'):
        pass

def transpose(m: matrix) -> matrix:
    pass

