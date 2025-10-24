from src.chess_product.piece import Piece


class General(Piece):
    """General (將/帥) - can only move within palace, one step at a time"""

    def get_piece_type(self):
        return 'General'

    def is_valid_move(self, to_position, board):
        from_row, from_col = self.position
        to_row, to_col = to_position

        # Check if within palace
        if not self._is_in_palace(to_position):
            return False

        # Can only move one step orthogonally
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)

        if (row_diff == 1 and col_diff == 0) or (row_diff == 0 and col_diff == 1):
            # Check "Flying General" rule - Generals cannot face each other
            return not self._would_face_opponent_general(to_position, board)

        return False

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

    def _would_face_opponent_general(self, to_position, board):
        """Check if moving to this position would face the opponent's General"""
        to_row, to_col = to_position

        # Search along the column for opponent's General
        opponent_color = 'Black' if self.color == 'Red' else 'Red'

        for row in range(1, 11):
            if row == to_row:
                continue  # Skip our own position

            piece = board.get_piece((row, to_col))
            if piece:
                # If we hit any piece, check if it's opponent's General
                if piece.get_piece_type() == 'General' and piece.color == opponent_color:
                    # Check if there are any pieces between
                    if board.is_path_clear((to_row, to_col), (row, to_col)):
                        return True  # Would face opponent's General
                # If we hit any other piece, we're blocked
                break

        return False
