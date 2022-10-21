# Given a N*N board with the Knight placed on the first block of an empty board.
# Moving according to the rules of chess knight must visit each square exactly once.
# Print the order of each cell in which they are visited.
# from geeksforgeeks
n = int(input())


def issafe(x, y, board):
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

def solveKTUtil(n, board, currX ,currY, moveX, moveY,pos):
    if pos==n*n:
        return True

    for i in range(8):
        newX = currX + moveX[i]
        newY = currY + moveY[i]
        if issafe(newX, newY, board):
            currX=newX
            currY = newY
            board[newX][newY] = pos
            pos+=1
            if solveKTUtil(n, board, currX,currY,moveX,moveY,pos):
                return True
            board[newX][newY]=-1
    return False




