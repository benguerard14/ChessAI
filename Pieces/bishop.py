from Pieces.piece import Piece

class Bishop(Piece):
    def __init__(self, color, position, value):
        self.value = value
        self.color = color
        self.position = position
        self.piece = "b" if self.color == -1 else "B"

    def get_moves(self, board):
        valid_moves = []
        return valid_moves