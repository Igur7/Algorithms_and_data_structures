from matrix import matrix, transpose

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
