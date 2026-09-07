import numpy as np
import os

moves = {"A1": (0, 0), "A2": (0, 1), "A3": (0, 2),
         "B1": (1, 0), "B2": (1, 1), "B3": (1, 2),
         "C1": (2, 0), "C2": (2, 1), "C3": (2, 2)}

turn = 1
board = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
char = [" ", "X", "O"]
players = ["O", "X"]

def printboard(board):
    line = ["A", "B", "C"]
    print("  " + 13 * "-")
    for i in range(3):
        print(line[i] + " | "+char[board[i][0]]+" | "+char[board[i][1]] +" | "+char[board[i][2]]+" |")
        print("  " + 13 * "-")
    print(4 * " " + "1" + 3 * " "+"2" + 3 * " "+"3")

def check_victory(board):
    #check line and column alignment
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0 \
                or board[0][i] == board[1][i] == board[2][i] != 0:
            return True
    #check diagonal alignments
    if board[0][0] == board[1][1] == board[2][2]  != 0 \
        or board[0][2] == board[1][1] == board[2][0]  != 0:
        return True

    return False

while True:
    print(20 * "*")
    print("Turn", turn, ": Player", players[turn % 2])
    print(20 * "*")
    printboard(board)

    move = input("Enter your move:").upper()
    if move not in moves.keys():
        print(move, "is not an authorized move !")
        continue
    coord = moves[move]
    if board[coord[0]][coord[1]] == 0:
        board[coord[0]][coord[1]] = 2 - (turn % 2)
    else:
        print("Square already used !")
        continue
    if turn >=5 and check_victory(board):
        os.system('clear')
        print("Player", players[turn % 2], "won !")
        printboard(board)
        break
    elif turn >=9:
        os.system('clear')
        print("The game is draw !")
        printboard(board)
        break
    turn += 1
    os.system('clear')