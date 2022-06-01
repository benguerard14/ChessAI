import Chess as cs 
import random
from copy import deepcopy

def minimax(board, is_maximizing, depth):
    if cs.game_state(board) != 0 or depth == 0:
        values = cs.return_values(board)
        return values[0] - values[1]
    pieces = cs.get_pieces(board, not is_maximizing)
    all_moves = [[piece.position, piece.get_moves(board)] for piece in pieces] 
    best_value = -100 if is_maximizing else 100
    best_move = []
    for piece_move in all_moves:
        for move in piece_move[1]:
            new_board = deepcopy(board)
            new_board[piece_move[0]].move_piece(new_board, move)
            value = minimax_layers(new_board, not(is_maximizing), depth - 1)
            if value == best_value:
                best_move.append([cs.num_to_pos(piece_move[0]), cs.num_to_pos(move)])
            elif (is_maximizing and value > best_value) or (not is_maximizing and value < best_value):
                best_value = value
                best_move.clear()
                best_move.append([cs.num_to_pos(piece_move[0]), cs.num_to_pos(move)])
    return random.choice(best_move)


def minimax_layers(board, is_maximizing, depth):
    if cs.game_state(board) != 0 or depth == 0:
        values = cs.return_values(board)
        return values[0] - values[1]
    pieces = cs.get_pieces(board, not is_maximizing)
    all_moves = [[piece.position, piece.get_moves(board)] for piece in pieces] 
    values = []
    for piece_move in all_moves:
        for move in piece_move[1]:
            new_board = deepcopy(board)
            new_board[piece_move[0]].move_piece(new_board, move)
            value = minimax_layers(new_board, not(is_maximizing), depth - 1)
            values.append(value)
    if is_maximizing:
        return max(values)
    else:
        return min(values)
            
        
def main():
    turn = 0
    turns = [-1, 1]
    board = cs.initialize_board(cs.normal_setup)
    print("Welcome to Scuffed Chess!")
    while True:
        cs.print_board(board)
        piece = input("What is the piece you want to move? ")
        piece = cs.pos_to_num(piece)
        if board[piece] == None or board[piece].color == turns[turn % 2]:
            print("Invalid piece")
            continue
        move = input("What is the move you want to make? ")
        move = cs.pos_to_num(move)
        board[piece].move_piece(board, move)
        turn += 1
        print(minimax(board, turn % 2, 3))
        cs.print_board(board)
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
