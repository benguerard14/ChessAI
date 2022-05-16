from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, color, piece, value, position):
        self.value = value
        self.color = color
        self.piece = piece
        self.position = position

    @abstractmethod
    def get_moves(self):
        pass
    
    def is_color(self, piece):
        return self.color == piece.color
    
    def move_piece(self, board, move):
        if not move in self.get_moves(board):
            print("Invalid Move!")
            return False
        previous_location = self.position
        self.position = move
        board[move] = self
        board[previous_location] = None
        return True
        