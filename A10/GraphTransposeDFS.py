class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[] for _ in range(num_vertices)]
        self.transposed_graph = [[] for _ in range(num_vertices)]
        self.result = {}

    def read_graph_from_file(self, filename):
        with open(filename, 'r') as file:
            for i, line in enumerate(file):
                values = list(map(int, line.strip().split()))
                for j, value in enumerate(values):
                    if value == 1:
                        self.graph[i].append(j)

    def transpose_graph(self):
        for u in range(self.num_vertices):
            for v in self.graph[u]:
                self.transposed_graph[v].append(u)

    def dfs(self, u, visited, label):
        visited[u] = True
        self.result[u] = label

        for v in self.transposed_graph[u]:
            if not visited[v]:
                self.dfs(v, visited, label)

    def find_smallest_reachable(self):
        visited = [False] * self.num_vertices
        label = 1

        for v in range(self.num_vertices):
            if not visited[v]:
                self.dfs(v, visited, label)
                label += 1

        # Find the smallest label for each group of connected vertices
        smallest_labels = {}
        for u, label in self.result.items():
            if label not in smallest_labels or u < smallest_labels[label]:
                smallest_labels[label] = u

        # Update the result with the smallest labels
        for u, label in self.result.items():
            self.result[u] = smallest_labels[label] + 1

    def print_result(self):
        for vertex, label in sorted(self.result.items()):
            print(f"{vertex + 1}:{label}")

# Example usage:
g = Graph(6)
g.read_graph_from_file("graph_data_matrix.txt")
g.transpose_graph()
g.find_smallest_reachable()
g.print_result()
