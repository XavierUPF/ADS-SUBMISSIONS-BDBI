import matplotlib.pyplot as plt

def is_valid(maze, x, y):
    """
    Check if the current cell is a valid move.
    """
    if x >= 0 and x < len(maze) and y >= 0 and y < len(maze[0]) and maze[x][y] == 1:
        return True
    return False

def find_path(maze, x, y, path, dest_x, dest_y):
    """
    Find the shortest path in the maze using backtracking.
    """
    if x == dest_x and y == dest_y:                         # If we have reached the destination, return True
        return True

    if is_valid(maze, x, y):                                # If the current cell is valid
        path.append((x, y))                                 # Add the current cell to the path
        maze[x][y] = 0.2                                    # Mark the current cell as visited

        if find_path(maze, x + 1, y, path, dest_x, dest_y): # Move down
            return True                                     # If the move down is valid, return True
        if find_path(maze, x, y + 1, path, dest_x, dest_y): # Move right
            return True                                     # If the move right is valid, return True
        if find_path(maze, x - 1, y, path, dest_x, dest_y): # Move up
            return True                                     # If the move up is valid, return True
        if find_path(maze, x, y - 1, path, dest_x, dest_y): # Move left
            return True                                     # If the move left is valid, return True

        path.pop()                                          # If none of the above movements work, backtrack
        return False                                        # and
    return False                                            # return False

def solve_maze(maze, start_x, start_y, dest_x, dest_y):
    """
    Main function to solve the maze and find the shortest path.
    """
    path = []                                               # Initialize the path
    if find_path(maze, start_x, start_y, path, dest_x, dest_y):
        return path                                         # If the path exists, return the path
    return None                                             # If the path does not exist, return None

def plot_path(maze, path):
    """
    Plot the maze and the shortest path.
    """
    for x, y in path:                                       # For each cell in the path
        maze[x][y] = 2                                      # Mark the cell as part of the path

    fig, ax = plt.subplots()                                # Create a figure and an axis
    ax.imshow(maze, cmap='binary')                          # Display the image
    plt.show()                                              # Show the plot

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
        print('Time of execution:',time.time()-start_time)
        plot_path(maze, path)
    else:
        print('No path found.')