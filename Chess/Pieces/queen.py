from re import S
from Chess.Pieces.piece import Piece

class Queen(Piece):
    def __init__(self, color, position, value):
        self.value = value
        self.color = color
        self.position = position
        self.piece = "q" if self.color == -1 else "Q"

    def get_moves(self, board):
        valid_moves = []
        directions = [7, -7, 9, -9, 1, -1, 8, -8]
        for direction in directions:
            for i in range(1, 8):
                move = self.position + i * direction
                if (not self.is_same_diagonal(move, i) and direction % 2 == 1) or move < 0:
                    break
                if not (self.is_same_y or (direction != 1 or direction != -1)) and direction % 2 == 0:
                    break
                if board[self.position + i * direction] is None:
                    valid_moves.append(move)
                elif board[self.position + i * direction].color != self.color:
                    valid_moves.append(move)
                    break
                else:
                    break
        return valid_moves