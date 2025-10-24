class Board:
    """
    Chinese Chess Board (9 columns × 10 rows)
    Row 1-5: Red's territory, Row 6-10: Black's territory
    Palace: Red (1-3, 4-6), Black (8-10, 4-6)
    River: between row 5 and row 6
    """

    def __init__(self):
        # 10 rows × 9 columns grid
        self.grid = [[None for _ in range(9)] for _ in range(10)]
        self.game_over = False
        self.winner = None

    def place_piece(self, piece, position):
        """Place a piece at the given position"""
        row, col = position
        # Convert to 0-indexed
        self.grid[row - 1][col - 1] = piece
        piece.position = position

    def get_piece(self, position):
        """Get the piece at the given position"""
        row, col = position
        return self.grid[row - 1][col - 1]

    def remove_piece(self, position):
        """Remove piece from the given position"""
        row, col = position
        self.grid[row - 1][col - 1] = None

    def move_piece(self, from_pos, to_pos):
        """
        Move a piece from one position to another.

        Returns:
            bool: True if move was successful, False otherwise
        """
        piece = self.get_piece(from_pos)
        if not piece:
            return False

        # Check if move is valid
        if not piece.is_valid_move(to_pos, self):
            return False

        # Check for capturing
        target_piece = self.get_piece(to_pos)
        if target_piece:
            # Cannot capture own piece
            if target_piece.color == piece.color:
                return False

            # Check if capturing the General (winning condition)
            if target_piece.get_piece_type() == 'General':
                self.game_over = True
                self.winner = piece.color

        # Execute the move
        self.remove_piece(from_pos)
        self.place_piece(piece, to_pos)

        return True

    def is_path_clear(self, from_pos, to_pos):
        """Check if path between two positions is clear (for Rook, Cannon)"""
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        # Horizontal movement
        if from_row == to_row:
            step = 1 if to_col > from_col else -1
            for col in range(from_col + step, to_col, step):
                if self.get_piece((from_row, col)) is not None:
                    return False
            return True

        # Vertical movement
        if from_col == to_col:
            step = 1 if to_row > from_row else -1
            for row in range(from_row + step, to_row, step):
                if self.get_piece((row, from_col)) is not None:
                    return False
            return True

        return False

    def count_pieces_between(self, from_pos, to_pos):
        """Count pieces between two positions (for Cannon)"""
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        count = 0

        # Horizontal movement
        if from_row == to_row:
            step = 1 if to_col > from_col else -1
            for col in range(from_col + step, to_col, step):
                if self.get_piece((from_row, col)) is not None:
                    count += 1

        # Vertical movement
        elif from_col == to_col:
            step = 1 if to_row > from_row else -1
            for row in range(from_row + step, to_row, step):
                if self.get_piece((row, from_col)) is not None:
                    count += 1

        return count
