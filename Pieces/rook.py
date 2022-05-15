from Pieces.piece import Piece

class Rook(Piece):
    def __init__(self, color, position, value):
        self.value = value 
        self.color = color
        self.position = position
        self.piece = "r" if self.color == -1 else "R"

    def get_moves(self, board):
        valid_moves = []
        return valid_moves