# Heaps

"""
Priority Queue
    - abstract data type (specification/ interface defining behaviour but we dont know the implementation)
    - very similar to queues
    - BUT each item has an additional property: a priority value
    - Highest priority element is retrieved first!!
    - Usually implemented with heaps but it can be implemented with self balancing trees

    Operations:
        - insertWithPriority(data, priority) // for integers we do not specify priority
        - getHighestPriorityElement()
            We have to reconstruct the heap each time.
            MinHeap and MaxHeap
        - peek()
            Returns the element with highest priority but heap does not change.
        - sorting: tree sort, heapsort rely on this sort of method

Heap
    - referred to as data structure but are implemented using 1 dimensional arrays
        (so technically also an abstract data type)
    - has binary tree structure
    - max heap, the keys of parents are greater than or equal to those of the children (highest key is in the root node)
    - min heap, the keys of parents are less than or equal to those of the children (lowest key is in the root node)
    - it can not be unbalanced!
    Applications:
        - Dijkstras's algorithm
        - prims algorithm
    - It has NOTHING to do with the pool of memory from which dynamically allocated memory is allocated!!
    Properties:
        - complete: we construct from left to right
        - in binary heap every node can have 2 children (left and right)
            we DO NOT specify if left or right is greater/smaller
        - Min Heap -> parent is smaller than children
        - Max Heap -> parent is greater than children

    Represent heap as array: index given to each node

        parent node
      |------[i]-------|
    2i + 1          2i + 2
    Left Child      Right Child
                                                                  __ARRAY___
            |----------[210]----------|                          | 210 | 0 |
      |---[100]---|                 [23]                         | 100 | 1 |
    [2]          [5]                                             | 23  | 2 |
                                                                 | 2   | 3 |
                                                                 | 5   | 4 |

    O(N) to construct a heap

    Delete an item: we remove the item and put the last item there, then we make sure theap properties are valid
        Operation:  deleting the root node O(1) + reconstruction O(logN)    = O(logN)
                    removing arbitrary item O(N) + reconstruction O(logN)   = O(N)

    | Operation             | Time complexity   |
    |-----------------------|-------------------|
    | Memory complexity     | O(N)              |
    | Find min or max       | O(1)              | very fast! As it will be the root node
    | Insert new item       | O(logN)           | We may have to make many swaps
    | Remove min/ max       | O(logN)           |

    Binomial heap
        - similar to binary heap but also supports quick merging of two heaps
        - priority queue with support for merge operation
        - insertion can be reduced to O(1) constant time complexity
        - merge operation is O(logN)

    Fibonacci heap
        - faster than binary heap
        - BUT hard to implement efficiently
        - can have several children but number usual kept low
        - can achieve O(1) insertion
        - merge operation is O(1)


"""


# maximum number of items that can be stored in the heap
CAPACITY = 10


class MaxHeap:

    def __init__(self):
        # create an array with as many slots as the CAPACITY
        self.heap = [0]* CAPACITY
        # So we can track the number of items in the heap
        self.heap_size = 0

    # Insertion takes O(1) BUT we have also run self.fix_up which has time complexity O(logN)
    # Running time: O(logN)
    def insert(self, item):
        # check our heap has space
        if self.heap_size == CAPACITY:
            print('Cannot insert: Heap full')
            return

        # insert item + increment the heap size
        self.heap[self.heap_size] = item
        self.heap_size = self.heap_size + 1

        # check if heap properties have been violated + fix them
        self.fix_up(self.heap_size-1)

    # look at the last item and checks whether swaps are needed
    # running time: O(logN)
    def fix_up(self, index):
        parent_index = (index-1) // 2

        # checking recursively up to the root node we swap the node with the parent if it is greater
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.swap(index, parent_index)

    # Peek()
    # O(1)
    def get_max(self):
        return self.heap[0]

    # returns max item + remove it from the heap
    # O(logN)
    def poll(self):

        max = self.get_max()

        self.swap(0, self.heap_size-1)
        self.heap_size = self.heap_size - 1

        self.fix_down(0)

        return max

    # recursively check through the tree for violations
    # ensure the largest index is swapped up to the root if necessary
    def fix_down(self, index):

        left_index = (index * 2) + 1
        right_index = (index * 2) + 2
        index_largest = index

        if left_index < self.heap_size and self.heap[left_index] > self.heap[index]:
            index_largest = left_index

        if right_index < self.heap_size and self.heap[right_index] > self.heap[index]:
            index_largest = right_index

        # of course we don't want to swap the given index with it's self
        if index != index_largest:
            self.swap(index, index_largest)
            self.fix_down((index_largest))

    def swap(self, index1, index2):
        self.heap[index2], self.heap[index1] = self.heap[index1], self.heap[index2]

    # every poll() operation takes O(logN) because the fix_down() method so overall complexity is O(NlogN)
    # where N is the number of items we want to sort
    def heap_sort(self):
        # we decrease the size of the heap in the poll() so we store it here !!!
        size = self.heap_size

        for i in range(0, size):
            max_item = self.poll()
            print(f'Max: {max_item}')


from heapq import heappop, heappush, heapify

heap = []
nums = [12,3,-2,6,4,8,9]

for num in nums:
    heappush(heap, num)

while heap:
    print(heappop(heap))

heapify(nums)  # converts nums array to a heap

print(f'Heapify: {nums}')
