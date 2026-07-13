class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [['#' for _ in range(width)] for _ in range(height)]
        self.visited = [[False for _ in range(width)] for _ in range(height)]

    def render(self):
        print("\033[H\033[J", end='')
        for row in self.grid:
            print(''.join(row))

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
                self.generate_maze(nx, ny)
                time.sleep(speed)

    def solve_maze(self, start, end):
        stack = [start]
        while stack:
            x, y = stack.pop()
            if (x, y) == end:
                return True
            if self.visited[y][x]:
                continue
            self.visited[y][x] = True
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and self.grid[ny][nx] == '.':
                    stack.append((nx, ny))
        return False

if __name__ == '__main__':
    import argparse
    import random
    import time

    parser = argparse.ArgumentParser(description='Generate and solve mazes.')
    parser.add_argument('--width', type=int, required=True, help='Width of the maze')
    parser.add_argument('--height', type=int, required=True, help='Height of the maze')
    parser.add_argument('--algo', choices=['bfs'], required=True, help='Algorithm to use for solving')
    parser.add_argument('--animate', action='store_true', help='Animate the maze generation')
    args = parser.parse_args()

    maze = Maze(args.width, args.height)
    maze.generate_maze(speed=0.1 if args.animate else 0)
    maze.render()
    if args.algo == 'bfs':
        if maze.solve_maze((0, 0), (args.width - 1, args.height - 1)):
            print("Maze solved!")
        else:
            print("No solution found.")