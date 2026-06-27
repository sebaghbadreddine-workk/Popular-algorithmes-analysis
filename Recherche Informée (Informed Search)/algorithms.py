import heapq
from collections import deque

def manhattan_distance(p1, p2):
    """Heuristic: Manhattan distance calculation"""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# --- Uninformed Search Algorithms ---

def bfs_search(maze):
    """Breadth-First Search (BFS) - Guarantees the shortest path in uniform grids"""
    start = maze.start
    queue = deque([start])
    came_from = {start: None}
    nodes_explored = 0

    while queue:
        current = queue.popleft()
        nodes_explored += 1

        if maze.is_goal(current):
            return reconstruct_path(came_from, current), nodes_explored

        for neighbor in maze.get_neighbors(current):
            if neighbor not in came_from:
                came_from[neighbor] = current
                queue.append(neighbor)
    return None, nodes_explored

def dfs_search(maze):
    """Depth-First Search (DFS) - Does not guarantee the shortest path"""
    start = maze.start
    stack = [start]
    came_from = {start: None}
    nodes_explored = 0

    while stack:
        current = stack.pop()
        nodes_explored += 1

        if maze.is_goal(current):
            return reconstruct_path(came_from, current), nodes_explored

        for neighbor in maze.get_neighbors(current):
            if neighbor not in came_from:
                came_from[neighbor] = current
                stack.append(neighbor)
    return None, nodes_explored

# --- Informed Search Algorithms ---

def a_star_search(maze):
    """A* Search - Combines path cost and heuristic for optimal efficiency"""
    start = maze.start
    goal = maze.goal
    pq = [(0 + manhattan_distance(start, goal), start)]
    came_from = {start: None}
    g_score = {start: 0}
    nodes_explored = 0

    while pq:
        current_f, current = heapq.heappop(pq)
        nodes_explored += 1

        if maze.is_goal(current):
            return reconstruct_path(came_from, current), nodes_explored

        for neighbor in maze.get_neighbors(current):
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + manhattan_distance(neighbor, goal)
                heapq.heappush(pq, (f_score, neighbor))
                came_from[neighbor] = current
    return None, nodes_explored

def greedy_best_first_search(maze):
    """Greedy Best-First Search (GBFS) - Relies solely on the heuristic"""
    start = maze.start
    goal = maze.goal
    pq = [(manhattan_distance(start, goal), start)]
    came_from = {start: None}
    visited = {start}
    nodes_explored = 0

    while pq:
        current_h, current = heapq.heappop(pq)
        nodes_explored += 1

        if maze.is_goal(current):
            return reconstruct_path(came_from, current), nodes_explored

        for neighbor in maze.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                heapq.heappush(pq, (manhattan_distance(neighbor, goal), neighbor))
                came_from[neighbor] = current
    return None, nodes_explored

def reconstruct_path(came_from, current):
    """Backtracks from the goal to the start to reconstruct the final path"""
    path = []
    while current is not None:
        path.append(current)
        current = came_from[current]
    return path[::-1]