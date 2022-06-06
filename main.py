import Chess as cs 
import random
from copy import deepcopy

def minimax(board, is_maximizing, depth, alpha, beta):
    if cs.game_state(board) != 0 or depth == 0:
        values = cs.return_values(board)
        return values[0] - values[1]
    pieces = cs.get_pieces(board, is_maximizing)
    move_values = []
    for piece in pieces:
        for move in piece.get_moves(board):
            new_board = deepcopy(board) 
            new_board[piece.position].move_piece(new_board, move)
            move_value = minimax(new_board, not is_maximizing, depth - 1, alpha, beta)
            move_values.append(move_value)

         
def main():
    turn = 0
    turns = [-1, 1]
    board = cs.initialize_board(cs.normal_setup)
    print("Welcome to Scuffed Chess!")
    while True:
        cs.print_board(board)
        ai = input("AI? y/n: ")
        if ai == "y":
            moves = minimax(board, not (turn % 2), 4, float("inf"), -float("inf"))
            print(moves)
            piece = cs.pos_to_num(moves[0])
            if board[piece] == None or board[piece].color == turns[turn % 2]:
                print("Invalid piece")
                continue
            move = cs.pos_to_num(moves[1])
        else:
            piece = input("What is the piece you want to move? ")
            piece = cs.pos_to_num(piece)
            if board[piece] == None or board[piece].color == turns[turn % 2]:
                print("Invalid piece")
                continue
            move = input("What is the move you want to make? ")
            move = cs.pos_to_num(move)
        board[piece].move_piece(board, move)
        turn += 1

if __name__ == "__main__":
    main()
