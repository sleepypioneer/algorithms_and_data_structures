# Binary Search Trees

"""
RECAP:
| Sorted arrays                     | Linked Lists                              |
|-----------------------------------|-------------------------------------------|
| Inserting a new item is slow O(N) | Inserting a new item is very fast O(1)    |
| Searching quite fasts O(logN)     | Searching is sequential O(N)              |
| Removing an item is slow O(N)     | Removing an item is fast O(1)             |

Binary search trees are going to make all of these operations quite fast, with O(logN) time complexity ~ predictable

Tree - Nodes and edges (connection between nodes).
     - There must be only a single path form the root node to any other nodes in the tree!
     - Parent nodes connect to child nodes
     - Nodes with no children are leaf nodes

Binary search trees
    - Data structure
    - Keeps key in sorted order
    - Every node can have at most two children
    - Left child: smaller than parent
    - Right child: great than the parent
    - On every decision we get rid of half of the data in which we are searching ~ O(logN)
    - Height of the tree = number of layers
    - Layer 1 has 1 node, layer 2 has 2 nodes, etc
    - Balanced Tree number of right subtrees and left subtrees are equal, the complexity will be favourable O(logN)
    - This is much better than the linear time O(N) required to find items by key in an unsorted array,
        but slower than the corresponding operations on hash tables.

Binary search tree insertion and search
    - If the data we want to insert is greater than the root node we go to the right, if it is smaller we go to the left
    - We continue checking the data against each node and insert when we get to the correct position
    - For search we do the same, checking through each node and seeing if it less than or greater than that node until
        we find the node we are looking for

Binary search tree deletion
    1) We want to remove a leaf node
        - Find the item O(logN)
        - Set the item to Null (update parent node reference) O(1)
        - O(logN)
    2) We want to remove a node with one child:
        - Find the item O(logN)
        - Update references for parent node to grandchild node O(1)
        - O(logN)
    3) We want to remove a node with two children:
        - Find the node O(logN)
        - Find predecessor (greatest item in left subtree) and identify successor (lowest item in right subtree) O(logN)
        - swap with predecessor/ successor
        - now we can set the node to Null if it is a leaf node or if there is one child we can do as number 2 above
        - O(logN)

Example tree:

             |----------------32-----------------|
    |-------10---|                              55------|
    1        |--19--|                                   79
            16      23

Traversal
    1) In-order traversal
        - we visit the left subtree and the root node and the right subtree recursively

    1 - 10 - 16 - 19 - 23 - 32 - 55 - 79 (NUMERICAL ORDERING)

    2) Pre-order traversal
        - We visit the root then the left subtree and the right subtree recursively

    32 - 10 - 1 - 19 - 16 - 23 - 55 - 79

    3) Post-order traversal
        - we visit the left subtree then the right subtree and the root recursively

    1 - 16 - 23 - 19 - 10 - 79 - 55 - 32


|           | Average case  | Worst Case    | Worst Case Balanced Tree  |
|-----------|---------------|---------------|---------------------------|
| Space     | O(N)          | O(N)          | O(N)                      |
| Insert    | O(logN)       | O(N)          | O(logN)                   |
| Delete    | O(logN)       | O(N)          | O(logN)                   |
| Search    | O(logN)       | O(N)          | O(logN)                   |

Worst case: Is with a unbalanced tree

Applications of tree like structures:
    Powerful for representing hierarchical data (file systems)
        - operating systems
        - game trees (chess and tic-tac-toe)
        - machine learning: decision trees and boosting which uses decision trees under the hood

"""


class Node:
    """
    We store in the node a reference to the left child, right child and parent node.
    """
    def __init__(self, data, parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent


class BinarySearchTree:
    """

    """
    def __init__(self):
        self.root = None

    def insert(self, data):
        """
        O(logN) if Tree is balanced (left subtree contains approx. same amount of items as right subtree)
        BUT if the tree is not balanced could be linear complexity O(N)
        """
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            # we go to the left subtree
            if node.leftChild:
                self.insert_node(data, node.leftChild)
            else:
                node.leftChild = Node(data, node)
        else:
            # we go to the right subtree
            if node.rightChild:
                self.insert_node(data, node.rightChild)
            else:
                node.rightChild = Node(data, node)

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        """
        O(logN)
        """
        if node.leftChild:
            # traverse left subtree recursively
            self.traverse_in_order(node.leftChild)

        print(f'{node.data}')

        if node.rightChild:
            # travers right subtree recursively
            self.traverse_in_order(node.rightChild)

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        if node.rightChild:
            return self.get_max(node.rightChild)
        else:
            return node.data

    def get_max_iterative(self, node):
        actual = self.root

        while actual.rightChild is not None:
            actual = actual.rightChild

        return actual.data

    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self, node):
        if node.leftChild:
            return self.get_min(node.leftChild)
        else:
            return node.data

    def remove_value(self, data):
        self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if node is None:
            return
        if data < node.data:
            # check the left subtree
            self.remove_node(data, node.leftChild)
        elif data > node.data:
            # check the right subtree
            self.remove_node(data, node.rightChild)
        else:
            # We found the node we want to remove
            # We want to delete a leaf node
            if node.leftChild is None and node.rightChild is None:
                print(f'Removing a leaf node...{node.data}')

                parent = node.parent

                if parent is not None and parent.leftChild == node:
                    # node we want to remove is left child of it's parent node
                    parent.leftChild = None

                if parent is not None and parent.rightChild == node:
                    # node we want to remove is right child of it's parent node
                    parent.rightChild = None

                if parent is None:
                    # node we want to remove is the root node
                    self.root = None

                del node

            # we want to remove a node with one child
            elif node.leftChild is None and node.rightChild is not None:
                print(f'Removing a node with single right child...{node.data}')

                parent = node.parent

                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.rightChild
                    if parent.rightChild == node:
                        parent.rightChild = node.rightChild
                else:
                    # node we want to remove is the root node
                    self.root = node.rightChild
                # we must also update the child to have the parent as it's parent
                node.rightChild.parent = parent
                del node

            # we want to remove a node with one left child
            elif node.rightChild is None and node.leftChild is not None:
                print(f'Removing a node with single left child...{node.data}')

                parent = node.parent

                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.leftChild
                    if parent.rightChild == node:
                        parent.rightChild = node.leftChild
                else:
                    # node we want to remove is the root node
                    self.root = node.leftChild
                # we must also update the child to have the parent as it's parent
                node.leftChild.parent = parent
                del node

            # we want to remove a node with two children
            else:
                print(f'Removing a node with two children nodes...{node.data}')

                predecessor = self.get_predecessor(node.leftChild)

                # swap predecessor and root node
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.rightChild:
            return self.get_predecessor(node.rightChild)
        return node




bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(66)
bst.insert(32)
bst.insert(2)
bst.insert(28)
bst.insert(-5)

bst.traverse()

print(f'Max item: {bst.get_max_value()}')  # right most item
print(f'Min item: {bst.get_min_value()}')  # left most item

print(f'Max item with iteration: {bst.get_max_iterative(bst.root)}')  # right most item

bst.remove_value(10)

