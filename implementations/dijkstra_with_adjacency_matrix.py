import sys


class DijkstraAlgorithmAdjacencyMatrix:
    def __init__(self, adjacency_matrix, start_vertex):
        self.adjacency_matrix = adjacency_matrix
        self.start_vertex = start_vertex
        self.v = len(adjacency_matrix)
        self.visited = [False for _ in range(len(adjacency_matrix))]
        self.min_distances = [float('inf') for _ in range(len(adjacency_matrix))]
        self.min_distances[start_vertex] = 0

    def get_min_vertex(self):
        """
        Find the vertex with the shortest min distance
        :return:
        """
        min_vertex_value = sys.maxsize
        min_vertex_index = 0

        # linear search in O(V)
        # If we would use a heap instead we would be able to achieve O(logN)
        for index in range(self.v):
            if not self.visited[index] and self.min_distances[index] < min_vertex_value:
                min_vertex_value = self.min_distances[index]
                min_vertex_index = index

        return min_vertex_index

    def calculate(self):

        for vertex in range(self.v):
            # get the minimum distance per vertex
            actual_vertex = self.get_min_vertex()
            print(f'Considering vertex: {vertex}')
            self.visited[actual_vertex] = True

            # it has again O(V) linear running time - so overall time is quadratic O(V^2)
            for other_vertex in range(self.v):
                # check if there is a connection between the two nodes
                if self.adjacency_matrix[actual_vertex][other_vertex] > 0:
                    # is there a shorter path to the other_vertex from the actual_vertex?
                    if self.min_distances[actual_vertex] + self.adjacency_matrix[actual_vertex][other_vertex] \
                            < self.min_distances[other_vertex]:
                        self.min_distances[other_vertex] = self.min_distances[actual_vertex] + \
                            self.adjacency_matrix[actual_vertex][other_vertex]

    def print_distances(self):
        print(self.min_distances)


m = [
    [0, 7, 5, 2, 0, 0],
    [7, 0, 0, 0, 3, 8],
    [5, 0, 0, 10, 4, 0],
    [2, 0, 10, 0, 0, 2],
    [0, 3, 4, 0, 0, 6],
    [0, 8, 0, 2, 6, 0]
]

algorithm = DijkstraAlgorithmAdjacencyMatrix(m, 0)

algorithm.calculate()

algorithm.print_distances()


