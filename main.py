import Chess as cs 
import numpy as np

def minimax(board, is_maximizing, depth):
    if cs.game_state != 0 or depth == 0:
        pass #end minimaxing


def main():
    turn = 0
    turns = [-1, 1]
    board = cs.initialize_board(cs.normal_setup)
    print("Welcome to Scuffed Chess!")
    while True:
        cs.print_board(board)
        piece = input("What is the piece you want to move? ")
        piece = cs.pos_to_num(piece)
        if board[piece].color == turns[turn] or board[piece] == None:
            print("Invalid piece")
            continue
        move = input("What is the move you want to make? ")
        move = cs.pos_to_num(move)
        board[piece].move_piece(board, move)
        turn += 1
        print(cs.return_values(board))

if __name__ == "__main__":
    main()
