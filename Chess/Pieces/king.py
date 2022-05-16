from Chess.Pieces.piece import Piece

class King(Piece):
    def __init__(self, color, position, value):
        self.value = value 
        self.color = color
        self.position = position
        self.piece = "k" if self.color == -1 else "K"

    def get_moves(self, board):
        valid_moves = []
        return valid_moves