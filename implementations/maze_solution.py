from collections import deque


class Node:

    def __init__(self, x, y, value):
        self.value = value
        self.x = x
        self.y = y
        self.adjacency_matrix = []
        self.visited = False


class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.move_x = [1, 0, 0, -1]
        self.move_y = [0, -1, 1, 0]
        # create a matrix the same size as the maze with all values set to False
        self.visited = [[False for _ in range(len(maze))] for _ in range(len(maze))]
        self.min_distance = float('inf')

    def is_valid(self, row, col):

        if row < 0 or row >= len(self.maze):
            return False  # we are outside the maze
        
        if col < 0 or col >= len(self.maze):
            return False  # we are outside the maze

        if self.maze[row][col] == 0:
            return False  # obstacle

        if self.visited[row][col]:
            return False  # already visited this cell
    
        return True

    def search(self, start_x, start_y, end_x, end_y):
        self.visited[start_x][start_y] = True

        queue = deque()  # doubly linked list - can access first and last item with O(N)
        queue.append((start_x, start_y, 0))

        while queue:
            (x, y, dist) = queue.popleft()

            if x == end_x and y == end_y:
                self.min_distance = dist
                break

            for move in range(len(self.move_x)):
                next_x = x + self.move_x[move]
                next_y = y + self.move_y[move]

                if self.is_valid(next_x, next_y):
                    self.visited[next_x][next_y] = True
                    queue.append((next_x, next_y, dist+1))

    def show_result(self):
        if self.min_distance != float('inf'):
            print(f'The shortest path from source to destination: {self.min_distance}')
        else:
            print('No feasible solution - the destination can not be reached!')


m = [
        [1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1],
        [0, 0, 0, 1, 1]
]


maze_solver = MazeSolver(m)

maze_solver.search(0, 0, 4, 4)

maze_solver.show_result()


m2 = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]

maze_solver2 = MazeSolver(m2)

maze_solver2.search(0, 0, 4, 4)

maze_solver2.show_result()