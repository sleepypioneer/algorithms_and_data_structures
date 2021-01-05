# Ternary Search trees

"""
Ternary Search Trees
    - we cna search and sort strings very very efficiently
    - Trie data structure consumes a lot of memory, so use ternary search trees instead which store less references
    - TST store characters or strings in nodes
    - Each node has 3 children
        left: less than (prev letter in alphabet),
        middle: equal (next character in word),
        right: greater (next letter in alphabet)
    - we can balance but it's not efficient
    - good alternative for hashmap (faster) and more flexible than binary search trees


Tries:
    - node can have as many children as the size of the alphabet (ie in English 26)

"""


class Node:

    def __init__(self, char):
        self.char = char
        self.children = {}
        self.word_finished = False
        self.counter = 0


class Trie:

    def __init__(self):
        self.root = Node('*')  # to make the root empty

    def insert(self, word):
        current = self.root
        for char in word:
            if char in current.children:
                current = current.children[char]
                current.counter += 1
            else:
                new_node = Node(char)
                current.children[char] = new_node
                current = new_node
                current.counter += 1
        current.word_finished = True

    def search(self, word):
        """

        :param word:
        :return: True (word found) False (word not found)
        """
        if not self.root.children:
            return False
        current = self.root
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        if current.word_finished:
            return True
        return False


tree = Trie()

tree.insert('bat')
tree.insert('horse')
tree.insert('zebra')
tree.insert('cat')
tree.insert('caterpillar')
tree.insert('mouse')
tree.insert('rat')

print(tree.search('bat'))
print(tree.search('dog'))
print(tree.search('batter'))
print(tree.search('caterpillar'))


