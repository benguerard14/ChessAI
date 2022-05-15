from Pieces.piece import Piece

class Knight(Piece):
    def __init__(self, color, position, value):
        self.value = value
        self.color = color
        self.position = position
        self.piece = "n" if self.color == -1 else "N"

    def get_moves(self, board):
        valid_moves = []
        return valid_moves