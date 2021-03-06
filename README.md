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


```
[A]----4---->[C]
 |
 2
 |
[B]---3--->[D]
```

|    |A   |B   |C   |D|
|----|----|----|----|-|
|A   |0   |2   |4   |0|
|B   |0   |0   |0   |3|
|C   |0   |0   |0   |0|
|D   |0   |0   |0   |0|

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

A web crawler may acquire important parameters of the web such as page rank (importance of a page)
It can also allow us to learn about the topology and degree of distribution of complex networks (such as popularity of a person on a social network)

[Web crawler implementation](implementations/webcrawler.py)

### Maze Solver with BFS
Design an algorithms with breadth-first search that is able to find the shortest path from a given source to a given destination.
The maze is represented by a two-dimensional list.
The (0,0) is the source and (4,4) is the destination. 0 represents walls or obstacles and 1 is the valid cells we can include in the solution.

```
[
   [S, 1, 1, 1, 1],
   [0, 1, 1, 1, 1],
   [0, 0, 0, 0, 1],
   [1, 0, 1, 1, 1],
   [0, 0, 0, 1, D]
]
```

[maze solver solution](implementations/maze_solution.py)

## Depth First Search (DFS)

- strategy for solving mazes
- traverses as far as possible along each branch before backtracking (BFS is a layer by layer algorithm)
- O(V+E) V= no. of vertices E= no. of edges
- memory complexity is a bit better that that of BFS
- two approaches recursion (will be stored on the call stack) and iteration (will require a stack)

Underlying data structure is a stack, we make use here of LIFO data structure.
    - memory complexity is O(logN) (the height of the tree is how many items we have to store in the stack)

### Applications

* Topological ordering
* Find strongly connected components in a graph (important for recommendation systems)
* Detecting cycles
* Generate maze or find way out of a maze

[Implementation](implementations/dfs.py)


## The Shortest Path problem and Dijkstra's Algorithm

Dijkstra's algorithm is popular for the shortest path problem as it can find the shortest path incredibly quickly but is also able to construct the shortest path tree.
The shortest path tree defines the shortest paths form a source to all the other nodes.
It's running time complexity is O(VlogV + E) with a priority queue and O(V*V+E) without
It is however a greedy approach - the more memory the faster it gets
The appropriate underlying data structure is a priority queue (heap).

[Implementation of dijstra's algorithm with adjacency list](implementations/dijkstra_algorithm.py)
[Implementation of dijstra's algorithm with adjacency matrix](implementations/dijkstra_with_adjacency_matrix.py)

### Applications

- GPS and navigation
- Routing information protocol
- Image processing (shrinking)


## The Longest Path problem

NP-hard problem - no know polynomial running time algorithm
but if G(V,E) is a directed acyclic graph (DAG) then we can solve it in linear running time
We can change the longest path problem into the shortest path - negate the edge weights (multiply by -1)
We have to use Bellman-Ford algorithm because Dijkstra's cannot handle the negative edges.

### Critical path method (CPM)

Came out of the Manhattan project, used for major skyscrapers.

Algorithm requires:
1) list of all activities required to complete the project
2) the time (duration) that each activity will take to complete
3) the dependencies between the activities

From this we can construct an G(V,E) DAG. There are no cycles in such graphs.

## Bellman-Ford Algorithm

- Can work with negative edge weights
- Slower than Dijkstra's algorithm but it is more robust
- Running complexity O(V*E)
- Makes v-1 iterations because the maximal length of the shortest path between vi and vj arbitrary nodes in a G(V,E) graph is |V|-1 (if there are no cycles)
- If we make another iteration after V-1 and there is a change we can conclude there is a negative cycle 

## Greedy approach and dynamic programing

Greedy algorithm:   An algorithmic paradigm that constructs the final solution by choosing the best option possible in every iteration.
                    It combined locally optimal solutions to get the global solution (final result).
                    They are usually faster than dynamic approach.

Dynamic algorithm:  An algorithmic paradigm that avoids recalculating the same problems over and over again
                    It uses extra memory to store the sub-results.
                    Main idea is to break down complicated problems in to sub-problems often in a recursive manner.
                    We can apply dynamic programming when:
                        1) optimal substructure
                        2) overlapping sub-problems




