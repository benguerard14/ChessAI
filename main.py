import Chess as cs 
import random
from copy import deepcopy

def minimax(board, is_maximizing, depth, alpha, beta):
    if cs.game_state(board) != 0 or depth == 0:
        values = cs.return_values(board)
        return [0, 0, values[0] - values[1]]
    pieces = cs.get_pieces(board, is_maximizing)
    move_values = []
    broke = False
    for piece in pieces:
        for move in piece.get_moves(board):
            new_board = deepcopy(board) 
            new_board[piece.position].move_piece(new_board, move)
            move_value = minimax(new_board, not is_maximizing, depth - 1, alpha, beta)
            if move_value == None:
                continue
            print(move_value, depth)
            move_value[0] = piece.position
            move_value[1] = move
            move_values.append(move_value)
            if not is_maximizing:
                if move_value[2] > alpha:
                    alpha = move_value
            else:
                if move_value[2] < beta:
                    beta = move_value
            if alpha <= beta:
                print("AB:  " + str(alpha) + str(beta))
                print("end")
                broke = True
                break
        if broke:
            break
    if is_maximizing:
        best_value = max([x[2] for x in move_values])
    else:
        best_value = min([x[2] for x in move_values])
    moves = [move if move[2] == best_value else None for move in move_values]
    return random.choice(moves) 
         
def main():
    turn = 0
    turns = [-1, 1]
    board = cs.initialize_board(cs.normal_setup)
    print("Welcome to Scuffed Chess!")
    while True:
        cs.print_board(board)
        ai = input("AI? y/n: ")
        if ai == "y":
            moves = minimax(board, not (turn % 2), 3, 100, -100)
            print(cs.num_to_pos(moves[0]), cs.num_to_pos(moves[1]), moves[2])
            piece = moves[0]
            if board[piece] == None or board[piece].color == turns[turn % 2]:
                print("Invalid piece")
                continue
            move = moves[1]
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
