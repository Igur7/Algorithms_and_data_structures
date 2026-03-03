class matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def __add__(self, other: 'matrix'):
        pass
    def __mul__(self, other :'matrix'):
        pass
    def __eq__(self, other: 'matrix'):
        pass
    def __getitem__(self, key: int):
        pass
    
    def size(self):
        return (self.rows, self.cols)

def transpose(m: matrix) -> matrix:
    pass

