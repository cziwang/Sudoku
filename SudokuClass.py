
class Sudoku:

    count = 0

    def __init__(self, board):
        self.board = board

    def is_valid(self, num, pos):
        """
        Checks if num is valid in the given position of the self.board.
        For the num to be valid, num must not exist in the row,
        and the column, and its 3x3 box
        """
        if self.count > 100000:
            raise InvalidBoard('The board is unsolveable!')
        #Check if num already exists in the same row row already (horizontal check)
        row = pos[0]
        if num in self.board[row]:
            return False

        #Check if num already exists in the same column; go over every row with same x index
        for row in self.board:
            if num == row[pos[1]]:
                return False

        #Check if num already exists in the its corresponding 3x3 subgrid
        sub = self.subgrid(pos)
        for row in sub:
            if num in row:
                return False

        return True

    def subgrid(self, pos):
        """ Returns the corresponding subgrid (3x3) given a position """
        row, col = pos[0] // 3 * 3, pos[1] // 3 * 3
        rows = self.board[row:row+3]
        sub = []
        for row in rows:
            sub.append(row[col:col+3])
        return sub

    def solve(self):
        """
        Solves Sudoku Puzzle
        """
        self.count += 1

        empty = self.find_empty()
        if not empty:
            return True
        row, col = empty

        for i in range(1, 10):
            if self.is_valid(i, [row, col]):
                self.replace(i, [row, col])
                if self.solve():
                    return True
                self.replace(0, [row, col])
        return False


    def replace(self, num, pos):
        """
        Replaces number of self.board with num at pos
        """
        row, col = pos[0], pos[1]
        self.board[row][col] = num


    def find_empty(self):
        """
        Find the position of an empty slot in the self.board, and return it.
        If all spots are filled, return None
        """
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == 0:
                    return row, col
        return None


    def __repr__(self):
        for row in range(len(self.board)):
            if row % 3 == 0 and row != 0:
                print('----------------')
            for col in range(len(self.board[0])):
                if col % 3 == 0 and col != 0:
                    print(' | ', end="")

                if col == 8:
                    print(self.board[row][col])
                else:
                    print(self.board[row][col], end = "")
        return ""
