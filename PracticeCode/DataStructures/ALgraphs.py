class Graph:
    def __init__(self):
        self.graph = {}

    # Function for adding Vertices
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
        else:
            print(f"{vertex} already exists !")

    # Function for adding Edge
    def add_edge(self, ver1, ver2):
        if ver1 in self.graph and ver2 in self.graph:
            self.graph[ver1].append(ver2)
            self.graph[ver2].append(ver1)
        else:
            print("Vertex not found !")

    # Function for Displaying Graph
    def show_edges(self):
        for ver, nei in self.graph.items():
            print(f"{ver} -> {nei}")

# Example Usage:
g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.show_edges()