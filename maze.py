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

    def a_star_search(self, start, goal):
        open_set = {start}
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.manhattan_distance(start, goal)}

        while open_set:
            current = min(open_set, key=lambda pos: f_score.get(pos, float('inf')))
            if current == goal:
                return self.reconstruct_path(came_from, current)

            open_set.remove(current)
            for neighbor in self.get_neighbors(current):
                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.manhattan_distance(neighbor, goal)
                    open_set.add(neighbor)

        return []  # No path found

    def manhattan_distance(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def get_neighbors(self, pos):
        x, y = pos
        neighbors = []
        if x > 1: neighbors.append((x - 2, y))
        if x < self.width - 2: neighbors.append((x + 2, y))
        if y > 1: neighbors.append((x, y - 2))
        if y < self.height - 2: neighbors.append((x, y + 2))
        return [n for n in neighbors if 0 <= n[0] < self.width and 0 <= n[1] < self.height]

    def reconstruct_path(self, came_from, current):
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        return total_path[::-1]  # Return reversed path