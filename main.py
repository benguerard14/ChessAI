import Chess as cs 
import numpy as np


def main():
    board = cs.initialize_board(cs.normal_setup)
    rook = board[29] 
    cs.print_board(board) 
    print(rook.get_moves(board))

if __name__ == "__main__":
    main()