import random

class Maze:
    def __init__(self, width, height, density=0.3):

        self.width = width
        self.height = height
        self.density = density
        self.grid = []
        self.start = (0, 0)
        self.goal = (height - 1, width - 1)
        self.generate_maze()

    def generate_maze(self):
        """Generates the maze grid based on the specified density"""
        self.grid = []
        for r in range(self.height):
            row = []
            for c in range(self.width):
                # Randomly place a wall (1) or a path (0) based on density
                if random.random() < self.density:
                    row.append(1) # 1 represents a wall
                else:
                    row.append(0) # 0 represents a path
            self.grid.append(row)
        
        # Ensure that the start and goal points are paths, not walls
        self.grid[self.start[0]][self.start[1]] = 0
        self.grid[self.goal[0]][self.goal[1]] = 0

    def get_neighbors(self, pos):
        """Returns available neighboring nodes (non-walls) for a given position"""
        row, col = pos
        neighbors = []
        # Four movement directions: Right, Left, Down, Up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.height and 0 <= c < self.width and self.grid[r][c] == 0:
                neighbors.append((r, c))
        return neighbors

    def is_goal(self, pos):
        """Checks if the current position is the goal"""
        return pos == self.goal