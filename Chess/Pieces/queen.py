from Chess.Pieces.piece import Piece

class Queen(Piece):
    def __init__(self, color, position, value):
        self.value = value
        self.color = color
        self.position = position
        self.piece = "q" if self.color == -1 else "Q"

    def get_moves(self, board):
        valid_moves = []
        return valid_moves