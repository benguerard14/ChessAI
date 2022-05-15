from selectors import SelectorKey
from Pieces.piece import Piece

class Pawn(Piece):
    def __init__(self, color, position, value):
        self.value = value
        self.color = color
        self.position = position 
        self.piece = "p" if self.color == -1 else "P"

    def get_moves(self, board):
        valid_moves = [] 
        if board[self.position - 8 * self.color] is None:
            valid_moves.append(self.position - 8 * self.color)
            if board[self.position - 16 * self.color] is None and self.position // 8 == (1 if self.color == -1 else 6):
                valid_moves.append(self.position - 16 * self.color)
        return valid_moves
