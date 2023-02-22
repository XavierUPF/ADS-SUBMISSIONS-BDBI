import matplotlib.pyplot as plt

def is_valid(maze, x, y):
    """
    Check if the current cell is a valid move.
    """
    if x >= 0 and x < len(maze) and y >= 0 and y < len(maze[0]) and maze[x][y] == 1:
        return True
    return False



def find_shortest_path(maze, start_x, start_y, dest_x, dest_y):
    """
    Find the shortest path in the maze using breadth-first search.
    """
    visited = set()                                 # keep track of visited cells
    queue = [(start_x, start_y, [])]                # queue of cells to visit

    while queue:                                    # while queue is not empty
        x, y, path = queue.pop(0)                   # pop the first cell
        if x == dest_x and y == dest_y:             # if we reached the destination
            path.append((x, y))                     # add the destination to the path
            return path                             # return the path

        if (x, y) not in visited:                   # if we haven't visited the cell yet
            visited.add((x, y))                     # mark the cell as visited
            path.append((x, y))                     # add the cell to the path

            if is_valid(maze, x + 1, y):            # move down and check if it is a valid move
                queue.append((x + 1, y, path[:]))   # if it is, add it to the queue
            if is_valid(maze, x, y + 1):            # move right and check if it is a valid move
                queue.append((x, y + 1, path[:]))   # if it is, add it to the queue
            if is_valid(maze, x - 1, y):            # move up and check if it is a valid move
                queue.append((x - 1, y, path[:]))   # if it is, add it to the queue
            if is_valid(maze, x, y - 1):            # move left and check if it is a valid move
                queue.append((x, y - 1, path[:]))   # if it is, add it to the queue

    return None                                     # if we can't reach the destination, return None

def solve_maze(maze, start_x, start_y, dest_x, dest_y):
    """
    Main function to solve the maze and find the shortest path.
    """
    path = find_shortest_path(maze, start_x, start_y, dest_x, dest_y)
    return path                                     # return the shortest path

def plot_path(maze, path):
    """
    Plot the maze and the shortest path.
    """
    for x, y in path:
        maze[x][y] = 2

    fig, ax = plt.subplots()
    ax.imshow(maze, cmap='binary')
    plt.show()

if __name__ == '__main__':
    maze = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0],
            [0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0],
            [0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0],
            [0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0],
            [0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0],
            [0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0],
            [0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0],
            [0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0],
            [0,1,0,1,0,0,0,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0],
            [0,1,0,1,1,1,1,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0],
            [0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0],
            [0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0],
            [0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0],
            [0,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],
            [0,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0],
            [0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0],
            [0,0,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0],
            [0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0],
            [0,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0],
            [0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0],
            [0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0],
            [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    
    import time
    start_time = time.time()
    
    start_x, start_y = (30, 0)
    dest_x, dest_y = (6, 15)

    path = solve_maze(maze, start_x, start_y, dest_x, dest_y)
    if path:
        print(path)
        print('Time of execution:',time.time() - start_time)
        plot_path(maze, path)
    else:
        print('No path found.')