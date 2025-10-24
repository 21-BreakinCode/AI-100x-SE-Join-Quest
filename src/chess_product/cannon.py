from src.chess_product.piece import Piece


class Cannon(Piece):
    """Cannon (炮) - moves like Rook, but needs exactly one piece to jump when capturing"""

    def get_piece_type(self):
        return 'Cannon'

    def is_valid_move(self, to_position, board):
        from_row, from_col = self.position
        to_row, to_col = to_position

        # Must move in straight line (horizontal or vertical)
        if from_row != to_row and from_col != to_col:
            return False

        target_piece = board.get_piece(to_position)
        pieces_between = board.count_pieces_between(self.position, to_position)

        if target_piece:
            # Capturing: need exactly one piece to jump over (screen)
            return pieces_between == 1
        else:
            # Non-capturing: path must be clear (no pieces between)
            return pieces_between == 0
