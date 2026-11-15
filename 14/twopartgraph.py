class TwopPartGraph:
    def __init__(self, U, V, edges):
        self.U = U
        self.V = V
        self.edges = edges
        
        self.points = sorted(list(U) + list(V))
        self.num_points = len(self.points)
        self.num_edges = len(self.edges)

    def point_to_index(self, point):
        return self.points.index(point)

    def get_edge_list(self):
        return self.edges

    def get_adjacency_lists(self):
        adj_lists = {p: [] for p in self.points}
        for u, v in self.edges:
            adj_lists[u].append(v)
            adj_lists[v].append(u)
        return adj_lists

    def get_adjacency_vectors(self):
        adj_lists = self.get_adjacency_lists()
        vectors = {}
        for p in self.points:
            vector = [0] * self.num_points
            for neighbor in adj_lists[p]:
                idx = self.point_to_index(neighbor)
                vector[idx] = 1
            vectors[p] = vector
        return vectors

    def get_adjacency_array(self):
        matrix = [[0] * self.num_points for _ in range(self.num_points)]
        for u, v in self.edges:
            i, j = self.point_to_index(u), self.point_to_index(v)
            matrix[i][j] = 1
            matrix[j][i] = 1
        return matrix

    def get_incidence_matrix(self):
        matrix = [[0] * self.num_edges for _ in range(self.num_points)]
        for edge_idx, (u, v) in enumerate(self.edges):
            i_u, i_v = self.point_to_index(u), self.point_to_index(v)
            matrix[i_u][edge_idx] = 1
            matrix[i_v][edge_idx] = 1
        return matrix


if __name__ == "__main__":
    U_set = {1, 2, 3}
    V_set = {4, 5, 6, 7}
    graph_edges = [(1, 6), (1, 7), (2, 4), (2, 7), (3, 5)]

    graph = TwopPartGraph(U_set, V_set, graph_edges)

    print("1. Перечень рёбер:")
    print(graph.get_edge_list())
    print("-" * 40)

    print("2. Списки смежности:")
    adj_lists = graph.get_adjacency_lists()
    for p in graph.points:
        print(f"  {p}: {adj_lists[p]}")
    print("-" * 40)

    print("3. Векторы смежности:")
    adj_vectors = graph.get_adjacency_vectors()
    for p in graph.points:
        print(f"  {p}: {adj_vectors[p]}")
    print("-" * 40)

    print("4. Массивы смежности:")
    adj_array = graph.get_adjacency_array()
    print("   ", *graph.points)
    for i, row in enumerate(adj_array):
        print(f"{graph.points[i]}: {row}")
    print("-" * 40)

    print("5. Матрица инцидентности:")
    inc_matrix = graph.get_incidence_matrix()
    print("    e1 e2 e3 e4 e5")
    for i, row in enumerate(inc_matrix):
        print(f"{graph.points[i]}:  {row}")