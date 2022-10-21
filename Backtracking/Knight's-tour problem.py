# Given a N*N board with the Knight placed on the first block of an empty board.
# Moving according to the rules of chess knight must visit each square exactly once.
# Print the order of each cell in which they are visited.
# from geeksforgeeks
n = 6


def isSafe(x, y, board):
    if 0 <= x < n and 0 <= y < n and board[x][y] == -1:
        return True
    return False


def printSolution(n, board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()


def solveKT(n):
    board = [[-1 for x in range(8)] for i in range(n)]
    moveX = [1, 2, 1, 2, -1, -2, -1, -2]
    moveY = [2, 1, -2, -1, 2, 1, -2, -1]
    board[0][0]=0
    pos=1
    if solveKTUtil(n, board, 0, 0, moveX, moveY, pos):
        printSolution(n, board)
    else:
        print('solution does\'nt exist')

def solveKTUtil(n, board, curr_x ,curr_y, move_x, move_y,pos):
    if pos==n*n:
        return True

    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if (isSafe(new_x, new_y, board)):
            board[new_x][new_y] = pos
            if (solveKTUtil(n, board, new_x, new_y, move_x, move_y, pos + 1)):
                return True

            # Backtracking
            board[new_x][new_y] = -1
    return False


solveKT(n)