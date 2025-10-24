from src.chess_product.piece import Piece


class Guard(Piece):
    """Guard (士/仕) - can only move diagonally within palace"""

    def get_piece_type(self):
        return 'Guard'

    def is_valid_move(self, to_position, board):
        from_row, from_col = self.position
        to_row, to_col = to_position

        # Check if within palace
        if not self._is_in_palace(to_position):
            return False

        # Must move exactly one step diagonally
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)

        return row_diff == 1 and col_diff == 1

    def _is_in_palace(self, position):
        """Check if position is within the palace"""
        row, col = position

        # Red palace: rows 1-3, cols 4-6
        if self.color == 'Red':
            return 1 <= row <= 3 and 4 <= col <= 6

        # Black palace: rows 8-10, cols 4-6
        if self.color == 'Black':
            return 8 <= row <= 10 and 4 <= col <= 6

        return False
