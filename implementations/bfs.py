# Breadth first search (BFS)

class Node:
    def __init__(self, name):
        self.name = name
        self.adjacency_list = [] # we will set the nieghbours manually
        self.visited = False


def breadth_first_search(start_node):
    """
    - select starting node, add it to the queue
    - add its neighbors to the queue
    - remove the node to be visited and dequeue
    - visit first neighbour in queue and add its neighbours to the queue
    - mark neighbour as visited and remove it from the queue
    - note we only add neighbours we have not yet visited
    - We continue until the queue is empty.
    """

    queue = [start_node]  #FIFO structure

    while queue:
        # we want to return and remove the first item
        actual_node = queue.pop(0)
        actual_node.visited = True
        print(actual_node.name)

        # consider the neighbours of actual node
        for n in actual_node.adjacency_list:
            if not n.visited:
                queue.append(n)


# create nodes
node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")

# set up neighbours
node1.adjacency_list.append(node2)
node2.adjacency_list.append(node3)
node3.adjacency_list.append(node4)
node4.adjacency_list.append(node5)

# run BFS
breadth_first_search(node1)