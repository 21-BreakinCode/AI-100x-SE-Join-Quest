from src.chess_product.piece import Piece


class Elephant(Piece):
    """Elephant (相/象) - moves exactly 2 steps diagonally, cannot cross river"""

    def get_piece_type(self):
        return 'Elephant'

    def is_valid_move(self, to_position, board):
        from_row, from_col = self.position
        to_row, to_col = to_position

        # Must move exactly 2 steps diagonally
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)

        if row_diff != 2 or col_diff != 2:
            return False

        # Cannot cross the river
        if not self._stays_on_own_side(to_position):
            return False

        # Check if midpoint is blocked ("blocking the elephant's eye")
        midpoint = self._get_midpoint(self.position, to_position)
        if board.get_piece(midpoint) is not None:
            return False

        return True

    def _stays_on_own_side(self, position):
        """Check if elephant stays on its own side of the river"""
        row, col = position

        # Red elephants: rows 1-5
        if self.color == 'Red':
            return 1 <= row <= 5

        # Black elephants: rows 6-10
        if self.color == 'Black':
            return 6 <= row <= 10

        return False

    def _get_midpoint(self, from_pos, to_pos):
        """Get the midpoint between two positions"""
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        mid_row = (from_row + to_row) // 2
        mid_col = (from_col + to_col) // 2

        return (mid_row, mid_col)
