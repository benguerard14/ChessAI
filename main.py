from Pieces.pawn import * 
from Pieces.rook import *
from Pieces.bishop import *
from Pieces.knight import *
from Pieces.queen import *
from Pieces.king import *
from board import * 
import numpy as np


def main():
    board = initialize_board(normal_setup)
    pawn = board[10]
    pawn.move_piece(board, 26)
    pawn1 = board[51]
    print(pawn.get_moves(board))
    pawn1.move_piece(board, 35)
    print(pawn.get_moves(board))
    print_board(board)

if __name__ == "__main__":
    main()