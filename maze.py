class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [['#' for _ in range(width)] for _ in range(height)]
        self.visited = [[False for _ in range(width)] for _ in range(height)]

    def render(self):
        for row in self.grid:
            print(''.join(row))

    def set_passage(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = '.'

    def generate_maze(self, x=0, y=0):
        self.visited[y][x] = True
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height and not self.visited[ny][nx]:
                self.set_passage(x + dx // 2, y + dy // 2)
                self.generate_maze(nx, ny)

    def solve_maze(self, x=0, y=0):
        if x == self.width - 1 and y == self.height - 1:
            return True
        if 0 <= x < self.width and 0 <= y < self.height and not self.visited[y][x] and self.grid[y][x] == '.':
            self.visited[y][x] = True
            if self.solve_maze(x + 1, y) or self.solve_maze(x - 1, y) or self.solve_maze(x, y + 1) or self.solve_maze(x, y - 1):
                self.grid[y][x] = '*'  # Mark path
                return True
            self.visited[y][x] = False
        return False
