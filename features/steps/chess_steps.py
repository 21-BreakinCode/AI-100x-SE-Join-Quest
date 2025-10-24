from behave import given, when, then
from src.chess_product.board import Board
from src.chess_product.general import General
from src.chess_product.guard import Guard
from src.chess_product.rook import Rook
from src.chess_product.horse import Horse
from src.chess_product.cannon import Cannon
from src.chess_product.elephant import Elephant
from src.chess_product.soldier import Soldier
import re


def parse_position(pos_str):
    """Parse position string like '(1, 5)' into tuple (1, 5)"""
    match = re.match(r'\((\d+),\s*(\d+)\)', pos_str)
    if match:
        return (int(match.group(1)), int(match.group(2)))
    raise ValueError(f"Invalid position format: {pos_str}")


def create_piece(piece_name, color, position):
    """Factory method to create chess pieces"""
    piece_type = piece_name.split()[-1]  # Get last word (General, Guard, Rook, etc.)

    piece_map = {
        'General': General,
        'Guard': Guard,
        'Rook': Rook,
        'Horse': Horse,
        'Cannon': Cannon,
        'Elephant': Elephant,
        'Soldier': Soldier
    }

    piece_class = piece_map.get(piece_type)
    if piece_class:
        return piece_class(color, position)
    else:
        raise ValueError(f"Unknown piece type: {piece_type}")


@given('the board is empty except for a {color} {piece_type} at {position}')
def step_board_with_single_piece(context, color, piece_type, position):
    context.board = Board()
    pos = parse_position(position)
    piece = create_piece(piece_type, color, pos)
    context.board.place_piece(piece, pos)
    context.move_result = None


@given('the board has')
def step_board_with_multiple_pieces(context):
    context.board = Board()

    for row in context.table:
        piece_desc = row['Piece']  # e.g., "Red General"
        position = row['Position']

        # Parse piece description
        parts = piece_desc.split()
        color = parts[0]  # Red or Black
        piece_type = ' '.join(parts[1:])  # General, Guard, Rook, etc.

        pos = parse_position(position)
        piece = create_piece(piece_type, color, pos)
        context.board.place_piece(piece, pos)

    context.move_result = None


@when('{color} moves the {piece_type} from {from_pos} to {to_pos}')
def step_move_piece(context, color, piece_type, from_pos, to_pos):
    from_position = parse_position(from_pos)
    to_position = parse_position(to_pos)

    # Attempt the move
    context.move_result = context.board.move_piece(from_position, to_position)


@then('the move is legal')
def step_move_is_legal(context):
    assert context.move_result is True, \
        "Expected move to be legal, but it was illegal"


@then('the move is illegal')
def step_move_is_illegal(context):
    assert context.move_result is False, \
        "Expected move to be illegal, but it was legal"


@then('{color} wins immediately')
def step_player_wins(context, color):
    assert context.board.game_over is True, \
        "Expected game to be over, but it is not"
    assert context.board.winner == color, \
        f"Expected {color} to win, but winner is {context.board.winner}"


@then('the game is not over just from that capture')
def step_game_continues(context):
    assert context.board.game_over is False, \
        "Expected game to continue, but it is over"
