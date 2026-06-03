import time

def find_pattern_rec(P,T,i,j):

    if i == 0:
        return j
    if j == 0:
        return i
    
    insert_cost = find_pattern_rec(P,T,i,j-1) + 1
    delete_cost = find_pattern_rec(P,T,i-1,j) + 1

    if P[i] == T[j]:
        replace_cost = find_pattern_rec(P,T,i-1,j-1)
    else:
        replace_cost = find_pattern_rec(P,T,i-1,j-1) + 1
    
    return min(insert_cost,delete_cost,replace_cost)

def string_compare_pd(P,T):
    m = len(P)
    n = len(T)

    D = [[0 for i in range(n)] for j in range(m)]
    parrent = [['X' for i in range(n)] for j in range(m)]

    for i in range(1,m):
        D[i][0] = i
        parrent[i][0] = 'D'
    
    for j in range(1,n):
        D[0][j] = j
        parrent[0][j] = 'I'

    for i in range(1,m):
        for j in range(1,n):
            insert_cost = D[i][j-1] + 1
            delte_cost = D[i-1][j] + 1

            if P[i] == T[j]:
                replace_cost = D[i-1][j-1]
            else:
                replace_cost = D[i-1][j-1] + 1

            min_cost = min(insert_cost,delte_cost,replace_cost)
            D[i][j] = min_cost

            if min_cost == replace_cost:
                if P[i] == T[j]:
                    parrent[i][j] = 'M'
                else:
                    parrent[i][j] = 'R'
            elif min_cost == delte_cost:
                parrent[i][j] = 'D'
            else:
                parrent[i][j] = 'I'

    return D[m-1][n-1], parrent

def reconstruct_path(parent):
    i = len(parent) - 1
    j = len(parent[0]) - 1
    result = []

    while parent[i][j] != 'X':
        operation = parent[i][j]
        result.append(operation)

        if operation == 'M' or operation == 'R':
            i -= 1
            j -= 1
        elif operation == 'D':
            i -= 1
        elif operation == 'I':
            j -= 1

    result.reverse()
    return ''.join(result)

if __name__ == "__main__":
    P = ' kot'
    T = ' pies'

    cost = find_pattern_rec(P, T, len(P) - 1, len(T) - 1)
    print(cost)


    P = ' biały autobus'
    T = ' czarny autokar'

    cost, parent = string_compare_pd(P, T)
    print(cost)
    print(reconstruct_path(parent))
    
    P = ' thou shalt not'
    T = ' you should not'

    cost, parent = string_compare_pd(P, T)
    path = reconstruct_path(parent)

    print(path)