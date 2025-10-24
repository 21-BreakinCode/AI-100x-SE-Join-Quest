from src.chess_product.piece import Piece


class Rook(Piece):
    """Rook (車) - moves any distance orthogonally without jumping"""

    def get_piece_type(self):
        return 'Rook'

    def is_valid_move(self, to_position, board):
        from_row, from_col = self.position
        to_row, to_col = to_position

        # Must move in straight line (horizontal or vertical)
        if from_row != to_row and from_col != to_col:
            return False

        # Path must be clear
        return board.is_path_clear(self.position, to_position)
