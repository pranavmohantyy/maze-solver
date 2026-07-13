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
                    print('\033[94mE\033[0m', end='')
                elif self.visited[y][x]:
                    print('\033[92m.\033[0m', end='')
                else:
                    print(cell, end='')
            print()

    def set_passage(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = '.'

    def generate_maze(self, x=0, y=0, speed=0.1):
        self.visited[y][x] = True
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < self.width and 0 <= ny < self.height and not self.visited[ny][nx]:
                self.set_passage(x + dx, y + dy)
                self.generate_maze(nx, ny, speed)
                time.sleep(speed)
