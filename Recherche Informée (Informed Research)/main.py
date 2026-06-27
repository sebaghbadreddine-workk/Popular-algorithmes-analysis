import pandas as pd
import time
import tracemalloc
from maze import Maze
from algorithms import bfs_search, dfs_search, a_star_search, greedy_best_first_search
# Importing the functions from the visualization file
from visualization import (
    plot_bar_comparison, 
    plot_box_plots, 
    plot_pie_charts, 
    plot_line_metrics, 
    visualize_maze_solution
)

def run_experiments(algorithms, maze_size=(100, 100), density=0.3, runs=20):
    """ Executes experiments and collects all required performance data """
    # Pre-generate a list of mazes so that all algorithms are evaluated on the exact same mazes
    mazes = [Maze(maze_size[0], maze_size[1], density) for _ in range(runs)]
    
    results = []
    for name, algo_func in algorithms.items():
        print(f"Running {name}...")
        for i, m in enumerate(mazes):
            tracemalloc.start()
            start_time = time.perf_counter()
            
            # Returning path and nodes_explored for performance metrics
            path, nodes_explored = algo_func(m) 
            
            end_time = time.perf_counter()
            _, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            
            if path:
                results.append({
                    'Algorithm': name,
                    'Run': i + 1,
                    'Time': end_time - start_time,
                    'Memory': peak / 10**6, # Memory in MB
                    'Path Length': len(path),
                    'Nodes Explored': nodes_explored
                })
    return pd.DataFrame(results)


if __name__ == "__main__":
    # 1. Define the algorithms to be tested
    algorithms = {
        'BFS': bfs_search,
        'DFS': dfs_search,
        'A*': a_star_search,
        'Greedy': greedy_best_first_search
    }
    # 2. Run the experiment suite
    df_results = run_experiments(algorithms, maze_size=(100, 100), runs=20) 
    
    # 3. Generate statistical summary (Mean & Std)
    summary_stats = df_results.groupby('Algorithm').agg({
        'Time': ['mean', 'std'],
        'Memory': ['mean', 'std'],
        'Path Length': ['mean', 'std']
    }).round(4)
    
    print("\n" + "="*60)
    print("STATISTICAL RESULTS (MEAN & STD)")
    print("="*60)
    print(summary_stats)
    
    # 4. Execute all visualization functions
    print("\nGenerating all visualizations...")
    
    # Bar Plot for metric comparison
    plot_bar_comparison(df_results)
    
    # Box Plot for result distribution
    plot_box_plots(df_results)
    
    # Pie Chart for Nodes Explored proportions
    plot_pie_charts(df_results)
    
    # Line Plot for performance stability across runs
    plot_line_metrics(df_results)
    
