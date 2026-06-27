# Informed Search (Recherche Informée) - A*, Greedy, BFS & DFS Comparison

This folder compares **Informed Search** algorithms (A* and Greedy Best-First Search) against **Uninformed Search** algorithms (BFS and DFS) on randomized maze environments, measuring execution time, memory consumption, path length, and nodes explored.

## Directory Structure

```
Recherche Informée (Informed Research)/
├── maze.py                            # Maze class: random grid generation and traversal helpers
├── algorithms.py                      # Search algorithm implementations (BFS, DFS, A*, Greedy)
├── visualization.py                   # Statistical and path visualization functions
├── main.py                            # Experiment runner: benchmarks and statistical output
├── README.md                          # Documentation (this file)
└── RECHERCHE_INFORMEE_RAPPORT.pdf     # Original laboratory report (French)
```

> [!NOTE]
> The original academic PDF report inside this directory reflects the initial version (V1) of the project submitted for grading. The code has since been updated in two ways:
> 1. **Code**: All comments and outputs have been standardized to English.
> 2. **Experimental Design**: The V1 code evaluated each algorithm on 20 independently generated random mazes (meaning algorithms were compared on different mazes). This version pre-generates a single shared set of 20 mazes so that all four algorithms are tested on the **same** grid configurations, ensuring a scientifically fair performance comparison.

---

## Algorithms Implemented

### Uninformed Search
1. **Breadth-First Search (BFS)**:
   * Explores all neighbors at the current depth before moving deeper (FIFO queue).
   * **Guarantees** the shortest path in terms of steps.

2. **Depth-First Search (DFS)**:
   * Explores as deep as possible before backtracking (LIFO stack).
   * Does **not** guarantee the shortest path.

### Informed Search
3. **A\* Search**:
   * Combines actual cost ($g$) and a heuristic estimate ($h$ = Manhattan Distance) to find the optimal path efficiently.
   * **Guarantees** the shortest path when using an admissible heuristic.

4. **Greedy Best-First Search (GBFS)**:
   * Uses only the heuristic ($h$ = Manhattan Distance) to guide exploration toward the goal.
   * Fast, but does **not** guarantee the shortest path.

---

## Metrics Measured

For each run, the following metrics are captured and aggregated (Mean & Std Dev):
* **Execution Time (s)**: Profiled with `time.perf_counter()`.
* **Peak Memory Usage (MB)**: Profiled with `tracemalloc`.
* **Path Length (Nodes)**: Number of steps in the path from start to goal.
* **Nodes Explored**: Total number of nodes visited during the search.

---

## Visualizations Generated

The experiment suite produces the following plots via `visualization.py`:
* **Bar Plot**: Side-by-side average comparison of Time, Memory, and Path Length.
* **Box Plot**: Statistical distribution of each metric per algorithm.
* **Pie Chart**: Proportional resource consumption breakdown.
* **Line Plot**: Execution time stability per algorithm across all 20 runs.

---

## Prerequisites

Ensure you have Python 3 installed. Install all required dependencies:

```bash
pip install matplotlib pandas seaborn numpy scipy
```

---

## How to Run

```bash
python main.py
```

This will:
1. Pre-generate 20 random maze instances (100x100 grid, 30% wall density).
2. Run all four algorithms (BFS, DFS, A*, Greedy) on the same set of 20 mazes.
3. Print the statistical summary table (Mean & Std Dev) in the terminal.
4. Generate all statistical plot windows sequentially.
