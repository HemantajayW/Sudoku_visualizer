

from xmlrpc.client import boolean



def print_board(board):
    for i in range(len(board)):
        if(i != 0 and i % 3 == 0):
            print("----------------------")
        for k in range(len(board)):
            if(k != 0 and k % 3 == 0):
                print("| ", end="")
            print(board[i][k], end=" ")
        print()


def find_empty(board):
    for i in range(len(board)):
        for k in range(len(board)):
            if(board[i][k] == 0):
                return (i, k)


def isSafe(board, row, col, ele):
    for i in range(len(board)):
        if(board[i][col] == ele or board[row][i] == ele):
            return False
    row = int(row/3)
    col = int(col/3)
    row = row*3
    col = col*3
    for i in range(row, row+3):
        for k in range(col, col+3):
            if(board[i][k] == ele):
                return False
    return True





# board = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
#          [6, 0, 0, 0, 7, 5, 0, 0, 9],
#          [0, 0, 0, 6, 0, 1, 0, 7, 8],
#          [0, 0, 7, 0, 4, 0, 2, 6, 0],
#          [0, 0, 1, 0, 5, 0, 9, 3, 0],
#          [9, 0, 4, 0, 6, 0, 0, 0, 5],
#          [0, 7, 0, 3, 0, 0, 0, 1, 2],
#          [1, 2, 0, 0, 0, 7, 4, 0, 0],
#          [0, 4, 9, 2, 0, 6, 0, 0, 7]]

