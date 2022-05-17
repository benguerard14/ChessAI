import Chess as cs 
import numpy as np


def main():
    board = cs.initialize_board(cs.normal_setup)
    print("Welcome to Scuffed Chess!")
    while True:
        cs.print_board(board)
        piece = int(input("What is the piece you want to move? ")) 
        move = int(input("What is the move you want to make? "))
        board[piece].move_piece(board, move)

if __name__ == "__main__":
    main()