class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def __repr__(self):
        return f"Edge({self.v1}, {self.v2})"


class Graf:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = len(matrix)
        self.weight_full = self.find_weight()

    def find_weight(self):
        w = 0
        for i in range(self.size):
            for j in range(i + 1, self.size):
                w += abs(self.matrix[i][j])
        return w

    def get_min(self, mas, visited):
        min_idx = -1
        for i in range(len(mas)):
            if visited[i]:
                continue
            if min_idx == -1 or mas[i] < mas[min_idx]:
                min_idx = i
        return min_idx

    def deikstra(self, vertex):
        ways = [self.weight_full] * self.size
        visited = [False] * self.size
        parent = [-1] * self.size
        ways[vertex] = 0

        for _ in range(self.size):
            min_v = self.get_min(ways, visited)
            if min_v == -1:
                break
            visited[min_v] = True
            for i in range(self.size):
                if visited[i]:
                    continue
                if self.matrix[min_v][i] == 0:
                    continue
                weight = ways[min_v] + self.matrix[min_v][i]
                if weight < ways[i]:
                    ways[i] = weight
                    parent[i] = min_v

        edges = []
        for v in range(self.size):
            if v != vertex and parent[v] != -1:
                edges.append(Edge(parent[v], v))

        return ways, edges


if __name__ == "__main__":
    matrix = [
        [0, 7, 9, 0, 0, 14],
        [7, 0, 10, 15, 0, 0],
        [9, 10, 0, 11, 0, 2],
        [0, 15, 11, 0, 6, 0],
        [0, 0, 0, 6, 0, 9],
        [14, 0, 2, 0, 9, 0],
    ]
    graf = Graf(matrix)

    for vertex in range(graf.size):
        ways, edges = graf.deikstra(vertex)

        print(f"Минимальные пути из вершины {vertex}:")
        print(" ".join(f"{way}" for way in ways))

        print("Дерево кратчайших путей:")
        for edge in edges:
            print(f"{edge}")
        print()