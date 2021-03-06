"""
Contains lists which can be utilized in terminal for testing purposes.
All boards below should be solve able with

s = Sudoku(<board>)
s.solve()

with the exception of impossibleBoard, in which an error is raised
"""


board = [
    [0, 0, 4, 0, 1, 0, 5, 0, 0],
    [0, 1, 0, 0, 2, 0, 0, 3, 0],
    [5, 0, 0, 4, 0, 3, 0, 0, 2],
    [0, 0, 2, 0, 0, 0, 6, 0, 0],
    [7, 8, 0, 0, 9, 0, 0, 4, 5],
    [0, 0, 5, 0, 0, 0, 7, 0, 0],
    [9, 0, 0, 8, 0, 1, 0, 0, 6],
    [0, 7, 0, 0, 6, 0, 0, 5, 0],
    [0, 0, 8, 0, 4, 0, 9, 0, 0]
    ]

a = [
    [0, 8, 0, 0, 0, 9, 7, 4, 3],
    [0, 5, 0, 0, 0, 8, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 8, 0, 4, 0, 0, 0],
    [0, 0, 0, 3, 0, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 7, 0],
    [0, 3, 0, 5, 0, 0, 0, 8, 0],
    [9, 7, 2, 4, 0, 0, 0, 5, 0]
    ]
impossibleBoard = [
    [2, 0, 0, 9, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [5, 0, 2, 6, 0, 0, 4, 0, 7],
    [0, 0, 0, 0, 0, 4, 1, 0, 0],
    [0, 0, 0, 0, 9, 8, 0, 2, 3],
    [0, 0, 0, 0, 0, 3, 0, 8, 0],
    [0, 0, 5, 0, 1, 0, 0, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 0, 0]
     ]
c = [
    [8, 0, 0, 0, 0, 5, 0, 9, 0],
    [0, 0, 7, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 8, 0, 6, 0, 0, 0],
    [0, 0, 4, 2, 0, 0, 0, 8, 5],
    [0, 0, 0, 0, 0, 0, 0, 0, 9],
    [0, 0, 8, 9, 0, 0, 3, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 7, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 7, 0, 0, 0]
    ]
