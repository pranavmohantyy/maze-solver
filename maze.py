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

    def bfs_solver(self, start, end):
        from collections import deque
        queue = deque([start])
        came_from = {start: None}
        while queue:
            current = queue.popleft()
            if current == end:
                break
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                neighbor = (current[0] + dx, current[1] + dy)
                if 0 <= neighbor[0] < self.width and 0 <= neighbor[1] < self.height:
                    if self.grid[neighbor[1]][neighbor[0]] == '.' and neighbor not in came_from:
                        queue.append(neighbor)
                        came_from[neighbor] = current
                        self.set_passage(neighbor[0], neighbor[1])
        return self.reconstruct_path(came_from, start, end)

    def reconstruct_path(self, came_from, start, end):
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path