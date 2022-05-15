from ctypes import resize
from Pieces.pawn import * 
from Pieces.rook import *
from Pieces.bishop import *
from Pieces.knight import *
from Pieces.queen import *
from Pieces.king import *
from board import * 
import numpy as np


def main():
    board = string_to_class(normal_setup)
    pawn = board[10]
    pawn.move_piece(board, 18)
    pawn = board[54]
    pawn.move_piece(board, 38)
    print_board(board)

if __name__ == "__main__":
    main()