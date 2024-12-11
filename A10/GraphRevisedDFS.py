from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.result = {}

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def read_graph_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                vertices = list(map(int, line.strip().split("->")))
                for i in range(len(vertices) - 1):
                    self.add_edge(vertices[i], vertices[i + 1])

    def dfs(self, u, visited, parent):
        visited[u] = True
        self.result[u] = u  # Initialize with the current vertex itself

        for v in self.graph[u]:
            if not visited[v]:
                self.dfs(v, visited, u)
            self.result[u] = min(self.result[u], self.result[v])

    def find_smallest_reachable(self):
        vertices = list(self.graph.keys())
        visited = {v: False for v in vertices}

        for vertex in vertices:
            if not visited[vertex]:
                self.dfs(vertex, visited, None)

    def print_result(self):
        for vertex, smallest_reachable in self.result.items():
            print(f"{vertex}:{smallest_reachable}")

# Example usage:
g = Graph()
g.read_graph_from_file("graph_data_list.txt")
g.find_smallest_reachable()
g.print_result()
