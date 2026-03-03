from matrix import matrix, transpose

def chio_det(m: matrix):
    rows, cols = m.size()
    if rows != cols:
        raise ValueError("Macierz musi być kwadratowa")
    if rows == 1:
        return m[0][0]
    if rows == 2: 
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    
    a11 = m[0][0]

    if a11 != 0:
        reduced_data = []

        for i in range(1, rows):
            row = []
            for j in range(1,rows):
                value = a11 * m[i][j] - m[i][0] * m[0][j]
                row.append(value)
            reduced_data.append(row)
        reduced = matrix(reduced_data)

        return chio_det(reduced) /(a11 ** (rows - 2))
    else:  
        swap_row = -1
        for i in range(1, rows):
            if m[i][0] != 0:
                swap_row = i
                break

        if swap_row == -1:
            return 0

        data = [[m[i][j] for j in range(cols)] for i in range(rows)]

        data[0], data[swap_row] = data[swap_row], data[0]

        m_s = matrix(data)
        result = -chio_det(m_s)
        if result == 0:
            return 0
        return result


    
