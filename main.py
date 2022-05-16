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
    bishop = board[2] 
    print(bishop)
    print(bishop.get_moves(board))

if __name__ == "__main__":
    main()