# Algorithms and Data structure in Python 🐍

Notes from [Algorithms and Data structures](https://www.udemy.com/course/algorithms-and-data-structures-in-python) Udemy course instructed by Balazs Holczer.
The course covers the implementation of data structures and abstract data types such as Arrays, Linked Lists, Heaps, Stacks, Queues, Graphs, Binary Search Trees, Associatives Arrays, and Dictionaries in Python.
As well as the time complexity of each data structure.

The course also introduces algorithms in Python. Including: Dijkstra's algorithm, Bellman-Ford algorithm, Sorting algorithms.

* [Arrays and linked lists](implementations/arrays_and_linked_lists.py)
* [stacks and queues](implementations/stacks_and_queue.py)
* [Binary search trees](implementations/binary_search_trees.py)
* [AVL trees](implementations/avl_trees.py)
* [Red-black trees](implementations/red_black_trees.py)
* [Heaps](implementations/heaps.py)
* [Associative arrays / hashtables / dictionaries](implementations/associative_arrays.py)
* [Ternary Search Trees](implementations/tenary_search_trees.py)


## Time complexity

Big O notation

| Notation      | Name                  |
|---------------|-----------------------|   
| O(1)          | constant              |
| O(logN)       | logarithmic           |
| O(N)          | linear                |
| O(n log n)    | n log n / loglinear   |
| O(N^2)        | quadratic             |
| O(n!)         | factorial             |


## Data structure versus abstract data type

An abstract data type is the specification/ interface defining behaviour, but we don't know the implementation.
A data structure is the concrete implementation.

An algorithm can be boosted up by proper data structures (however it will require more memory)
For example Dijkstra's algorithm without a priority queue has O(N2) time complexity and with a priority queue (heap) O(NlogN)


## Graph theory overview

The study of graphs, which are mathematical structures used to model pairwise relations between objects.

- Graphs are made up of nodes (vertices) that connected by edges (links)

**Undirected graphs:** edges are bidirectional edge(u,v) == edge(v,u)

**Directed graphs:** edges have a direction edge(u,v) != edge(v,u)

*note edges may have weights as well*

### Graph Types

* **Trees** - undirected graph where any two verticals are connected by one path
* **Forest** - undirected graph whose connected coponents are trees
* **direct** acyclic graph (DAG): finite directed graph with no directed cycles
* **complete graph** - every single pair of vertices are connected


### Graph representation

#### Adjacency list Representation

We assign a data structure (array) to every single vertex (node) in the graph that stores the edges accordingly

**Good** - iterating over all the edges is efficient
**Bad** - edge weight lookup is slow O(E) because we have to find it in linear time

#### Adjacency list Matrix

We construct VxV martix (M) wgere M[i][j] represents the edge weight going from i to j, where 0 represents no connection.


[A]----4---->[C]
 |
 2
 |
[B]---3--->[D]

    A   B   C   D
A   0   2   4   0
B   0   0   0   3
C   0   0   0   0
D   0   0   0   0

*Undirected graphs have symmetric adjacency matrices*

Space effiecient with dense graphs but it requires O(V^2) memory

**Good** - edge weight look up O(1)
**Bad** - iterating over all edges take O(E^2) where E is the number of edges

### Applications of Graphs

* Shortest path algorithm
    - Dijkstra's shortest path to find path between two distances (maps)
    - computer networks (open shortest path first routing)
* Crawling a network (WWW)
* Job scheduling (how to schedule dependant jobs so overall time is the minimum)
* Complex networks (graphs with non-trivial topological features - ecosystem)
* Quadracti optimization problems (vehicle routing problem, traveling sales man)
* Strongly connect components (recommendation systems, analyze ecosystems)


## Breadth First Search (BFS)

- visit every vertex exactly once
- Linear time complexity O(V+E) V= no. of vertices E= no. of edges
- memory complexity is not good, it requires a lot of references
- Advantage it constructs a shortest path
- Dijstra's algorithm uses BFS if all edges have the weight 1

Underlying data structure is a queue, we add nodes to it and dequeue them once we have visited them.
    - memory complexity is O(N)

### Applications

* AI (ML)
* maximum flow
* Cheyen's algorith in garbage collection
* serialization and deserialization

*In the main DFS is a bit better for traversing trees*

[Implementation](implementations/bfs.py)


### Web crawlers

A web crawler may acquire important paramters of the web such as page rank (importance of a page)
It can also allow us to learn about the topology and degree of distribution of complex networks (such as popularity of a person on a social network)

[Web crawler implementation](implementations/webcrawler.py)

## Depth First Search (BFS)

- strategy for solving mazes
- traverses as far as possible along each branch before backtracking (BFS is a layer by layer algorithm)
- O(V+E) V= no. of vertices E= no. of edges
- memory complexity is a bit better that that of BFS
- two approaches recursion (will be stored on the call stack) and iteration (will require a stack)

Underlying data structure is a stack, we make use here of LIFO data structure.
    - memory complexity is O(logN) (the height of the tree is how many items we have to store in the stack)

### Applications

* Topological ordering
* Find strongly connected components in a graph (important for reccomendation systems)
* Detecting cycles
* Generate maze or find way out of a maze

[Implementation](implementations/dfs.py)

