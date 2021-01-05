# STACK

"""
Abstract data type (interface)
Basic operations: pop, push, peek
LIFO (last in first out)
Can be implemented with array or linked list
Many languages are stack oriented - taking their arguments from the stack and placing return values back on the stack
Applications:
    - back button in the web browser
    - undo operation in software
    - stack memory stores local variable and function calls
"""

# Stack versus heap memory

"""
STACK:
- Call stack is an abstract data type that stores information about the active subroutines/methods, functions of a program
- Details are normally hidden and automatic in high level programming languages
- keeps track of the point to which each active subroutine should return control when it finishes executing
- stores temporary variables created by each function, when the function exits the variables are freed
- stack memory is limited

HEAP:
- NOT managed automatically for you (we have to deallocated these memory chunks or risk memory leak)
- Large region of memory
- Slower because of the pointers


| stack memory                  | heap memory               |
|-------------------------------|---------------------------|
| limited in size               | no size limits            |
| fast access                   | slow access               |
| local variables               | objects                   |
| space managed by CPU          | memory may be fragmented  |
| variables cannot be resized   | variables can be resized  |

"""

# Stack and recursion

"""
Recursion:
- Applications: Depth First Search, looking for an item in a linked list
- Can transform to iterative approach with stack (while loop)
- The OS will use stacks
- Recursive function calls are pushed onto the stack
- Can risk stack overflow if there are too many function calls to be pushed onto the stack
"""

class Stack:

    def __init__(self):
        self.stack =  []

    def push(self, data):
        """
        insert item into the stack
        O(1) constant running time operation
        """
        self.stack.append(data)

    def pop(self):
        """
        remove and return the last item we have inserted (LIFO)
        O(1) constant running time operation
        """
        if self.stack_size() < 1:
            return -1  # -1 indicates the stack is empty

        data = self.stack[-1] # return last item
        del self.stack[-1]
        return data

    def peek(self):
        """
        return the last item without removing it
        0(1) constant running time operation
        """
        return self.stack[-1]

    def is_empty(self):
        """
        O(1)
        """
        return self.stack == []

    def stack_size(self):
        return len(self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print('Size: ', stack.stack_size())
print('Peek item: ', stack.peek())
stack.pop()
print('Size: ', stack.stack_size())


# QUEUE

"""
Abstract data type (interface)
Base operations: enqueue(), dequeue(), peek()
FIFO (first in first out)
Can be implemented with dynamic arrays as well as with linked list
Applications: 
    - Important when implementing BFS algorithm for graphs
    - When a resource is shared with several consumers (threads) we store them in a queue for example CPU scheduling
    - When data is transferred asynchronously for example IO buffers
    - Operational research applications or stochastic models
"""

class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        """
        O(1)  constant running time
        """
        return self.queue == []

    def enqueue(self, data):
        """
        O(1) constant running time
        """
        self.queue.append(data)

    def dequeue(self):
        """
        O(N) linear running time (because we have to remove the first item in the array)
        Could use doubly linked list as it can manipulate both the first and last in O(1)
        """
        if self.size_queue() != 0:
            data = self.queue[0]
            del self.queue[0]
            return data
        return -1   # -1 indicates the stack is empty

    def peek(self):
        """
        O(1) constant running time
        """
        return self.queue[0]

    def size_queue(self):
        """
        O(1) constant running time
        """
        return len(self.queue)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print('Dequeue: ', queue.dequeue())
print('Size: ', queue.size_queue())