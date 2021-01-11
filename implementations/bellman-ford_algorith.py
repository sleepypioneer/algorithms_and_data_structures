# Iterate through all vertices - O(V)
#   For each iteration we consider of the (u,v) edges with w edge weight - O(E)
#   Relaxation - O(1)
#       we calculate the possible shortest paths to the given nodes
#       if the path from the current node is shorter we set this as the predecessor and update the distance
# After the V-1 iteration, we make one additional loop to check negative cycles - O(E)
# Total time complexity = O(V*E)
# We can terminate the algorithm early if there is no change in the distances between two iterations
#   (we use the same technique in bubble sort)

class Node:
    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.predecessor = None
        self.min_distance = float('inf')


class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex


class BellmanFordAlgorithm:
    def __init__(self, vertex_list, edge_list, start_vertex):
        self.vertex_list = vertex_list
        self.edge_list = edge_list
        self.start_vertex = start_vertex
        self.has_cycle = False

    def find_shortest_path(self):

        self.start_vertex.min_distance = 0

        for _ in range(len(self.vertex_list)-1):
            for edge in self.edge_list:
                # calculate whether there are shorter paths
                u = edge.start_vertex
                v = edge.target_vertex

                dist = u.min_distance + edge.weight

                if dist < v.min_distance:
                    v.min_distance = dist
                    v.predecessor = u

        for edge in self.edge_list:
            if self.check_cycle(edge):
                print('Negative cycle detected.')
                return

    def check_cycle(self, edge):
        # if the total cost (min_distance) of a given vertex decreases after V-1 iterations
        # there is a negative cycle
        u = edge.start_vertex
        v = edge.target_vertex

        dist = u.min_distance + edge.weight

        if dist < v.min_distance:
            self.has_cycle = True
            return True
        else:
            return False

    def get_shortest_path(self, vertex):
        if not self.has_cycle:
            node = vertex

            while node is not None:
                print(node.name)
                node = node.predecessor
        else:
            print('There is a negative cycle in the G(V,E) graph')


# create the nodes
node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')
node6 = Node('F')
node7 = Node('G')

# create the edges
edge1 = Edge(5, node1, node2)
edge2 = Edge(9, node1, node5)
edge3 = Edge(4, node2, node5)
edge4 = Edge(12, node2, node3)
edge5 = Edge(7, node2, node3)
edge6 = Edge(3, node3, node4)
edge7 = Edge(1, node3, node6)
edge8 = Edge(9, node4, node7)
edge9 = Edge(6, node5, node3)
edge10 = Edge(4, node5, node6)
edge11 = Edge(2, node6, node7)
edge12 = Edge(6, node7, node3) # if we change this edge weight to -6 we will get a negative cycle

# put the edges in the corresponding adjacency list for the nodes
node1.adjacency_list.append(edge1)
node1.adjacency_list.append(edge2)
node2.adjacency_list.append(edge3)
node2.adjacency_list.append(edge4)
node2.adjacency_list.append(edge5)
node3.adjacency_list.append(edge6)
node3.adjacency_list.append(edge7)
node4.adjacency_list.append(edge8)
node5.adjacency_list.append(edge9)
node5.adjacency_list.append(edge10)
node6.adjacency_list.append(edge11)
node7.adjacency_list.append(edge12)


vertices = [node1, node2, node3, node4, node5, node6, node7]
edges = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12]

algorithm = BellmanFordAlgorithm(vertices, edges, node1)

algorithm.find_shortest_path()
algorithm.get_shortest_path(node7)


