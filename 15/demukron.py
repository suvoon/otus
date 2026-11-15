class Graf:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = len(matrix)
        self.level = []

    def demukron(self):
        size = self.size
        weight = [0] * size
        for i in range(size):
            for j in range(size):
                weight[i] += self.matrix[j][i]

        visited = [False] * size
        self.level = []

        while True:
            current = [v for v in range(size) if not visited[v] and weight[v] == 0]
            if not current:
                break
            self.level.append(current)
            for v in current:
                visited[v] = True
                for j in range(size):
                    weight[j] -= self.matrix[v][j]


if __name__ == "__main__":
    matrix = [
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0],
    ]

    graf = Graf(matrix)
    graf.demukron()

    print("Уровни (int[][] level):")
    for i, lvl in enumerate(graf.level):
        print(f"  level[{i}] = {lvl}")