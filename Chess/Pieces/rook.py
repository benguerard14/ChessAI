from Chess.Pieces.piece import Piece

class Rook(Piece):
    def __init__(self, color, position, value):
        self.value = value 
        self.color = color
        self.position = position
        self.piece = "r" if self.color == -1 else "R"

    def get_moves(self, board):
        valid_moves = []
        directions = [1, -1, 8, -8]
        for direction in directions:
            for i in range(1, 8):
                move = self.position + i * direction
                if self.position % 8 == move % 8 or self.position // 8 == move // 8:
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