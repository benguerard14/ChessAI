import Chess as cs 
import numpy as np


def main():
    turn = 0
    turns = [-1, 1]
    board = cs.initialize_board(cs.normal_setup)
    print("Welcome to Scuffed Chess!")
    while True:
        cs.print_board(board)
        piece = input("What is the piece you want to move? ")
        move = input("What is the move you want to make? ")
        move = cs.pos_to_num(move)
        piece = cs.pos_to_num(piece)
        print(move)
        board[piece].move_piece(board, move)

if __name__ == "__main__":
    main()