class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def __repr__(self):
        return f"Edge({self.v1}, {self.v2})"


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, v):
        if self.parent[v] == v:
            return v
        return self.find(self.parent[v])

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        self.parent[rb] = ra
        return True


def kruskal(matrix):
    size = len(matrix)
    weight_min = 0
    edges = []

    candidates = []
    for i in range(size):
        for j in range(i + 1, size):
            if matrix[i][j] == 0:
                continue
            candidates.append((matrix[i][j], i, j))

    candidates.sort(key=lambda x: x[0])

    uf = UnionFind(size)

    for weight, a, b in candidates:
        if uf.union(a, b):
            edges.append(Edge(a, b))
            weight_min += weight

    return edges, weight_min

if __name__ == "__main__":
    matrix = [
        [0, 2, 2, 0, 1, 0, 3],
        [2, 0, 3, 3, 0, 0, 0],
        [2, 3, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 2, 0, 0],
        [1, 0, 0, 2, 0, 4, 0],
        [0, 0, 0, 0, 4, 0, 2],
        [3, 0, 0, 0, 0, 2, 0],
    ]

    edges, weight_min = kruskal(matrix)

    print("Рёбра минимального остовного дерева:")
    for e in edges:
        print(f"  {e}")
    print(f"Минимальный вес: {weight_min}")