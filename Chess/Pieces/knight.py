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
            if move < 0 or move > 63:
                continue 
            pos_x, pos_y = divmod(self.position, 8)
            move_x, move_y = divmod(move, 8)
            if  abs(pos_x - move_x) + abs(pos_y - move_y) != 3:
                continue
            if board[move] is None:
                valid_moves.append(move)
            elif board[move].color != self.color:
                valid_moves.append(move) 
        return valid_moves 