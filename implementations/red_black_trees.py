# Red Black Trees

"""
Running time of BST operations depends on the height of the binary search tree
AVL trees are raster than red-black trees BUT needs more work (for balancing)
Operating systems relies heavily on these data structures
Both average case and worst case running time are O(logN)
The longest path can be twice the shortest (so the tree is approximately balanced)

Important features:
    - Root node is always black
    - All leaves are black
    - Every red node must have two black child nodes and no other children. It must have a black parent.
        We assign Null pointers to the leaf nodes so they are valid when red.
    - Every path from a given node to any of its descendants contains the same number of black nodes
    - Every new node is red by default
    - On every insertion we have to check whether we have violated the red-black properties or not
    - If a violation has occurred the tree needs to be rebalanced
        1) make rotations
        2) recolor the nodes (this happens very fast)

Rotations are the same as AVL trees:

        |----------[D]----------|       right rotation -->         |----------[B]----------|
    |---[B]---|                 [E]     left rotation  <--        [A]                 |---[D]---|
   [A]       [C]                                                                    [C]        [F]

** We just have to update the references which cna be done in O(1) time complexity!! **

Red black property violations:
    When we recolor we have to recursively check the tree as we may have violated the red-black principles elsewhere.
    1) We insert a red node as a right child to a red parent with red uncle.
        Root becomes black and parent and uncle become black.
    2) We insert a red node to a red parent as a right child with a black uncle.
        Make a left (or right) rotation on the parent. The inserted node becomes the parent of the original parent.
    3) Uncle node is black, node is left child of a left child(or right of a right).
        We have to make a rotation on the inserted nodes grandparent. After rotation we have to make some recoloring.
    4) Uncle is red, node is left child of a left child (or right of a right).
        We recolor the parent and uncle to be black.
"""


class Color:
    RED = 1
    BLACK = 2


class Node:

    def __init__(self, data, parent=None, color=Color.RED):
        self.data = data
        self.color = color
        self.parent = parent
        self.leftChild = None
        self.rightChild = None


class RedBlackTree:

    def __init__(self):
        self.root = None

        def traverse(self):
            if self.root is not None:
                self.traverse_in_order(self.root)

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.leftChild:
            self.traverse_in_order(node.leftChild)

        l = 'NULL'
        r = 'NULL'
        p = 'NULL'

        if node.leftChild is not None:
            l = node.leftChild.data

        if node.rightChild is not None:
            r = node.rightChild.data

        if node.parent is not None:
            p = node.parent.data

        print(f'Node data: {node.data} left: {l} right: {r} parent: {p} color: {node.color}')

        # now we have to consider the right subtree
        if node.rightChild:
            self.traverse_in_order(node.rightChild)

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            self.violation_check(self.root)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):

        if data < node.data:
            if node.leftChild:
                self.insert_node(data, node.leftChild)
            else:
                node.leftChild = Node(data, node)
                self.violation_check(node.leftChild)
        else:
            if node.rightChild:
                self.insert_node(data, node.rightChild)
            else:
                node.rightChild = Node(data, node)
                self.violation_check(node.rightChild)

    def violation_check(self, node):

        parent_node = None
        grandparent_node = None

        while node != self.root and node.parent.color == Color.RED:
            parent_node = node.parent
            grandparent_node = parent_node.parent

            if grandparent_node is None:
                return

            if parent_node == grandparent_node.leftChild:

                # uncle is other child of grandparent
                uncle = grandparent_node.rightChild

                if uncle and uncle.color == Color.RED:
                    # case 1 and case 4: we recolor the nodes
                    print(f'Recoloring node {grandparent_node.data} to RED')
                    grandparent_node.color = Color.RED
                    print(f'Recoloring node {parent_node.data} to BLACK')
                    parent_node.color = Color.BLACK
                    node = grandparent_node  # so we can check the other parts of the tree for violations
                else:
                    # case 2: uncle node is black and node is right child
                    if node == parent_node.rightChild:
                        self.rotate_left(parent_node)
                        node = parent_node
                        parent_node = node.parent  # again now we have to check the other parts of the tree

                    # case 3: uncle is black and node is left child
                    parent_node.color = Color.BLACK
                    grandparent_node.color = Color.RED
                    print(f'Recoloring node {parent_node.data} to RED')
                    print(f'Recoloring node {grandparent_node.data} to BLACK')
                    self.rotate_right(grandparent_node)

            # symmetric solution for the above
            else:
                uncle = grandparent_node.leftChild

                if uncle and uncle.color == Color.RED:
                    # case 1 and case 4: we recolor the nodes
                    print(f'Recoloring node {grandparent_node.data} to RED')
                    grandparent_node.color = Color.RED
                    print(f'Recoloring node {parent_node.data} to BLACK')
                    parent_node.color = Color.BLACK
                    node = grandparent_node  # so we can check the other parts of the tree for violations
                else:
                    # case 2: uncle node is black and node is left child
                    if node == parent_node.leftChild:
                        self.rotate_right(parent_node)
                        node = parent_node
                        parent_node = node.parent  # again now we have to check the other parts of the tree

                    # case 3: uncle is black and node is right child
                    parent_node.color = Color.BLACK
                    grandparent_node.color = Color.RED
                    print(f'Recoloring node {parent_node.data} to RED')
                    print(f'Recoloring node {grandparent_node.data} to BLACK')
                    self.rotate_left(grandparent_node)

        if self.root.color == Color.RED:
            print(f'Recoloring root node to RED')
            self.root.color = Color.BLACK

    def rotate_right(self, node):
        """
        O(1) constant running time complexity
        """
        print(f'Rotating to the right on node {node.data}')

        # using temporary values we create a temporary left node that takes updated references for it's child nodes
        temp_left_node = node.leftChild
        t = temp_left_node.rightChild

        temp_left_node.rightChild = node
        node.leftChild = t

        if t is not None:
            t.parent = node
        # we have to update the parent which is referenced by our temporary node
        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        # and now we have to update the parents references to point to our temporary node
        if temp_left_node.parent is not None and temp_left_node.parent.leftChild == node:
            temp_left_node.parent.leftChild = temp_left_node

        if temp_left_node.parent is not None and temp_left_node.parent.rightChild == node:
            temp_left_node.parent.rightChild = temp_left_node

        # if the node is the root we swap it for our temporary node
        if node == self.root:
            self.root = temp_left_node

    def rotate_left(self, node):
        """
        O(1) constant running time complexity
        """
        print(f'Rotating to the left on node {node.data}')

        # using temporary values we create a temporary right node that takes updated references for it's child nodes
        temp_right_node = node.rightChild
        t = temp_right_node.leftChild

        temp_right_node.leftChild = node
        node.rightChild = t

        if t is not None:
            t.parent = node
        # we have to update the parent which is referenced by our temporary node
        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        # and now we have to update the parents references to point to our temporary node
        if temp_right_node.parent is not None and temp_right_node.parent.leftChild == node:
            temp_right_node.parent.leftChild = temp_right_node

        if temp_right_node.parent is not None and temp_right_node.parent.rightChild == node:
            temp_right_node.parent.rightChild = temp_right_node

        # if the node is the root we swap it for our temporary node
        if node == self.root:
            self.root = temp_right_node


rbt = RedBlackTree()
rbt.insert(32)
rbt.insert(10)
rbt.insert(55)
rbt.insert(1)
rbt.insert(19)
rbt.insert(79)
rbt.insert(16)
rbt.insert(23)
rbt.insert(12)

rbt.traverse()