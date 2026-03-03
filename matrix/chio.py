from matrix import matrix, transpose

def chio_det(m: matrix) -> int:
    rows, cols = m.size()
    if rows != cols:
        raise ValueError("Macierz musi byc kwadratowa")
    if rows == 2: 
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    