class Graph:
    def __init__(self):
        self.vertices = []
        self.graph = []

    # Function for adding Vertices
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            for row in self.graph:
                row.append(0)
            self.graph.append([0]*len(self.vertices))
        else:
            print(f"{vertex} already exists !")

    # Function for adding Edge
    def add_edge(self, ver1, ver2, weight=1):
        if ver1 in self.vertices and ver2 in self.vertices:
            ind1 = self.vertices.index(ver1)
            ind2 = self.vertices.index(ver2)
            self.graph[ind1][ind2] = weight
            self.graph[ind2][ind1] = weight
        else:
            print("Vertex not found !")

    # Function for Displaying Graph
    def show_edges(self):
        for i in range(len(self.vertices)):
            print(self.vertices[i], end=" -> ")
            for j in range(len(self.vertices)):
                if self.graph[i][j] != 0:
                    print(self.vertices[j], end=" ")
            print()

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