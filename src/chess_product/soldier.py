from src.chess_product.piece import Piece


class Soldier(Piece):
    """Soldier/Pawn (兵/卒) - moves forward, can move sideways after crossing river"""

    def get_piece_type(self):
        return 'Soldier'

    def is_valid_move(self, to_position, board):
        from_row, from_col = self.position
        to_row, to_col = to_position

        row_diff = to_row - from_row
        col_diff = abs(to_col - from_col)

        # Check if soldier has crossed the river
        has_crossed = self._has_crossed_river()

        if self.color == 'Red':
            # Red moves forward (increasing row number)
            if row_diff == 1 and col_diff == 0:
                # Forward move (always allowed)
                return True
            elif has_crossed and row_diff == 0 and col_diff == 1:
                # Sideways move (only after crossing)
                return True
        else:  # Black
            # Black moves forward (decreasing row number)
            if row_diff == -1 and col_diff == 0:
                # Forward move (always allowed)
                return True
            elif has_crossed and row_diff == 0 and col_diff == 1:
                # Sideways move (only after crossing)
                return True

        return False

    def _has_crossed_river(self):
        """Check if soldier has crossed the river"""
        row, col = self.position

        # Red soldiers cross at row 6+
        if self.color == 'Red':
            return row >= 6

        # Black soldiers cross at row 5-
        if self.color == 'Black':
            return row <= 5

        return False
