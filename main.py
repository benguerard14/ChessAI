import Chess as chess
import numpy as np


def main():
    board = chess.initialize_board(chess.normal_setup)
    bishop = board[2] 
    print(bishop)
    print(bishop.get_moves(board))

if __name__ == "__main__":
    main()