# AVL tree

"""
Balanced tree that guarantees O(logN) meaning it is predictable
1962: invented by two russian computer scientist (Adelson-Velsky and Landis)
The heights of the two child subtrees of any node differ by at most one (+/- 1)
AVL trees are faster than red-black trees as they are more rigidly balanced but needs more work to construct
Most operations are the same as the BST
For insertion we have to check whether the tree is balanced or unbalances for every insertion (check height)
    and fix the tree if it is unbalanced. Still happens within O(logN)

motivation:
    -  if we build a BST from a sorted array we will get a linked list (unbalanced tree)
        this means the complexity will be reduced to linear running time O(N)


Height of a node: length of the longest path from it to the a leaf

Rotations:
    1) doubly left unbalanced

             |----C
        |----B
        A

        - BEGIN rotateRight(Node node)
            Node tempLeftNode = node.getLeftNone()
            Node t = tempLeftNode.getRightNode()

            tempLeftNode.setRightNode(node)
            node.setLeftNode(t)

            node.updateheight()
            tempLeftNode.updateHeight()
         END

    2) doubly right unbalanced

             B------|
                    D-----|
                          E

        - BEGIN leftRight(Node node)
            Node tempRightNode = node.getRightNone()
            Node t = tempRightNode.getLeftNode()

            tempRightNode.setLeftNode(node)
            node.setRightNode(t)

            node.updateheight()
            tempRightNode.updateHeight()
         END

    3) Left Right situation, root has a left child and the child has a right child

            |------D
            B----|
                 C

        - Right rotation on B so it becomes left child of C
        - Now we can make right rotation on the root node as above

    4) Right Left situation, root has a right child and the child has a left child

            D-------|        difference in height == -1 and 1
            |------F         difference in height == -1 and 0
            E                difference in height == -1 and -1

        ** If F has a right child it doesn't change // we do not modify the pointers for them**

        - Right rotation on F so it becomes left child of C
        - Now we can make left rotation on the root node as above

AVL sort:
    - We can use this data structure to sort items by inserting N items and make an in-order traversal
    - Insertion O(N*logN)
    - in-order traversal O(N)
    - combined complexity O(N*logN)
    - Memory O(N)
    - Running time for AVL sort and quick sort are the same but AVL trees require more amount memory

Applications:
    - Databases when deletions or insertions are not so frequent, but have to make a lot of look ups
    - AVL trees are quicker for lookups than Red Black trees.


"""


class Node:

    def __init__(self, data, parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent
        self.height = 0


class AVLTree:

    def __init__(self):
        self.root = None

    def remove(self, data):
        if self.root:
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

    def insert(self, data):
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
                node.height = max(self.calculate_height(node.leftChild), self.calculate_height(node.rightChild)) + 1
        else:
            # we go to the right subtree
            if node.rightChild:
                self.insert_node(data, node.rightChild)
            else:
                node.rightChild = Node(data, node)
                node.height = max(self.calculate_height(node.leftChild), self.calculate_height(node.rightChild)) + 1

        self.handle_violation(node)  # check if the tree has become unbalanced

    @staticmethod
    def calculate_height(node):
        if node is None:
            return -1
        return node.height

    def handle_violation(self, node):
        """
        Check if we have to make rotations to balance the tree.
        We check the parents of the node until we reach the root node
        Update the height parameter (recalculate)
        We then check the balance factor, if it is more than 1 then the tree is unbalanced.
        We then need to make the necessary rotations to balance the tree.
        :param node:
        :return:
        """
        while node is not None:
            node.height = max(self.calculate_height(node.leftChild), self.calculate_height(node.rightChild)) + 1
            self.violation_helper(node)
            node = node.parent

    def violation_helper(self, node):
        balance_factor = self.calculate_balance(node)

        if balance_factor > 1:
            # the height of the left subtree height > right subtree height (left heavy)

            if self.calculate_balance(node.leftChild) < 0:
                # tree is left right unbalanced : we need left rotation on parent + below right rotation on grandparent
                self.rotate_left(node.leftChild)

            # if tree is left left unbalanced we only need this single right rotation
            self.rotate_right(node)

        if balance_factor < -1:
            # the height of the right subtree height > left subtree height (right heavy)

            if self.calculate_balance(node.leftChild) > 0:
                # tree is right left unbalanced : we need right rotation on parent + below left rotation on grandparent
                self.rotate_right(node.rightChild)

            # if tree is right right unbalanced we only need this single left rotation
            self.rotate_left(node)

    def calculate_balance(self, node):
        if node is None:
            return 0

        return self.calculate_height(node.leftChild) - self.calculate_height(node.rightChild)

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

        # finally we have to update the height value
        node.height = max(self.calculate_height(node.leftChild), self.calculate_height(node.rightChild)) + 1
        temp_left_node.height = max(self.calculate_height(temp_left_node.leftChild),
                                    self.calculate_height(temp_left_node.rightChild)) + 1

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

        # finally we have to update the height value
        node.height = max(self.calculate_height(node.leftChild), self.calculate_height(node.rightChild)) + 1
        temp_right_node.height = max(self.calculate_height(temp_right_node.leftChild),
                                     self.calculate_height(temp_right_node.rightChild)) + 1

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.leftChild:
            self.traverse_in_order(node.leftChild)

        l = 'NULL'
        r = 'NULL'
        p = 'NULL'
        root_node = True

        if node.leftChild is not None:
            l = node.leftChild.data

        if node.rightChild is not None:
            r = node.rightChild.data

        if node.parent is not None:
            p = node.parent.data
            root_node = False

        print(f'Node data: {node.data} left: {l} right: {r} parent: {p} height: {node.height} root node: {root_node}')

        # now we have to consider the right subtree
        if node.rightChild:
            self.traverse_in_order((node.rightChild))


avl = AVLTree()
avl.insert(3)
avl.insert(4)
avl.insert(5)
avl.insert(6)

avl.remove(6)

avl.traverse()
