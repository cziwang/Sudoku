"""
Used to help write methods in the Sudoku class in solver.py
"""



def is_valid(board, num, pos):
    """
    Checks if num is valid in the given position of the board.
    For the num to be valid, num must not exist in the row,
    and the column, and its 3x3 box
    """
    #Check if num already exists in the same row row already (horizontal check)
    row = pos[0]
    if num in board[row]:
        return False

    #Check if num already exists in the same column; go over every row with same x index
    for row in board:
        if num == row[pos[1]]:
            return False

    #Check if num already exists in the its corresponding 3x3 subgrid
    sub = subgrid(board, pos)
    for row in sub:
        if num in row:
            return False

    return True

def subgrid(board, pos):
    """ Returns the corresponding subgrid (3x3) given a position """
    row, col = pos[0] // 3 * 3, pos[1] // 3 * 3
    rows = board[row:row+3]
    sub = []
    for row in rows:
        sub.append(row[col:col+3])
    return sub

def solve(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            replace(board, i, (row, col))
            if solve(board):
                return True
            replace(board, 0, (row, col))
    return False


def replace(board, num, pos):
    row, col = pos[0], pos[1]
    board[row][col] = num

def find_empty(board):
    """
    Find the position of an empty slot in the board, and return it.
    If all spots are filled, return None
    """
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return row, col

    return None


def print_board(board):
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print('----------------')
        for col in range(len(board[0])):
            if col % 3 == 0 and col != 0:
                print(' | ', end="")

            if col == 8:
                print(board[row][col])
            else:
                print(board[row][col], end = "")
