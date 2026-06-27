import time
import tracemalloc
import matplotlib.pyplot as plt
from collections import deque

def get_neighbors(node, maze, directions):
    """
    Get all valid adjacent neighbors of a node in the maze.
    
    :param node: Tuple (row, col) representing current position
    :param maze: Dictionary mapping (row, col) coordinates to 0 (free) or 1 (wall)
    :param directions: List of coordinate offsets representing movement directions
    :return: List of valid neighbor coordinates
    """
    x, y = node
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if (nx, ny) in maze and maze[(nx, ny)] == 0:
            neighbors.append((nx, ny))
    return neighbors

def bfs(start, goal, maze, directions):
    """
    Find a path from start to goal using Breadth-First Search.
    
    :param start: Starting coordinate tuple (row, col)
    :param goal: Target coordinate tuple (row, col)
    :param maze: Dictionary representing the maze grid
    :param directions: List of coordinate offsets representing movement directions
    :return: List of coordinates representing the path from start to goal (empty if no path)
    """
    queue = deque([start])
    came_from = {start: None}

    while queue:
        current = queue.popleft()
        if current == goal:
            break
        for neighbor in get_neighbors(current, maze, directions):
            if neighbor not in came_from:
                came_from[neighbor] = current
                queue.append(neighbor)

    if goal not in came_from:
        return []

    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = came_from[node]
    return path[::-1]

def dfs(start, goal, maze, directions):
    """
    Find a path from start to goal using Depth-First Search.
    
    :param start: Starting coordinate tuple (row, col)
    :param goal: Target coordinate tuple (row, col)
    :param maze: Dictionary representing the maze grid
    :param directions: List of coordinate offsets representing movement directions
    :return: List of coordinates representing the path from start to goal (empty if no path)
    """
    stack = [start]
    came_from = {start: None}

    while stack:
        current = stack.pop()
        if current == goal:
            break
        for neighbor in get_neighbors(current, maze, directions):
            if neighbor not in came_from:
                came_from[neighbor] = current
                stack.append(neighbor)

    if goal not in came_from:
        return []

    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = came_from[node]
    return path[::-1]

def measure_performance(algorithm, start, goal, maze, directions):
    """
    Measure execution time and peak memory consumption of a search algorithm.
    
    :param algorithm: Search algorithm function (bfs or dfs)
    :param start: Starting coordinate tuple (row, col)
    :param goal: Target coordinate tuple (row, col)
    :param maze: Dictionary representing the maze grid
    :param directions: List of coordinate offsets representing movement directions
    :return: Tuple of (path, elapsed_time_seconds, peak_memory_kb)
    """
    # Start tracking time and memory allocation
    start_time = time.time()
    tracemalloc.start()
    
    path = algorithm(start, goal, maze, directions)
    
    # Get peak memory and stop tracking
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    elapsed_time = time.time() - start_time
    
    return path, elapsed_time, peak / 1024  # Convert bytes to KB

def print_maze(maze, rows, cols, path=None):
    """
    Print the maze grid in console text representation.
    
    :param maze: Dictionary representing the maze grid
    :param rows: Number of rows in the maze
    :param cols: Number of columns in the maze
    :param path: Optional list of coordinates forming the path to highlight
    """
    for x in range(rows):
        for y in range(cols):
            if path and (x, y) in path:
                print("P", end=" ")
            elif maze.get((x, y)) == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()

def plot_results(results):
    """
    Plot execution time, memory usage, and path length side-by-side using matplotlib.
    
    :param results: List of tuples (algorithm_name, path_length, time_taken_sec, peak_memory_kb)
    """
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))

    names = [res[0] for res in results]
    times = [res[2] * 1000 for res in results]  # Convert execution time to milliseconds
    memory = [res[3] for res in results]
    lengths = [res[1] for res in results]

    # Graph 1: Execution Time
    ax1.bar(names, times, color='skyblue')
    ax1.set_title('Execution Time')
    ax1.set_ylabel('Milliseconds')
    ax1.grid(axis='y', linestyle='--')

    # Graph 2: Memory Used
    ax2.bar(names, memory, color='lightgreen')
    ax2.set_title('Memory Used')
    ax2.set_ylabel('Kilobytes')
    ax2.grid(axis='y', linestyle='--')

    # Graph 3: Path Length
    ax3.bar(names, lengths, color='salmon')
    ax3.set_title('Path Length')
    ax3.set_ylabel('Number of Nodes')
    ax3.grid(axis='y', linestyle='--')

    plt.tight_layout()
    plt.show()
