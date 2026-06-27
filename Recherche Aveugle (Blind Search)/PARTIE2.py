import maze_utils

# Create a 15x15 maze:
ROWS, COLS = 15, 15
MY_MAZE = {(r, c): 0 for r in range(ROWS) for c in range(COLS)}

# Define wall coordinates in the maze:
walls = [
    (0, 1), (1, 1), (2, 1), (4, 1), (5, 1),
    (1, 3), (2, 3), (3, 3), (4, 3), (6, 3), (7, 3), (8, 3),
    (0, 5), (1, 5), (2, 5), (4, 5), (5, 5), (6, 5), (8, 5), (9, 5),
    (1, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (9, 7),
    (2, 8), (4, 9),
    (10, 2), (11, 2), (12, 2), (14, 2),
    (10, 10), (11, 10), (12, 10), (13, 10),
    (14, 5), (14, 6), (14, 7), (14, 12)
]

# Set walls in the maze:
for wall in walls:
    MY_MAZE[wall] = 1

# Define directions: UP, DOWN, LEFT, RIGHT
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Start and goal configurations
start = (0, 0)
goal = (14, 14)

# Define configurations for algorithms
algorithms = [
    (maze_utils.bfs, "BFS"),
    (maze_utils.dfs, "DFS"),
]

if __name__ == "__main__":
    print("Initial Maze Layout (15x15):")
    maze_utils.print_maze(MY_MAZE, ROWS, COLS)

    print("\nExecuting Search Algorithms...")
    results = []
    
    for algo, name in algorithms:
        print(f"\n{name} path:")
        path, time_taken, mem_used = maze_utils.measure_performance(
            algo, start, goal, MY_MAZE, directions
        )
        maze_utils.print_maze(MY_MAZE, ROWS, COLS, path)
        results.append((name, len(path), time_taken, mem_used))

    # Display execution comparison table
    print("\nPerformance Comparison Summary:")
    print(f"{'Algorithm':<12} | {'Time (ms)':<12} | {'Memory (KB)':<12} | {'Path Length'}")
    print("-" * 60)
    for name, length, time_taken, mem_used in results:
        time_ms = time_taken * 1000
        print(f"{name:<12} | {time_ms:<12.5f} | {mem_used:<12.2f} | {length}")

    # Plot metrics visually
    print("\nGenerating performance plots...")
    maze_utils.plot_results(results)
