from Chess.Pieces.piece import Piece

class Bishop(Piece):
    def __init__(self, color, position, value):
        self.value = value
        self.color = color
        self.position = position
        self.piece = "b" if self.color == -1 else "B"

    def get_moves(self, board):
        valid_moves = []
        directions = [7, -7, 9, -9]
        for direction in directions:
            for i in range(1, 8):
                move = self.position + i * direction
                if not self.is_same_diagonal(move, i):
                    break
                if move  < 0:
                    continue
                if board[self.position + i * direction] is None:
                    valid_moves.append(move)
                elif board[self.position + i * direction].color != self.color:
                    valid_moves.append(move)
                    break
                else:
                    break
        return valid_moves