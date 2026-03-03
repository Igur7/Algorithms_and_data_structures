from matrix import matrix, transpose
from chio import chio_det

m1 = matrix([
    [1, 0, 2],
    [-1, 3, 1]
])

print(transpose(m1))

print(" ")
m_add = matrix((2, 3), 1)
print(m1 + m_add)
print(" ")
m_mul = matrix([
    [3, 1],
    [2, 1],
    [1, 0]
])
print(m1 * m_mul)

m1chio = matrix([

[5 , 1 , 1 , 2 , 3],

[4 , 2 , 1 , 7 , 3],

[2 , 1 , 2 , 4 , 7],

[9 , 1 , 0 , 7 , 0],

[1 , 4 , 7 , 2 , 2]

])

m2chio = matrix(  [
     [0 , 1 , 1 , 2 , 3],
     [4 , 2 , 1 , 7 , 3],
     [2 , 1 , 2 , 4 , 7],
     [9 , 1 , 0 , 7 , 0],
     [1 , 4 , 7 , 2 , 2]
    ])
m3chio = matrix([
     [0 , 0 , 0 , 0 , 0],
     [4 , 2 , 1 , 7 , 3],
     [2 , 1 , 2 , 4 , 7],
     [9 , 1 , 0 , 7 , 0],
     [1 , 4 , 7 , 2 , 2]
    ])
m4chio = matrix( [
     [0 , 1 , 1 , 2 , 3],
     [0 , 2 , 1 , 7 , 3],
     [0 , 1 , 2 , 4 , 7],
     [0 , 1 , 0 , 7 , 0],
     [0 , 4 , 7 , 2 , 2]
    ])
print(chio_det(m1chio))
print(chio_det(m2chio))
print(chio_det(m3chio))
print(chio_det(m4chio))