"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:
Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells 
and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. 
You do not need to return anything.
"""


def sourrounded_regions(board):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    print("\n")

    if len(board) != 1:

        def traverse(board, i, j):
            board[i][j] = "NS"  # mark visited cell as non surroundable
            if i == 0 and board[i + 1][j] == "O":  # Check down
                traverse(board, i + 1, j)
            if i == len(board) - 1 and board[i - 1][j] == "O":  # Check up
                traverse(board, i - 1, j)
            if j == 0 and board[i][j + 1] == "O":  # Check right
                traverse(board, i, j + 1)
            if j == len(board[i]) - 1 and board[i][j - 1] == "O`":  # Check left
                traverse(board, i, j - 1)

        def is_border(board, i, j):
            if i == 0:
                return True
            if j == 0:
                return True
            if i == len(board) - 1:
                return True
            if j == len(board[i]) - 1:
                return True
            return False

        # Scan the board
        for i in range(len(board)):
            for j in range(len(board[i])):
                if is_border(board, i, j) and board[i][j] == "O":
                    traverse(board, i, j)
        # Mark non surroundable with "O"
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "NS":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

    return board


board1 = [["X", "X"], ["O", "O"]]
board2 = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
board3 = [["O", "O", "X"], ["O", "X", "O"], ["X", "X", "X"]]
board4 = [["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"]]
board5 = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]
board6 = [["X"]]
board7 = [["O"]]
board8 = [
    ["O", "X", "X", "O", "X"],
    ["X", "X", "X", "X", "O"],
    ["X", "X", "O", "X", "X"],
    ["O", "X", "X", "X", "O"],
    ["X", "X", "O", "X", "O"],
]

# print(sourrounded_regions(board1))
# print(sourrounded_regions(board2))
# print(sourrounded_regions(board3))
# print(sourrounded_regions(board4))
# print(sourrounded_regions(board5))
# print(sourrounded_regions(board6))
# print(sourrounded_regions(board7))
print(f"{sourrounded_regions(board8)}")
print(
    """ Expected board8:

    [
        ["O", "X", "X", "O", "X"],
        ["X", "X", "X", "X", "O"],
        ["X", "X", "X", "O", "X"],
        ["O", "X", "O", "O", "O"],
        ["X", "X", "O", "X", "O"],
    ]
"""
)

"""[
    ["O", "X", "X", "O", "X"],
    ["X", "X", "X", "X", "O"],
    ["X", "X", "X", "X", "X"],
    ["O", "X", "X", "X", "O"],
    ["X", "X", "O", "X", "O"],
]"""
