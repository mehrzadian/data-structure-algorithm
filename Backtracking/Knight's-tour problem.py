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
            print(board[i][j],end=" ")
        print()

def solveKT(n):
    board = [[-1 for x in range(8)] for i in range(n)]
    if ==0:
