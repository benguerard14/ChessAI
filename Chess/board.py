import numpy as np
from Chess.Pieces.piece import * 
from Chess.Pieces.pawn import * 
from Chess.Pieces.bishop import * 
from Chess.Pieces.king import *
from Chess.Pieces.queen import *
from Chess.Pieces.knight import *
from Chess.Pieces.rook import *


normal_setup = ["r", "n", "b", "q", "k", "b", "n", "r",
                " ", "p", "p", " ", "p", "p", "p", "p",
                " ", " ", " ", " ", " ", " ", " ", " ",
                "p", " ", " ", "p", " ", " ", " ", " ",
                " ", " ", " ", " ", " ", " ", " ", " ",
                " ", " ", " ", " ", " ", " ", " ", " ",
                "P", "P", "P", "P", "P", "P", "P", "P",
                "R", "N", "B", "Q", "K", "B", "N", "R"]

def initialize_board(board):
    class_board = [] 
    for i in range(64):
        class_board.append(assign_piece(board[i], i))
    return class_board

def assign_piece(piece, position):
    color = -1 if piece.islower() else 1
    if piece.lower() == "r":
        return Rook(color, position, 5)
    if piece.lower() == "n":
        return Knight(color, position, 3)
    if piece.lower() == "b":
        return Bishop(color, position, 3)
    if piece.lower() == "q":
        return Queen(color, position, 8)
    if piece.lower() == "k":
        return King(color, position, 40) 
    if piece.lower() == "p":
        return Pawn(color, position, 1)
    return None


def class_to_string(board):
    array = []
    for element in board: 
        if element == None:
            array.append(" ")
            continue
        array.append(element.piece)
    return array

def print_board(board):
    str_board = np.array(class_to_string(board))
    print(np.resize(str_board, (8, 8)))