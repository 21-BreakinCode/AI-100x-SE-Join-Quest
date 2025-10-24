from src.chess_product.piece import Piece


class Horse(Piece):
    """Horse (馬/傌) - moves in "L" shape, can be blocked by adjacent piece"""

    def get_piece_type(self):
        return 'Horse'

    def is_valid_move(self, to_position, board):
        from_row, from_col = self.position
        to_row, to_col = to_position

        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)

        # Must move in "L" shape: 2 steps in one direction, 1 in another
        if not ((row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)):
            return False

        # Check for blocking piece ("hobbling the horse's leg")
        blocking_pos = self._get_blocking_position(self.position, to_position)
        if blocking_pos and board.get_piece(blocking_pos) is not None:
            return False

        return True

    def _get_blocking_position(self, from_pos, to_pos):
        """Get the position that would block the horse's movement"""
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        # Determine direction of movement
        if abs(to_row - from_row) == 2:
            # Moving 2 steps vertically, check adjacent vertical position
            blocking_row = from_row + (1 if to_row > from_row else -1)
            return (blocking_row, from_col)
        else:
            # Moving 2 steps horizontally, check adjacent horizontal position
            blocking_col = from_col + (1 if to_col > from_col else -1)
            return (from_row, blocking_col)
