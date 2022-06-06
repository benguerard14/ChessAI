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
    
    def is_same_x(self, move):
        return self.position % 8 == move % 8
    def is_same_y(self, move):
        return self.position // 8 == move // 8
    def is_same_diagonal(self, move, i):
        return not ((move % 8) + i  != self.position % 8 and (move % 8) - i != self.position % 8)

    def move_piece(self, board, move):
        if not move in self.get_moves(board):
            print("Invalid Move!")
            return False
        previous_location = self.position
        self.position = move
        board[move] = self
        board[previous_location] = None
        return True
        
