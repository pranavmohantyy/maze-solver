from PIL import Image

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [['#' for _ in range(width)] for _ in range(height)]
        self.visited = [[False for _ in range(width)] for _ in range(height)]
        self.start = (0, 0)
        self.end = (width - 1, height - 1)
        self.nodes_explored = 0
        self.path_length = 0
        self.solve_time = 0

    def render(self):
        print("\033[H\033[J", end='')
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                print(cell, end='')
            print()  
        print(f'Nodes explored: {self.nodes_explored}, Path length: {self.path_length}')
