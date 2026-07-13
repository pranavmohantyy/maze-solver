from PIL import Image

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

    def export_to_png(self, path):
        img = Image.new('RGB', (self.width, self.height), color='white')
        pixels = img.load()
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == '#':
                    pixels[x, y] = (0, 0, 0)
                elif (x, y) == self.start:
                    pixels[x, y] = (255, 0, 0)
                elif (x, y) == self.end:
                    pixels[x, y] = (0, 255, 0)
        img.save(path)

    def overlay_solution(self, solution_path):
        for x, y in solution_path:
            if (x, y) != self.start and (x, y) != self.end:
                self.grid[y][x] = '.'
