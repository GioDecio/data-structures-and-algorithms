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

    def traverse(board, i, j):

        board[i][j] = "X"  # mark cell as visited

        # Scan adjacent cells
        if j == len(board[i]) - 2:
            pass
        else:
            if j + 1 < len(board[i]) and board[i][j + 1] == "O":  # check right
                traverse(board, i, j + 1)
        if i == len(board) - 2:
            pass
        else:
            if i + 1 < len(board) and board[i + 1][j] == "O":  # check down
                traverse(board, i + 1, j)
        if i == 1:
            pass
        else:
            if i - 1 > 0 and board[i - 1][j] == "O":  # check up
                traverse(board, i - 1, j)
        if j == 1:
            pass
        else:
            if (
                j - 1 < len(board[i]) and j - 1 >= 0 and board[i][j - 1] == "O"
            ):  # check left
                traverse(board, i, j - 1)

    for i in range(len(board)):
        for j in range(len(board[i]) - 1):
            if board[i][j] == "O" and not is_border(board, i, j):
                if (
                    (board[i - 1][j] == "O" and is_border(board, i - 1, j))
                    or (board[i + 1][j] == "O" and is_border(board, i + 1, j))
                    or (board[i][j - 1] == "O" and is_border(board, i, j - 1))
                    or (board[i][j + 1] == "O" and is_border(board, i, j + 1))
                ):
                    pass
                else:
                    traverse(board, i, j)
            else:
                pass
    return board


board1 = [["X", "X"], ["O", "O"]]
board2 = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
print(sourrounded_regions(board1))
print(sourrounded_regions(board2))
