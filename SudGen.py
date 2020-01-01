from solver import Sudoku
import copy
import random
class SudokuGen(Sudoku):

    """
    Generates solvable sudoku puzzle
    """
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

    diff = {'easy': 58, 'medium': 61, 'hard': 64}

    def __init__(self, d='medium'):
        pops_left = self.diff[d]
        self.create()
        positions = []
        while pops_left > 0:
            rand_pos = [random.randint(0, 8), random.randint(0, 8)]
            if rand_pos not in positions:
                row, col = rand_pos[0], rand_pos[1]
                self.board[row][col] = 0
                positions.append(rand_pos)
                pops_left -= 1


    def create(self):
        """
        Creates random sudoku puzzle, solved
        """

        empty = self.find_empty()
        if not empty:
            return True
        row, col = empty

        for i in self.random_list():
            if self.is_valid(i, [row, col]):
                self.replace(i, [row, col])
                if self.create():
                    return True
                self.replace(0, [row, col])
        return False


    def random_list(self):
        lst = list(range(1, 10))
        random.shuffle(lst)
        return lst
