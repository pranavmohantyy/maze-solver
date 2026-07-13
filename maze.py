class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [['#' for _ in range(width)] for _ in range(height)]
        self.visited = [[False for _ in range(width)] for _ in range(height)]
        self.start = (0, 0)
        self.end = (width - 1, height - 1)

    def render(self):
        print("\033[H\033[J", end='')
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if (x, y) == self.start:
                    print('\033[91mS\033[0m', end='')
                elif (x, y) == self.end:
                    print('\033[92mE\033[0m', end='')
                else:
                    print(cell, end='')
            print()  

    def generate_maze(self):
        self.grid[1][1] = ' '
        walls = [(1, 2), (2, 1)]
        while walls:
            wall = walls.pop()  
            x, y = wall
            if 0 < x < self.width - 1 and 0 < y < self.height - 1:
                if (self.grid[y - 1][x] == ' ' and self.grid[y + 1][x] == ' ') or (self.grid[y][x - 1] == ' ' and self.grid[y][x + 1] == ' '):
                    self.grid[y][x] = ' '
                    if x - 1 > 0:
                        walls.append((x - 1, y))
                    if x + 1 < self.width - 1:
                        walls.append((x + 1, y))
                    if y - 1 > 0:
                        walls.append((x, y - 1))
                    if y + 1 < self.height - 1:
                        walls.append((x, y + 1))

    def prims_algorithm(self):
        self.grid = [['#' for _ in range(self.width)] for _ in range(self.height)]
        self.visited = [[False for _ in range(self.width)] for _ in range(self.height)]
        self.grid[1][1] = ' '
        walls = [(1, 2), (2, 1)]
        while walls:
            wall = walls.pop()
            x, y = wall
            if 0 < x < self.width - 1 and 0 < y < self.height - 1:
                if (self.visited[y - 1][x] + self.visited[y + 1][x] + self.visited[y][x - 1] + self.visited[y][x + 1]) == 1:
                    self.grid[y][x] = ' '
                    self.visited[y][x] = True
                    if x - 1 > 0:
                        walls.append((x - 1, y))
                    if x + 1 < self.width - 1:
                        walls.append((x + 1, y))
                    if y - 1 > 0:
                        walls.append((x, y - 1))
                    if y + 1 < self.height - 1:
                        walls.append((x, y + 1))

