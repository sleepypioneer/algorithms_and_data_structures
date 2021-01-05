# Arrays
"""
- data structure
- 0 indexing
- access with index
- can be multidimensional
- Application: lookup tables/ hash tables, heap
IMPORTANT: we have to know the size of the array at compile time.
If the array is full and we want to add more we have to create a new one and copy the values O(N)
"""

# Types can be mixed
array = [10, 3, 'Adam', 6]

# random indexing
print(array[2])

print(array[0:1])

array[2] = 5

# OPERATIONS

# Add O(1)
array.append(12)
array.append(8)

print(array)

# Insert 0(N)
array.insert(2, 14)

# Remove last item O(1)
array.pop()
print(array)

# Remove specific item O(N)
array.pop(2)
print(array)

# Linear search O(N)

max = array[0]

for num in array:
    if num > max:
        max = num

print(max)

"""
Method	    Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""

# Linked Lists

"""
node {
    data
    reference to next node
}

- data structure
- easy to grow and insert/remove specific values
- arrays expect balues to be the same size, linked lists can have varying value sizes
- doubled linked list (this requires more memory as we have to use backward reference)
- Applications: low level memory management (manipulate the heap memory), 
    Alt Tab (show windows), Photo viewer (next/ prev photo), blockchains
"""

"""
|                       | linked list    | array    |
|-----------------------|----------------|----------|        
| search                | O(1)           | O(N)     |
| Deletion (start)      | O(1)           | O(N)     |
| Deletion (end)        | O(N)           | O(1)     |
| Insert   (start)      | O(1)           | O(N)     |
| Insert   (end)        | O(N)           | O(1)     |
| Memory   (waste space)| O(N)           | O(1)     |

"""


class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.numOfNodes = 0

    def insert_start(self, data):
        """
        O(1) constant running time operation
        """
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)

        if not self.head:
            # if the linked List is empty we make our new node the head
            self.head = new_node
        else:
            # if it already has a head node we insert the new node before it
            new_node.nextNode = self.head
            self.head = new_node

    def insert_end(self, data):
        """
        O(N) linear running time operation
        """
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)

        actual_node = self.head

        # we have to find the last node
        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode

        actual_node.nextNode = new_node

    def size_of_list(self):
        """
        O(1) constant running time operation
        """
        return self.numOfNodes

    def traverse(self):
        """
        O(N) linear running time operation
        """
        actual_node = self.head

        while actual_node.nextNode is not None:
            print(actual_node.data)
            actual_node = actual_node.nextNode

    def remove(self, data):

        if self.head is None:
            """
            linked list is empty
            O(1) constant running time operation
            """
            return

        actual_node = self.head
        previous_node = None

        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.nextNode

        if actual_node is None:
            """
            search miss - the item is not present in the list
            O(N) linear running time operation
            """
            return

        self.numOfNodes = self.numOfNodes - 1

        if previous_node is None:
            """
            Node is at start of list
            O(1) constant running time operation
            """
            self.head = actual_node.nextNode
        else:
            """
            Node is somewhere else in the list
            O(N) linear running time operation
            """
            previous_node.nextNode = actual_node.nextNode


linked_list = LinkedList()

linked_list.insert_start(4)
linked_list.insert_start(3)
linked_list.insert_start(7)
linked_list.insert_end(10)

linked_list.traverse()

linked_list.remove(10)

linked_list.traverse()

print("size of list: ", linked_list.size_of_list())


# Doubly linked list

class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.prevNode = None


"""
Advantages:
- cna be traverse in both directions
- remove operation is more efficient if the node is given
To remove a node from singly linked list -> we need the node + predecessor
To remove a node from doubly linked list -> we need only the node
"""