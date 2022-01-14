"""
Sprite Collect Coins with Background

Simple program to show basic sprite usage.


If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_collect_coins_background
"""

import arcade
import arcade.gui
import os
import piece
import board
import Black_player

PLAYER_SCALING = 0.75

WIDTH = 100
HEIGHT = 100

MARGIN = 5

ROW_COUNT = 8
COLUMN_COUNT = 8

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN

SCREEN_TITLE = "Chess"

GRID = board.Board.grid


class MyGameView(arcade.View):
    """
    Main application class.
    """

    def __init__(self):
        """ Initializer """
        super().__init__()

        self.enemy_list = None
        self.promoter = None
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.background = None

        self.player_list = None
        self.selected = None
        self.move_list = None
        self.white_king = None
        self.pre_check_spot = None
        self.checking_piece = None
        self.checking_path = None

        # Take me out later
        self.black_king = None

        self.black_player = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Load the background image. Do this in the setup so we don't keep reloading it all the time.
        # Image from: https://joszs.itch.io/chess-pack

        self.background = arcade.load_texture("Sprites/board.png")

        # Sprite lists
        self.player_list = arcade.SpriteList()

        self.promoter = PromoteView(self)
        self.checking_path = []

        # Pawns
        # self.score = 0
        for i in range(8):
            player_sprite = piece.Pawn(1, i, "Sprites/chess-pawn-white.png", 'white', 1)
            player_sprite.set_chess_position(GRID[player_sprite.get_chess_position()])
            board.Board.filled_spots[player_sprite.get_chess_position()] = player_sprite
            self.player_list.append(player_sprite)
            # self.white_legal_moves.append(
            # player_sprite.move_list(player_sprite.get_row(), player_sprite.get_column(), board.Board.filled_spots))

        # Rooks
        player_sprite = piece.Rook(0, 7, "Sprites/chess-rook-white.png", 'white', 4)
        player_sprite.set_chess_position(GRID[player_sprite.get_chess_position()])
        board.Board.filled_spots[player_sprite.get_chess_position()] = player_sprite
        self.player_list.append(player_sprite)
        # self.white_legal_moves.append(
        # player_sprite.move_list(player_sprite.get_row(), player_sprite.get_column(), board.Board.filled_spots))

        player_sprite = piece.Rook(0, 0, "Sprites/chess-rook-white.png", 'white', 4)
        player_sprite.set_chess_position(GRID[player_sprite.get_chess_position()])
        board.Board.filled_spots[player_sprite.get_chess_position()] = player_sprite
        self.player_list.append(player_sprite)
        # self.white_legal_moves.append(
        # player_sprite.move_list(player_sprite.get_row(), player_sprite.get_column(), board.Board.filled_spots))

        # Bishops
        player_sprite = piece.Bishop(0, 5, "Sprites/chess-bishop-white.png", 'white', 3)
        player_sprite.set_chess_position(GRID[player_sprite.get_chess_position()])
        board.Board.filled_spots[player_sprite.get_chess_position()] = player_sprite
        self.player_list.append(player_sprite)
        # self.white_legal_moves.append(
        # player_sprite.move_list(player_sprite.get_row(), player_sprite.get_column(), board.Board.filled_spots))

        player_sprite = piece.Bishop(0, 2, "Sprites/chess-bishop-white.png", 'white', 3)
        player_sprite.set_chess_position(GRID[player_sprite.get_chess_position()])
        board.Board.filled_spots[player_sprite.get_chess_position()] = player_sprite
        self.player_list.append(player_sprite)
        # self.white_legal_moves.append(
        # player_sprite.move_list(player_sprite.get_row(), player_sprite.get_column(), board.Board.filled_spots))

        # Knights
        player_sprite = piece.Knight(0, 1, "Sprites/chess-knight-white.png", 'white', 2)
        player_sprite.set_chess_position(GRID[player_sprite.get_chess_position()])
        board.Board.filled_spots[player_sprite.get_chess_position()] = player_sprite
        self.player_list.append(player_sprite)
        # self.white_legal_moves.append(
        # player_sprite.move_list(player_sprite.get_row(), player_sprite.get_column(), board.Board.filled_spots))

        player_sprite = piece.Knight(0, 6, "Sprites/chess-knight-white.png", 'white', 2)
        player_sprite.set_chess_position(GRID[player_sprite.get_chess_position()])
        board.Board.filled_spots[player_sprite.get_chess_position()] = player_sprite
        self.player_list.append(player_sprite)
        # self.white_legal_moves.append(
        # player_sprite.move_list(player_sprite.get_row(), player_sprite.get_column(), board.Board.filled_spots))

        # King
        player_sprite = piece.King(0, 4, "Sprites/chess-king-white.png", 'white', 8)
        player_sprite.set_chess_position(GRID[player_sprite.get_chess_position()])
        board.Board.filled_spots[player_sprite.get_chess_position()] = player_sprite
        self.player_list.append(player_sprite)
        self.white_king = player_sprite
        # self.white_legal_moves.append(
        # player_sprite.move_list(player_sprite.get_row(), player_sprite.get_column(), board.Board.filled_spots))

        # Queen
        player_sprite = piece.Queen(0, 3, "Sprites/chess-queen-white.png", 'white', 5)
        player_sprite.set_chess_position(GRID[player_sprite.get_chess_position()])
        board.Board.filled_spots[player_sprite.get_chess_position()] = player_sprite
        self.player_list.append(player_sprite)
        # self.white_legal_moves.append(
        # player_sprite.move_list(player_sprite.get_row(), player_sprite.get_column(), board.Board.filled_spots))

        # Black pieces
        # Move to different list later

        # Pawns
        for i in range(8):
            player_sprite = piece.Pawn(6, i, "Sprites/chess-pawn-black.png", "black", 1)
            player_sprite.set_chess_position(GRID[player_sprite.get_chess_position()])
            board.Board.filled_spots[player_sprite.get_chess_position()] = player_sprite
            self.player_list.append(player_sprite)
            # self.black_legal_moves.append(
            # player_sprite.move_list(player_sprite.get_row(), player_sprite.get_column(), board.Board.filled_spots))

        # Rooks
        player_sprite = piece.Rook(7, 7, "Sprites/chess-rook-black.png", 'black', 4)
        player_sprite.set_chess_position(GRID[player_sprite.get_chess_position()])
        board.Board.filled_spots[player_sprite.get_chess_position()] = player_sprite
        self.player_list.append(player_sprite)
        # self.white_legal_moves.append(
        # player_sprite.move_list(player_sprite.get_row(), player_sprite.get_column(), board.Board.filled_spots))

        player_sprite = piece.Rook(7, 0, "Sprites/chess-rook-black.png", 'black', 4)
        player_sprite.set_chess_position(GRID[player_sprite.get_chess_position()])
        board.Board.filled_spots[player_sprite.get_chess_position()] = player_sprite
        self.player_list.append(player_sprite)
        # self.white_legal_moves.append(
        # player_sprite.move_list(player_sprite.get_row(), player_sprite.get_column(), board.Board.filled_spots))

        # Bishops
        player_sprite = piece.Bishop(7, 5, "Sprites/chess-bishop-black.png", 'black', 3)
        player_sprite.set_chess_position(GRID[player_sprite.get_chess_position()])
        board.Board.filled_spots[player_sprite.get_chess_position()] = player_sprite
        self.player_list.append(player_sprite)
        # self.white_legal_moves.append(
        # player_sprite.move_list(player_sprite.get_row(), player_sprite.get_column(), board.Board.filled_spots))

        player_sprite = piece.Bishop(7, 2, "Sprites/chess-bishop-black.png", 'black', 3)
        player_sprite.set_chess_position(GRID[player_sprite.get_chess_position()])
        board.Board.filled_spots[player_sprite.get_chess_position()] = player_sprite
        self.player_list.append(player_sprite)
        # self.white_legal_moves.append(
        # player_sprite.move_list(player_sprite.get_row(), player_sprite.get_column(), board.Board.filled_spots))

        # Knights
        player_sprite = piece.Knight(7, 1, "Sprites/chess-knight-black.png", 'black', 2)
        player_sprite.set_chess_position(GRID[player_sprite.get_chess_position()])
        board.Board.filled_spots[player_sprite.get_chess_position()] = player_sprite
        self.player_list.append(player_sprite)
        # self.white_legal_moves.append(
        # player_sprite.move_list(player_sprite.get_row(), player_sprite.get_column(), board.Board.filled_spots))

        # Knights
        player_sprite = piece.Knight(7, 6, "Sprites/chess-knight-black.png", 'black', 2)
        player_sprite.set_chess_position(GRID[player_sprite.get_chess_position()])
        board.Board.filled_spots[player_sprite.get_chess_position()] = player_sprite
        self.player_list.append(player_sprite)
        # self.white_legal_moves.append(
        # player_sprite.move_list(player_sprite.get_row(), player_sprite.get_column(), board.Board.filled_spots))

        # King
        player_sprite = piece.King(7, 4, "Sprites/chess-king-black.png", 'black', 8)
        player_sprite.set_chess_position(GRID[player_sprite.get_chess_position()])
        board.Board.filled_spots[player_sprite.get_chess_position()] = player_sprite
        self.player_list.append(player_sprite)
        self.black_king = player_sprite
        # self.white_legal_moves.append(
        # player_sprite.move_list(player_sprite.get_row(), player_sprite.get_column(), board.Board.filled_spots))

        # Queen
        player_sprite = piece.Queen(7, 3, "Sprites/chess-queen-black.png", 'black', 5)
        player_sprite.set_chess_position(GRID[player_sprite.get_chess_position()])
        board.Board.filled_spots[player_sprite.get_chess_position()] = player_sprite
        self.player_list.append(player_sprite)
        # self.white_legal_moves.append(
        # player_sprite.move_list(player_sprite.get_row(), player_sprite.get_column(), board.Board.filled_spots))

        white_pieces = []
        black_pieces = []
        for x in self.player_list:
            if x.piece_color != 'white':
                black_pieces.append(x)
            else:
                white_pieces.append(x)
        self.black_player = Black_player.Player(black_pieces, white_pieces)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)

        # Draw all the sprites.
        # self.coin_list.draw()
        self.player_list.draw()
        # self.enemy_list.draw()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # column = int(x // (WIDTH + MARGIN))
        # row = int(y // (HEIGHT + MARGIN))
        square = (int(y // (HEIGHT + MARGIN)), int(x // (WIDTH + MARGIN)))
        print("Mouse down")
        for i in self.player_list:
            if i.get_chess_position() == square:
                self.selected = i
        self.pre_check_spot = (x, y)
        if self.selected:
            self.move_list = self.selected.move_list(int(y // (HEIGHT + MARGIN)), int(x // (WIDTH + MARGIN)),
                                                     board.Board.filled_spots)

    def move_piece(self, chess_piece, x, y, override=False):
        """Moves pieces by first checking for override, which is used when we need to move pieces in ways not
        determined by mouse position (Castling and reversing moves), then finds the selected piece's move set,
        and if the key spot where the player left the piece in is in the piece's move set, it is moved to that
        position. Lists are then updated to reflect the game state."""
        # After move, find piece new move set and if king in move set set king.check to true

        y_cord = int(y // (HEIGHT + MARGIN))
        x_cord = int(x // (WIDTH + MARGIN))
        if override:
            del board.Board.filled_spots[chess_piece.get_chess_position()]
            chess_piece.set_chess_position(GRID.get((int(y // (HEIGHT + MARGIN)), int(x // (WIDTH + MARGIN)))))
            chess_piece.MOVED = True
            chess_piece.set_row(int(y // (HEIGHT + MARGIN)))
            chess_piece.set_column(int(x // (WIDTH + MARGIN)))
            board.Board.filled_spots[chess_piece.get_chess_position()] = chess_piece
            # print(f"{type(chess_piece)} {chess_piece.taken_piece}")
            if type(chess_piece) is piece.King and chess_piece.taken_piece:
                board.Board.filled_spots[self.selected.taken_piece.get_chess_position()] = self.selected.taken_piece
                self.player_list.append(self.selected.taken_piece)

        elif (y_cord, x_cord) in self.move_list:
            del board.Board.filled_spots[chess_piece.get_chess_position()]
            if (y_cord, x_cord) in board.Board.filled_spots:
                if type(chess_piece) is piece.King:
                    chess_piece.taken_piece = board.Board.filled_spots[(y_cord, x_cord)]
                self.player_list.remove(
                    board.Board.filled_spots[(y_cord, x_cord)])
                del board.Board.filled_spots[(y_cord, x_cord)]
            # More castling logic
            if type(chess_piece) is piece.King and (y_cord, x_cord) == (0, 6) and chess_piece.MOVED is False:
                self.move_piece(board.Board.filled_spots[(0, 7)], 579, 66, True)
            if type(chess_piece) is piece.King and (y_cord, x_cord) == (0, 1) and chess_piece.MOVED is False:
                self.move_piece(board.Board.filled_spots[(0, 0)], 260, 60, True)

            chess_piece.set_chess_position(GRID.get((int(y // (HEIGHT + MARGIN)), int(x // (WIDTH + MARGIN)))))
            chess_piece.MOVED = True
            chess_piece.set_row(int(y // (HEIGHT + MARGIN)))
            chess_piece.set_column(int(x // (WIDTH + MARGIN)))
            board.Board.filled_spots[chess_piece.get_chess_position()] = chess_piece

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        """Ending step for human player moving a piece"""
        # All logic here works for white pieces
        if self.selected:
            if self.selected.piece_color == 'white':
                for i in list(self.black_king.danger_zone.keys()):
                    if i is self.selected:
                        del self.black_king.danger_zone[i]
            previous_spot = self.selected.get_chess_position()
            self.move_piece(self.selected, x, y)
            if previous_spot == self.selected.get_chess_position():
                print("Please try again")
                return

            if type(self.selected) is piece.Pawn and (self.selected.get_row() == 0 or self.selected.get_row() == 7):
                self.promote(self.selected)
                del self.selected

            for i in self.black_king.move_list(self.black_king.get_row(), self.black_king.get_column(),
                                               board.Board.filled_spots):
                if i in self.selected.move_list(self.selected.get_row(), self.selected.get_column(),
                                                board.Board.filled_spots):
                    self.black_king.danger_zone[self.selected] = i

            queens_left = False
            rooks_left = False
            bishops_left = False
            pawns_left = False
            knights_left = False
            for i in range(len(self.player_list)):
                curr_piece = type(self.player_list[i])
                if self.player_list[i].piece_color == 'white':
                    if pawns_left is False and curr_piece is piece.Pawn:
                        pawns_left = True
                    if queens_left is False and curr_piece is piece.Queen:
                        queens_left = True
                    if rooks_left is False and curr_piece is piece.Rook:
                        rooks_left = True
                    if bishops_left is False and curr_piece is piece.Bishop:
                        bishops_left = True
                    if knights_left is False and curr_piece is piece.Knight:
                        knights_left = True

            self.check_for_check(self.black_king, board.Board.filled_spots, queens_left, rooks_left, bishops_left,
                                 pawns_left, knights_left)
            if self.black_king.IN_CHECK:
                print("Black In Check")
                self.check_for_checkMate(self.black_king, board.Board.filled_spots, queens_left, rooks_left,
                                         bishops_left,
                                         pawns_left, knights_left)
            queens_left = False
            rooks_left = False
            bishops_left = False
            pawns_left = False
            knights_left = False
            for i in range(len(self.player_list)):
                curr_piece = type(self.player_list[i])
                if self.player_list[i].piece_color == 'black':
                    if pawns_left is False and curr_piece is piece.Pawn:
                        pawns_left = True
                    if queens_left is False and curr_piece is piece.Queen:
                        queens_left = True
                    if rooks_left is False and curr_piece is piece.Rook:
                        rooks_left = True
                    if bishops_left is False and curr_piece is piece.Bishop:
                        bishops_left = True
                    if knights_left is False and curr_piece is piece.Knight:
                        knights_left = True

            self.check_for_check(self.white_king, board.Board.filled_spots, queens_left, rooks_left, bishops_left,
                                 pawns_left, knights_left)
            if self.white_king.IN_CHECK:
                print("You cannot put your own king in Check")
                self.white_king.danger_zone[self.checking_piece] = self.white_king.get_chess_position()
                self.move_piece(self.selected, self.pre_check_spot[0], self.pre_check_spot[1], True)
                return
            # BlackMove
            self.black_player.sync_with_list(self.player_list)
            self.black_player.find_move(self.player_list)
            self.black_player.sync_with_list(self.player_list)

            self.check_for_check(self.white_king, board.Board.filled_spots, queens_left, rooks_left, bishops_left,
                                 pawns_left, knights_left)
            if self.white_king.IN_CHECK:
                if self.check_for_checkMate(self.white_king, board.Board.filled_spots, queens_left, rooks_left,
                                            bishops_left,
                                            pawns_left, knights_left):
                    print("CheckMate")
                else:
                    print("Check")
            if self.white_king.taken_piece:
                self.white_king.taken_piece = None

    def check_for_checkMate(self, king, positions, queens_left, rooks_left, bishops_left, pawns_left, knight_left):
        """Method for determining a winner."""
        checkMate = True

        # If king can move away First confirm danger zone. For each piece in danger zone, confirm that the spot is
        # still in the move list of the threatening piece
        if king.move_list(king.get_row(), king.get_column(), positions):
            checkMate = False
            return checkMate

        # If checking piece can be taken
        self.check_for_check(self.checking_piece, positions, queens_left, rooks_left, bishops_left, pawns_left,
                             knight_left)
        if self.checking_piece.IN_CHECK:
            checkMate = False
            return checkMate

        for x in self.checking_path:
            for i in self.player_list:
                if i.piece_color == 'white' and x in self.move_list:
                    checkMate = False
                    return checkMate
        return checkMate

    def check_for_check(self, king, positions, queens_left, rooks_left, bishops_left, pawns_left, knight_left):
        """Method for determining if a piece can be taken by the enemy.
        Works by scanning each possible spot around the piece that a piece could check it from"""

        # If an opponent has no pieces left of a certain type, skip that section
        king.IN_CHECK = False

        # White Pawns
        if pawns_left:
            if (king.get_row() - 1, king.get_column() - 1) in positions.keys():
                if positions[(king.get_row() - 1, king.get_column() - 1)].piece_color != king.piece_color and \
                        type(positions[(king.get_row() - 1, king.get_column() - 1)]) is piece.Pawn:
                    if type(king) is piece.King:
                        self.checking_piece = positions[(king.get_row() - 1, king.get_column() - 1)]
                    king.IN_CHECK = True
                    return
            if (king.get_row() - 1, king.get_column() + 1) in positions.keys():
                if positions[(king.get_row() - 1, king.get_column() + 1)].piece_color != king.piece_color and \
                        type(positions[(king.get_row() - 1, king.get_column() + 1)]) is piece.Pawn:
                    if type(king) is piece.King:
                        self.checking_piece = positions[(king.get_row() - 1, king.get_column() + 1)]
                    king.IN_CHECK = True
                    return
            # Black Pawns
            if (king.get_row() + 1, king.get_column() - 1) in positions.keys():
                if positions[(king.get_row() + 1, king.get_column() - 1)].piece_color != king.piece_color and \
                        type(positions[(king.get_row() + 1, king.get_column() - 1)]) is piece.Pawn:
                    if type(king) is piece.King:
                        self.checking_piece = positions[(king.get_row() + 1, king.get_column() - 1)]
                    king.IN_CHECK = True
                    return
            if (king.get_row() + 1, king.get_column() + 1) in positions.keys():
                if positions[(king.get_row() + 1, king.get_column() + 1)].piece_color != king.piece_color and \
                        type(positions[(king.get_row() + 1, king.get_column() + 1)]) is piece.Pawn:
                    if type(king) is piece.King:
                        self.checking_piece = positions[(king.get_row() + 1, king.get_column() + 1)]
                    king.IN_CHECK = True
                    return

        # Knights
        if knight_left:
            if (king.get_row() - 2, king.get_column() - 1) in positions.keys():
                if positions[(king.get_row() - 2, king.get_column() - 1)].piece_color != king.piece_color and type(
                        positions[(king.get_row() - 2, king.get_column() - 1)]) is piece.Knight:
                    if type(king) is piece.King:
                        self.checking_piece = positions[(king.get_row() - 2, king.get_column() - 1)]
                    king.IN_CHECK = True
                    return

            if (king.get_row() - 2, king.get_column() + 1) in positions.keys():
                if positions[(king.get_row() - 2, king.get_column() + 1)].piece_color != king.piece_color and type(
                        positions[(king.get_row() - 2, king.get_column() + 1)]) is piece.Knight:
                    if type(king) is piece.King:
                        self.checking_piece = positions[(king.get_row() - 2, king.get_column() + 1)]
                    king.IN_CHECK = True
                    return

            if (king.get_row() + 2, king.get_column() + 1) in positions.keys():
                if positions[(king.get_row() + 2, king.get_column() + 1)].piece_color != king.piece_color and type(
                        positions[(king.get_row() + 2, king.get_column() + 1)]) is piece.Knight:
                    if type(king) is piece.King:
                        self.checking_piece = positions[(king.get_row() + 2, king.get_column() + 1)]
                    king.IN_CHECK = True
                    return

            if (king.get_row() + 2, king.get_column() - 1) in positions.keys():
                if positions[(king.get_row() + 2, king.get_column() - 1)].piece_color != king.piece_color and type(
                        positions[(king.get_row() + 2, king.get_column() - 1)]) is piece.Knight:
                    if type(king) is piece.King:
                        self.checking_piece = positions[(king.get_row() + 2, king.get_column() - 1)]
                    king.IN_CHECK = True
                    return

            if (king.get_row() - 1, king.get_column() + 2) in positions.keys():
                if positions[(king.get_row() - 1, king.get_column() + 2)].piece_color != king.piece_color and type(
                        positions[(king.get_row() - 1, king.get_column() + 2)]) is piece.Knight:
                    if type(king) is piece.King:
                        self.checking_piece = positions[(king.get_row() - 1, king.get_column() + 2)]
                    king.IN_CHECK = True
                    return

            if (king.get_row() - 1, king.get_column() - 2) in positions.keys():
                if positions[(king.get_row() - 1, king.get_column() - 2)].piece_color != king.piece_color and type(
                        positions[(king.get_row() - 1, king.get_column() - 2)]) is piece.Knight:
                    if type(king) is piece.King:
                        self.checking_piece = positions[(king.get_row() - 1, king.get_column() - 2)]
                    king.IN_CHECK = True
                    return

            if (king.get_row() + 1, king.get_column() - 2) in positions.keys():
                if positions[(king.get_row() + 1, king.get_column() - 2)].piece_color != king.piece_color and type(
                        positions[(king.get_row() + 1, king.get_column() - 2)]) is piece.Knight:
                    if type(king) is piece.King:
                        self.checking_piece = positions[(king.get_row() + 1, king.get_column() - 2)]
                    king.IN_CHECK = True
                    return

            if (king.get_row() + 1, king.get_column() + 2) in positions.keys():
                if positions[(king.get_row() + 1, king.get_column() + 2)].piece_color != king.piece_color and type(
                        positions[(king.get_row() + 1, king.get_column() + 2)]) is piece.Knight:
                    if type(king) is piece.King:
                        self.checking_piece = positions[(king.get_row() + 1, king.get_column() + 2)]
                    king.IN_CHECK = True
                    return

        # Rooks and queens
        if rooks_left or queens_left:
            for i in range(7):
                # North
                if (king.get_row() + 1 + i, king.get_column()) in positions.keys():
                    self.checking_path.append((king.get_row() + 1 + i, king.get_column()))
                    if positions[(king.get_row() + 1 + i, king.get_column())].piece_color == king.piece_color:
                        break
                    elif not (
                            type(
                                positions[(king.get_row() + 1 + i, king.get_column())]) is piece.Rook or type(
                        positions[(king.get_row() + 1 + i, king.get_column())]) is piece.Queen):
                        break
                    else:
                        if type(king) is piece.King:
                            self.checking_piece = positions[(king.get_row() + 1 + i, king.get_column())]
                        king.IN_CHECK = True
                        return
            self.checking_path.clear()
            for i in range(7):
                if (king.get_row(), king.get_column() + 1 + i) in positions.keys():
                    self.checking_path.append((king.get_row(), king.get_column() + 1 + i))
                    if positions[(king.get_row(), king.get_column() + 1 + i)].piece_color == king.piece_color:
                        break
                    elif not (
                            type(
                                positions[(king.get_row(), king.get_column() + 1 + i)]) is piece.Rook or type(
                        positions[(king.get_row(), king.get_column() + 1 + i)]) is piece.Queen):
                        break
                    else:
                        if type(king) is piece.King:
                            self.checking_piece = positions[(king.get_row(), king.get_column() + 1 + i)]
                        king.IN_CHECK = True
                        return

            self.checking_path.clear()
            for i in range(7):
                if (king.get_row() - 1 - i, king.get_column()) in positions.keys():
                    self.checking_path.append((king.get_row() - 1 - i, king.get_column()))
                    if positions[(king.get_row() - 1 - i, king.get_column())].piece_color == king.piece_color:
                        break
                    elif not (
                            type(
                                positions[(king.get_row() - 1 - i, king.get_column())]) is piece.Rook or type(
                        positions[(king.get_row() - 1 - i, king.get_column())]) is piece.Queen):
                        break
                    else:
                        if type(king) is piece.King:
                            self.checking_piece = positions[(king.get_row() - 1 - i, king.get_column())]
                        king.IN_CHECK = True
                        return

            self.checking_path.clear()
            for i in range(7):
                if (king.get_row(), king.get_column() - 1 - i) in positions.keys():
                    if positions[(king.get_row(), king.get_column() - 1 - i)].piece_color == king.piece_color:
                        break
                    elif not (
                            type(
                                positions[(king.get_row(), king.get_column() - 1 - i)]) is piece.Rook or type(
                        positions[(king.get_row(), king.get_column() - 1 - i)]) is piece.Queen):
                        break
                    else:
                        if type(king) is piece.King:
                            self.checking_piece = positions[(king.get_row(), king.get_column() - 1 - i)]
                        king.IN_CHECK = True
                        return
                else:
                    self.checking_path.append((king.get_row(), king.get_column() - 1 - i))

        # Bishops and queens
        self.checking_path.clear()
        if bishops_left or queens_left:
            for i in range(7):
                # North
                if (king.get_row() + 1 + i, king.get_column() + 1 + i) in positions.keys():
                    if positions[(king.get_row() + 1 + i, king.get_column() + 1 + i)].piece_color == king.piece_color:
                        break
                    elif not (
                            type(
                                positions[(king.get_row() + 1 + i, king.get_column() + 1 + i)]) is piece.Bishop or type(
                        positions[(king.get_row() + 1 + i, king.get_column() + 1 + i)]) is piece.Queen):
                        break
                    else:
                        if type(king) is piece.King:
                            self.checking_piece = positions[(king.get_row() + 1 + i, king.get_column() + 1 + i)]
                        king.IN_CHECK = True
                        return
                else:
                    self.checking_path.append((king.get_row() + 1 + i, king.get_column() + 1 + i))
            self.checking_path.clear()
            for i in range(7):
                if (king.get_row() + 1 + i, king.get_column() - 1 - i) in positions.keys():
                    if positions[(king.get_row() + 1 + i, king.get_column() - 1 - i)].piece_color == king.piece_color:
                        break
                    elif not (
                            type(
                                positions[(king.get_row() + 1 + i, king.get_column() - 1 - i)]) is piece.Bishop or type(
                        positions[(king.get_row() + 1 + i, king.get_column() - 1 - i)]) is piece.Queen):
                        break
                    else:
                        if type(king) is piece.King:
                            self.checking_piece = positions[(king.get_row() + 1 + i, king.get_column() - 1 - i)]
                        king.IN_CHECK = True
                        return
                else:
                    self.checking_path.append((king.get_row() + 1 + i, king.get_column() - 1 - i))
                    # """if type(positions[(king.get_row() + 1 + i, king.get_column() - 1 - i)]) is piece.Bishop or
                    # type( positions[(king.get_row() + 1 + i, king.get_column() - 1 - i)]) is piece.Queen:"""
            self.checking_path.clear()
            for i in range(7):
                if (king.get_row() - 1 - i, king.get_column() - 1 - i) in positions.keys():
                    if positions[(king.get_row() - 1 - i, king.get_column() - 1 - i)].piece_color == king.piece_color:
                        break
                    elif not (
                            type(
                                positions[(king.get_row() - 1 - i, king.get_column() - 1 - i)]) is piece.Bishop or type(
                        positions[(king.get_row() - 1 + i, king.get_column() - 1 - i)]) is piece.Queen):
                        break
                    else:
                        if type(king) is piece.King:
                            self.checking_piece = positions[(king.get_row() - 1 - i, king.get_column() - 1 - i)]
                        king.IN_CHECK = True
                        return
                else:
                    self.checking_path.append((king.get_row() - 1 - i, king.get_column() - 1 - i))

            self.checking_path.clear()
            for i in range(7):
                if (king.get_row() - 1 - i, king.get_column() + 1 + i) in positions.keys():
                    if positions[(king.get_row() - 1 - i, king.get_column() + 1 + i)].piece_color == king.piece_color:
                        break
                    elif not (
                            type(
                                positions[(king.get_row() - 1 - i, king.get_column() + 1 + i)]) is piece.Bishop or type(
                        positions[(king.get_row() - 1 - i, king.get_column() + 1 + i)]) is piece.Queen):
                        break
                    else:
                        if type(king) is piece.King:
                            self.checking_piece = positions[(king.get_row() - 1 - i, king.get_column() + 1 + i)]
                        king.IN_CHECK = True
                        return
                else:
                    self.checking_path.append((king.get_row() - 1 - i, king.get_column() + 1 + i))

        self.checking_path.clear()
        if type(king) is not piece.King:
            if (king.get_row() + 1, king.get_column()) in positions.keys():
                if positions[(king.get_row() + 1, king.get_column())].piece_color != king.piece_color and type(
                        positions[(king.get_row() + 1, king.get_column())]) is piece.King:
                    king.IN_CHECK = True
                    return

            if (king.get_row() + 1, king.get_column() + 1) in positions.keys():
                if positions[(king.get_row() + 1, king.get_column() + 1)].piece_color != king.piece_color and type(
                        positions[(king.get_row() + 1, king.get_column() + 1)]) is piece.King:
                    king.IN_CHECK = True
                    return

            if (king.get_row(), king.get_column() + 1) in positions.keys():
                if positions[(king.get_row(), king.get_column() + 1)].piece_color != king.piece_color and type(
                        positions[(king.get_row(), king.get_column() + 1)]) is piece.King:
                    king.IN_CHECK = True
                    return

            #
            if (king.get_row() - 1, king.get_column() + 1) in positions.keys():
                if positions[(king.get_row() - 1, king.get_column() + 1)].piece_color != king.piece_color and type(
                        positions[(king.get_row() - 1, king.get_column() + 1)]) is piece.King:
                    king.IN_CHECK = True
                    return

            if (king.get_row() + 1, king.get_column() - 1) in positions.keys():
                if positions[(king.get_row() + 1, king.get_column() - 1)].piece_color != king.piece_color and type(
                        positions[(king.get_row() + 1, king.get_column() - 1)]) is piece.King:
                    king.IN_CHECK = True
                    return

            if (king.get_row() - 1, king.get_column()) in positions.keys():
                if positions[(king.get_row(), king.get_column() + 1)].piece_color != king.piece_color and type(
                        positions[(king.get_row(), king.get_column() + 1)]) is piece.King:
                    king.IN_CHECK = True
                    return

            if (king.get_row() - 1, king.get_column() - 1) in positions.keys():
                if positions[(king.get_row() - 1, king.get_column() - 1)].piece_color != king.piece_color and type(
                        positions[(king.get_row() - 1, king.get_column() - 1)]) is piece.King:
                    king.IN_CHECK = True
                    return

    def promote(self, call_piece):
        self.promoter.set_piece(call_piece)
        self.promoter.set_new_view(self)
        self.window.show_view(self.promoter)


class PromoteView(arcade.View):
    """Shown when the pawn needs to be promoted"""

    def __init__(self, game_view: arcade.View) -> None:
        # Initialize the parent
        super().__init__()
        self.call_piece = None

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Store a reference to the underlying view
        self.game_view = game_view

        # Store a semitransparent color to use as an overlay
        self.fill_color = arcade.make_transparent_color(
            arcade.color.WHITE, transparency=150
        )

        self.v_box = arcade.gui.UIBoxLayout()
        queen_button = arcade.gui.UIFlatButton(text="Promote To Queen", width=200)
        self.v_box.add(queen_button.with_space_around(bottom=20))

        knight_button = arcade.gui.UIFlatButton(text="Promote To Knight", width=200)
        self.v_box.add(knight_button.with_space_around(bottom=20))

        rook_button = arcade.gui.UIFlatButton(text="Promote To Rook", width=200)
        self.v_box.add(rook_button.with_space_around(bottom=20))

        bishop_button = arcade.gui.UIFlatButton(text="Promote To Bishop", width=200)
        self.v_box.add(bishop_button.with_space_around(bottom=20))

        @queen_button.event("on_click")
        def on_click_settings(event):
            game_view.player_list.remove(self.call_piece)
            new_piece = piece.Queen(self.call_piece.get_row(), self.call_piece.get_column(),
                                    "Sprites/chess-queen-white.png", self.call_piece.piece_color, 5)
            new_piece.set_chess_position(GRID[new_piece.get_chess_position()])
            game_view.player_list.append(new_piece)
            board.Board.filled_spots[self.call_piece.get_chess_position()] = new_piece
            self.window.show_view(game_view)

        @knight_button.event("on_click")
        def on_click_settings(event):
            game_view.player_list.remove(self.call_piece)
            new_piece = piece.Knight(self.call_piece.get_row(), self.call_piece.get_column(),
                                     "Sprites/chess-knight-white.png",
                                     self.call_piece.piece_color, 5)
            new_piece.set_chess_position(GRID[new_piece.get_chess_position()])
            game_view.player_list.append(new_piece)
            board.Board.filled_spots[self.call_piece.get_chess_position()] = new_piece
            self.window.show_view(game_view)

        @rook_button.event("on_click")
        def on_click_settings(event):
            game_view.player_list.remove(self.call_piece)
            new_piece = piece.Rook(self.call_piece.get_row(), self.call_piece.get_column(),
                                   "Sprites/chess-Rook-white.png",
                                   self.call_piece.piece_color, 5)
            new_piece.set_chess_position(GRID[new_piece.get_chess_position()])
            game_view.player_list.append(new_piece)
            board.Board.filled_spots[self.call_piece.get_chess_position()] = new_piece
            self.window.show_view(game_view)

        @bishop_button.event("on_click")
        def on_click_settings(event):
            game_view.player_list.remove(self.call_piece)
            new_piece = piece.Bishop(self.call_piece.get_row(), self.call_piece.get_column(),
                                     "Sprites/chess-Bishop-white.png",
                                     self.call_piece.piece_color, 5)
            new_piece.set_chess_position(GRID[new_piece.get_chess_position()])
            game_view.player_list.append(new_piece)
            board.Board.filled_spots[self.call_piece.get_chess_position()] = new_piece
            self.window.show_view(game_view)

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_draw(self) -> None:
        """Draw the underlying screen, blurred, then the Paused text"""

        # First, draw the underlying view
        # This also calls start_render(), so no need to do it again
        self.game_view.on_draw()

        # Now create a filled rect that covers the current viewport
        # We get the viewport size from the game view
        arcade.draw_lrtb_rectangle_filled(
            left=0,
            right=SCREEN_WIDTH,
            top=SCREEN_HEIGHT,
            bottom=0,
            color=self.fill_color,
        )
        self.manager.draw()

    def set_piece(self, this_piece):
        self.call_piece = this_piece

    def set_new_view(self, new_view):
        self.game_view = new_view


def main():
    """ Main function """

    window = arcade.Window(
        width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE
    )
    platform_view = MyGameView()
    platform_view.setup()
    window.show_view(platform_view)
    arcade.run()


if __name__ == "__main__":
    main()
