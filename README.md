# Maze Solver

This project generates and solves mazes using various algorithms with ASCII visualization.

## Algorithms

1. **Depth-First Search (DFS)**: A simple algorithm that explores as far as possible along each branch before backtracking.

2. **Breadth-First Search (BFS)**: This algorithm explores all neighbor nodes at the present depth prior to moving on to nodes at the next depth level.

3. **A* Search**: This algorithm finds the shortest path by combining the cost to reach a node and the estimated cost to reach the goal.

## Example Usage

To create a maze, instantiate the `Maze` class:
```python
maze = Maze(width, height)
```

To render the maze:
```python
maze.render()
```

To solve the maze:
```python
maze.solve()  # This will use the default algorithm
```

## Installation

Make sure you have Pillow installed:
```bash
pip install Pillow
```

## License

This project is licensed under the MIT License.