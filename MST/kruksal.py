from graf_mst import graf


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.p = []
        self.size = []

        for i in range(n):
            self.p.append(i)
            self.size.append(1)

    def find(self, v):
        while self.p[v] != v:
            v = self.p[v]

        return v

    def union_sets(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return

        if self.size[root_a] < self.size[root_b]:
            self.p[root_a] = root_b
            self.size[root_b] = self.size[root_b] + self.size[root_a]
        else:
            self.p[root_b] = root_a
            self.size[root_a] = self.size[root_a] + self.size[root_b]

    def same_component(self, a, b):
        if self.find(a) == self.find(b):
            return True
        else:
            return False


def change_letter_to_number(letter):
    return ord(letter) - ord('A')


def kruskal(edges):
    max_number = 0

    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]

        number1 = change_letter_to_number(v1)
        number2 = change_letter_to_number(v2)

        if number1 > max_number:
            max_number = number1

        if number2 > max_number:
            max_number = number2

    uf = UnionFind(max_number + 1)

    sorted_edges = sorted(edges, key=lambda edge: edge[2])

    mst = []

    for edge in sorted_edges:
        v1 = edge[0]
        v2 = edge[1]
        weight = edge[2]

        number1 = change_letter_to_number(v1)
        number2 = change_letter_to_number(v2)

        if uf.same_component(number1, number2) == False:
            uf.union_sets(number1, number2)
            mst.append(edge)

    return mst


if __name__ == "__main__":
    mst = kruskal(graf)

    for edge in mst:
        print(edge)
