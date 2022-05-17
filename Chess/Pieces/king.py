from Chess.Pieces.piece import Piece

class King(Piece):
    def __init__(self, color, position, value):
        self.value = value 
        self.color = color
        self.position = position
        self.piece = "k" if self.color == -1 else "K"

    def get_moves(self, board):
        valid_moves = []
        directions = [1, -1, 8, -8, 9, -9, 7, -7]
        for direction in directions:
            move = self.position + direction
            if (not self.is_same_diagonal(move, 1) and direction % 2 == 1) or move < 0:
                continue 
            if not (self.is_same_y or (direction != 1 or direction != -1)) and direction % 2 == 0:
                continue 
            if board[move] is None:
                valid_moves.append(move)
            elif board[move].color != self.color:
                valid_moves.append(move) 
        return valid_moves