import os

class Solver:
    def __init__(self, board: list):
        self.board = board
        self.visited = False
        self.start, self.finish = self.get_starting_finishing_points()
        self.stack = [self.start]
        
    def get_starting_finishing_points(self):
        _start = [i for i in range(len(self.board[0])) if self.board[0][i] == '.']
        _end = [i for i in range(len(self.board[0])) if self.board[len(self.board)-1][i] == '.']
        return [0, _start[0]], [len(self.board) - 1, _end[0]]

    def solver_backtracking(self):
        self.board[self.start[0]][self.start[1]] = 'o'
        self.backtrack()

    def backtrack(self):
        while self.stack:
            current_cell = self.stack[-1]
            if current_cell == self.finish:
                return
            moved = False
            if current_cell[0] + 1 < len(self.board) and self.board[current_cell[0] + 1][current_cell[1]] == '.':
                self.board[current_cell[0] + 1][current_cell[1]] = 'o'
                self.stack.append([current_cell[0] + 1, current_cell[1]])
                moved = True
            elif current_cell[1] + 1 < len(self.board[0]) and self.board[current_cell[0]][current_cell[1] + 1] == '.':
                self.board[current_cell[0]][current_cell[1] + 1] = 'o'
                self.stack.append([current_cell[0], current_cell[1] + 1])
                moved = True
            elif current_cell[0] - 1 >= 0 and self.board[current_cell[0] - 1][current_cell[1]] == '.':
                self.board[current_cell[0] - 1][current_cell[1]] = 'o'
                self.stack.append([current_cell[0] - 1, current_cell[1]])
                moved = True
            elif current_cell[1] - 1 >= 0 and self.board[current_cell[0]][current_cell[1] - 1] == '.':
                self.board[current_cell[0]][current_cell[1] - 1] = 'o'
                self.stack.append([current_cell[0], current_cell[1] - 1])
                moved = True
            if not moved:
                cell_to_remove = self.stack.pop()
                self.board[cell_to_remove[0]][cell_to_remove[1]] = '*'

    def astar(self):
        pass 

    def print_maze(self):
        maze_str=""
        for row in range(len(self.board)):
            maze_str+="".join(self.board[row])+'\n'
        print(maze_str)
        return maze_str

    def save_file(self, generation: str):
        name = input('Enter the desired filename (without extension): ')
        if generation == "astar":
            pass
        elif generation == "backtracking":
            self.solver_backtracking()
        maze_text = self.print_maze()
        folder_maze = './solver/maze_solved/' + generation
        name_with_underscores = name.replace(' ', '_')
        if not os.path.exists(folder_maze):
            os.makedirs(folder_maze)
        name_file =  os.path.join(folder_maze, f'{name_with_underscores}.txt')
        with open(name_file, 'w') as file:
            file.write(maze_text)
        print(f'The solving maze was registered under the name {name_file}')

    def choosing_solver(self):
        while True:
            print(' ')
            print("Chooze maze solver algorithm")
            print("1 - Astar algorithm")
            print('2 - Backtracking algorithm')
            print('3 - Leave')
            print(' ')
            number = input('Enter a number > ')
            print(' ')
            if number.isdigit() == False:
                print(' ')
                print('Enter a number between 1 and 2 !')
                print(' ')
            elif number == "1":
                self.save_file("astar")
                break
            elif number == "2":
                self.save_file("backtracking")
                break
            elif number == "3":
                break
            else:
                print(' ')
                print('Enter a valid number !')
                print(' ')