from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, color, position):
        """
        Initialize a chess piece.

        Args:
            color: 'Red' or 'Black'
            position: tuple (row, col) where row is 1-10, col is 1-9
        """
        self.color = color
        self.position = position

    @abstractmethod
    def is_valid_move(self, to_position, board):
        """
        Check if the move to the target position is valid.

        Args:
            to_position: tuple (row, col)
            board: Board object

        Returns:
            bool: True if move is valid, False otherwise
        """
        pass

    @abstractmethod
    def get_piece_type(self):
        """Return the piece type name"""
        pass
