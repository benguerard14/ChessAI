from Chess.Pieces.piece import Piece

class Knight(Piece):
    def __init__(self, color, position, value):
        self.value = value
        self.color = color
        self.position = position
        self.piece = "n" if self.color == -1 else "N"

    def get_moves(self, board):
        valid_moves = []
        directions = [15, 17, 10, 6, -6, -10, -17, -15] 
        for direction in directions:
            move = self.position + direction
            if (not self.is_same_diagonal(move, 1) and direction % 2 == 1) or move < 0 or move > 63:
                continue 
            if not (self.is_same_y or (direction != 1 or direction != -1)) and direction % 2 == 0:
                continue 
            if board[move] is None:
                valid_moves.append(move)
            elif board[move].color != self.color:
                valid_moves.append(move) 
        return valid_moves 