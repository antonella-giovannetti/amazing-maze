import time
from classes.Maze import *
from classes.Solver import * 

maze = Maze("MyMaze", 100)  

print('Generation maze')
start_time = time.time()
maze.backtracking()
end_time = time.time()

execution_time = end_time - start_time
print(f"Backtracking method : {execution_time} seconds")

start_time = time.time()
maze.kruskal()
end_time = time.time()

execution_time = end_time - start_time
print(f"Kruskal method : {execution_time} seconds")

print('')
print('Solving maze')

content = maze.print_maze()
lines = content.split('\n')
board= [list(line) for line in lines]
solver = Solver(board)
start_time = time.perf_counter()  
solver.solver_backtracking()
end_time = time.perf_counter()  

execution_time = end_time - start_time
print(f"Backtracking method : {execution_time} seconds")
