from Chess.Pieces.piece import Piece

class Pawn(Piece):
    def __init__(self, color, position, value):
        self.value = value
        self.color = color
        self.position = position 
        self.piece = "p" if self.color == -1 else "P"

    def get_moves(self, board):
        valid_moves = []
        if self.position - 8 >= 0:
            if board[self.position - 8 * self.color] is None:
                valid_moves.append(self.position - 8 * self.color)
                if self.position - 16 >= 0:
                    if board[self.position - 16 * self.color] is None and self.position // 8 == (1 if self.color == -1 else 6):
                        valid_moves.append(self.position - 16 * self.color)
        if self.position - 7 >= 0:
            if board[self.position - 7 * self.color] is not None and board[self.position - 7 * self.color].color != self.color:
                if self.is_same_diagonal(self.position - 7 * self.color, 1):
                    valid_moves.append(self.position - 7 * self.color)
        if self.position - 9 >= 0:
            if board[self.position - 9 * self.color] is not None and board[self.position - 9 * self.color].color != self.color:
                if self.is_same_diagonal(self.position - 9 * self.color, -1):
                    valid_moves.append(self.position - 9 * self.color)
        return valid_moves
