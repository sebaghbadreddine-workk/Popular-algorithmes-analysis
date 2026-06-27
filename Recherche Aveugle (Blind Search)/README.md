# Blind Search (Recherche Aveugle) - BFS & DFS Maze Solver

This folder contains Python implementations of blind search algorithms, specifically Breadth-First Search (BFS) and Depth-First Search (DFS), applied to solving maze pathfinding problems.

## Directory Structure

```
Recherche Aveugle (Blind Search)/
├── maze_utils.py              # Shared utility module (algorithms, profiling, visualization)
├── PARTIE1.py                 # 10x10 Maze search demo
├── PARTIE2.py                 # 15x15 Maze search demo
├── README.md                  # Documentation of the experiment (this file)
└── RECHERCHE_AVEUGLE_RAPPORT.pdf # Original laboratory report (French)
```

> [!NOTE]
> The original academic PDF report inside this directory reflects the initial version (V1) of the project submitted for grading. The code has since been refactored in this repository to use a more clean, modular structure ([maze_utils.py]) to eliminate redundancy and improve maintainability.


## Algorithms Implemented

1. **Breadth-First Search (BFS)**:
   * **Behavior**: Explores neighbors layer-by-layer (FIFO queue structure).
   * **Optimality**: Guarantees the shortest path in terms of steps for unweighted grids.
   * **Time/Space Complexity**: $O(V + E)$ where $V$ is number of nodes and $E$ is edges.

2. **Depth-First Search (DFS)**:
   * **Behavior**: Explores as deep as possible along each branch before backtracking (LIFO stack structure).
   * **Optimality**: Does not guarantee the shortest path.
   * **Time/Space Complexity**: $O(V + E)$ time, but often uses less memory than BFS depending on the target position and structure.

## Metrics Measured

For each run, the following metrics are captured and plotted side-by-side:
* **Execution Time (ms)**: Measured using Python's `time` library.
* **Peak Memory Usage (KB)**: Profiled using the built-in `tracemalloc` library.
* **Path Length (Nodes)**: Number of coordinates in the path from Start to Goal.

## Prerequisites

Ensure you have Python 3 and the `matplotlib` library installed for drawing the charts:

```bash
pip install matplotlib
```

## How to Run

### Part 1: 10x10 Maze Grid
Run the following script to execute BFS and DFS on the 10x10 grid:
```bash
python PARTIE1.py
```

### Part 2: 15x15 Maze Grid
Run the following script to execute BFS and DFS on the expanded 15x15 grid:
```bash
python PARTIE2.py
```
