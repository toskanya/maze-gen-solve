from mazesolve import *
from mazegenerate import *

while True:
    user_grid_txt = input("Enter the size (ex: 10 10): ")
    user_grid = tuple([int(e) for e in user_grid_txt.split()])
    maze_txt = mazeGen(user_grid)
  
    while True:
        maze = Maze(maze_txt)
        maze.print()
        algorithm = SolveMaze()
        
        user_algorithm = input("Choose an algorithm (DFS, BFS, A*, GBFS): ")
        if (user_algorithm == "reset"):
            break
        algorithm.solve(maze, user_algorithm)
        maze.draw()
