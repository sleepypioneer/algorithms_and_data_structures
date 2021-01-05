
class Node:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False


def depth_first_search(start_node):
    """
    - select starting node, add it to the queue
    - add its neighbours to the stack if they have not been visited
    - check last item appended to the stack (LIFO) this ensures we traverse as far as posisble first
    - uses LIFO structure (stack)
    """

    stack = [start_node]  #LIFO structure

    while stack:
        # pop() has O(1) time complexity
        actual_node = stack.pop()  # returns and removes last item
        actual_node.visited = True
        print(actual_node.name)

        for n in actual_node.adjacency_list:
            # avoid revisiting node
            if not n.visited:
                stack.append(n)



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
depth_first_search(node1)