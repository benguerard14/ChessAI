import Chess as chess
import numpy as np


def main():
    board = chess.initialize_board(chess.normal_setup)
    rook = board[0] 
    print(rook.get_moves(board))

if __name__ == "__main__":
    main()