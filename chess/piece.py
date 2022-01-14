import arcade


class Piece(arcade.Sprite):
    """Base class for all pieces"""
    CHECK_GUARDING = False
    IN_CHECK = False

    def __init__(self, row, column, image, piece_color, point_value):
        super().__init__(image, scale=0.3)
        self.row = row
        self.column = column
        self.piece_color = piece_color
        self.point_value = point_value


    def __str__(self):
        return f'{self.piece_color} {type(self)} at {self.get_chess_position()}'

    def get_column(self):
        return self.column

    def get_row(self):
        return self.row

    def get_point_value(self):
        return self.point_value

    def set_row(self, new_row):
        self.row = new_row

    def set_column(self, new_column):
        self.column = new_column

    def get_chess_position(self):
        pos = (self.row, self.column)
        return pos

    def set_chess_position(self, position):
        self.center_x = position[0]
        self.center_y = position[1]

    def get_takeable_pieces(self, move_list, positions):
        for x in move_list:
            if x in positions.keys() and positions[x].piece_color != self.piece_color:
                self.takeable_pieces.append(positions[x])


class Pawn(Piece):
    MOVED = False

    def __init__(self, row, column, image, piece_color, point_value):
        super().__init__(row, column, image, piece_color, point_value)

    def move_list(self, row, column, positions):
        moves = []
        if self.piece_color == 'white':

            if not self.MOVED:
                if (row + 1, column) not in positions.keys():
                    moves.append((row + 1, column))
                if (row + 2, column) not in positions.keys():
                    moves.append((row + 2, column))
                # moves = [(row + 1, column), (row + 2, column)]
            else:
                if (row + 1, column) not in positions.keys():
                    moves.append((row + 1, column))

            if (row + 1, column - 1) in positions.keys():
                if positions[(row + 1, column - 1)].piece_color != self.piece_color:
                    moves.append((row + 1, column - 1))
            if (row + 1, column + 1) in positions.keys():
                if positions[(row + 1, column + 1)].piece_color != self.piece_color:
                    moves.append((row + 1, column + 1))
        else:
            if not self.MOVED:
                if (row - 1, column) not in positions.keys():
                    moves.append((row - 1, column))
                if (row - 2, column) not in positions.keys():
                    moves.append((row - 2, column))
                    # moves = [(row + 1, column), (row + 2, column)]
            else:
                if (row - 1, column) not in positions.keys():
                    moves.append((row - 1, column))
            # logic for taking pieces
            if (row - 1, column - 1) in positions.keys():
                if positions[(row - 1, column - 1)].piece_color != self.piece_color:
                    moves.append((row - 1, column - 1))
            if (row - 1, column + 1) in positions.keys():
                if positions[(row - 1, column + 1)].piece_color != self.piece_color:
                    moves.append((row - 1, column + 1))
        return moves


class Rook(Piece):
    def __init__(self, row, column, image, piece_color, point_value):
        super().__init__(row, column, image, piece_color, point_value)

    MOVED = False

    def move_list(self, row, column, positions):
        moves = []
        for i in range(7):
            if (row + 1 + i, column) in positions.keys():
                if positions[(row + 1 + i, column)].piece_color == self.piece_color:
                    break
                else:
                    # print("Hi")
                    moves.append((row + 1 + i, column))
                    break
            else:
                if row + 1 + i < 8:
                    moves.append((row + 1 + i, column))

        for i in range(7):
            if (row, column + 1 + i) in positions.keys():
                if positions[(row, column + 1 + i)].piece_color == self.piece_color:
                    break
                else:
                    moves.append((row, column + 1 + i))
                    break
            else:
                if column + 1 + i < 8:
                    moves.append((row, column + 1 + i))

        for i in range(7):
            if (row - 1 - i, column) in positions.keys():
                if positions[(row - 1 - i, column)].piece_color == self.piece_color:
                    break
                else:
                    moves.append((row - 1 - i, column))
                    break
            else:
                if row - 1 - i > -1:
                    moves.append((row - 1 - i, column))

        for i in range(7):
            if (row, column - 1 - i) in positions.keys():
                if positions[(row, column - 1 - i)].piece_color == self.piece_color:
                    break
                else:
                    moves.append((row, column - 1 - i))
                    break
            else:
                if column - 1 - i > -1:
                    moves.append((row, column - 1 - i))
        return moves


class Bishop(Piece):
    def __init__(self, row, column, image, piece_color, point_value):
        super().__init__(row, column, image, piece_color, point_value)

    def move_list(self, row, column, positions):
        moves = []
        for i in range(7):
            if (row + 1 + i, column + 1 + i) in positions.keys():
                if positions[(row + 1 + i, column + 1 + i)].piece_color != self.piece_color:
                    moves.append((row + 1 + i, column + i + 1))
                    break
                else:
                    break
            else:
                if column + i + 1 < 8 and row + i + 1 < 8:
                    moves.append((row + 1 + i, column + i + 1))

        for i in range(7):
            if (row + 1 + i, column - 1 - i) in positions.keys():
                if positions[(row + 1 + i, column - 1 - i)].piece_color != self.piece_color:
                    moves.append((row + 1 + i, column - i - 1))
                    break
                else:
                    break
            else:
                if column - i - 1 > -1 and row + i + 1 < 8:
                    moves.append((row + 1 + i, column - i - 1))

        for i in range(7):
            if (row - 1 - i, column - 1 - i) in positions.keys():
                if positions[(row - 1 - i, column - 1 - i)].piece_color != self.piece_color:
                    moves.append((row - 1 - i, column - i - 1))
                    break
                else:
                    break
            else:
                if column - i - 1 > -1 and row - i - 1 > -1:
                    moves.append((row - 1 - i, column - i - 1))

        for i in range(7):
            if (row - 1 - i, column + 1 + i) in positions.keys():
                if positions[(row - 1 - i, column + 1 + i)].piece_color != self.piece_color:
                    moves.append((row - 1 - i, column + i + 1))
                    break
                else:
                    break
            else:
                if column + i + 1 < 8 and row - i - 1 > -1:
                    moves.append((row - 1 - i, column + i + 1))
        return moves


class Knight(Piece):
    def __init__(self, row, column, image, piece_color, point_value):
        super().__init__(row, column, image, piece_color, point_value)

    def move_list(self, row, column, positions):
        moves = []
        if (row + 2, column + 1) in positions:
            if positions[(row + 2, column + 1)].piece_color != self.piece_color and row + 2 < 8 and column + 1 < 8:
                moves.append((row + 2, column + 1))
        else:
            if row + 2 < 8 and column + 1 < 8:
                moves.append((row + 2, column + 1))

        if (row + 2, column - 1) in positions:
            if positions[(row + 2, column - 1)].piece_color != self.piece_color and row + 2 < 8 and column - 1 > -1:
                moves.append((row + 2, column - 1))
        else:
            if row + 2 < 8 and column - 1 > -1:
                moves.append((row + 2, column - 1))

        if (row - 2, column - 1) in positions:
            if positions[(row - 2, column - 1)].piece_color != self.piece_color and row - 2 > -1 and column - 1 > -1:
                moves.append((row - 2, column - 1))
        else:
            if row - 2 > -1 and column - 1 > -1:
                moves.append((row - 2, column - 1))

        if (row - 2, column + 1) in positions:
            if positions[(row - 2, column + 1)].piece_color != self.piece_color and row - 2 > -1 and column + 1 < 8:
                moves.append((row - 2, column + 1))
        else:
            if row - 2 > -1 and column + 1 < 8:
                moves.append((row - 2, column + 1))

        if (row + 1, column + 2) in positions:
            if positions[(row + 1, column + 2)].piece_color != self.piece_color and row + 1 < 8 and column + 2 < 8:
                moves.append((row + 1, column + 2))
        else:
            if row + 1 < 8 and column + 2 < 8:
                moves.append((row + 1, column + 2))

        if (row - 1, column + 2) in positions:
            if positions[(row - 1, column + 2)].piece_color != self.piece_color and row - 1 > -1 and column + 2 < 8:
                moves.append((row - 1, column + 2))
        else:
            if row - 1 > -1 and column + 2 < 8:
                moves.append((row - 1, column + 2))

        if (row + 1, column - 2) in positions:
            if positions[(row + 1, column - 2)].piece_color != self.piece_color and row + 1 < 8 and column - 2 > -1:
                moves.append((row + 1, column - 2))
        else:
            if row + 1 < 8 and column - 2 > -1:
                moves.append((row + 1, column - 2))

        if (row - 1, column - 2) in positions:
            if positions[(row - 1, column - 2)].piece_color != self.piece_color and row - 1 > -1 and column - 2 > -1:
                moves.append((row - 1, column - 2))
        else:
            if row - 1 > -1 and column - 2 > -1:
                moves.append((row - 1, column - 2))

        return moves


class King(Piece):
    def __init__(self, row, column, image, piece_color, point_value):
        super().__init__(row, column, image, piece_color, point_value)
        self.danger_zone = {}
        self.taken_piece = None
    MOVED = False

    def confirm_danger(self, positions):
        #print(str(self.danger_zone))
        for x in list(self.danger_zone.keys()):
            if self.danger_zone[x] not in x.move_list(x.get_row(), x.get_column(), positions):
                del self.danger_zone[x]
        #print(str(self.danger_zone))

    def move_list(self, row, column, positions):
        self.confirm_danger(positions)
        #self.taken_piece = None
        moves = []
        if (row + 1, column) in positions and (row + 1, column) not in self.danger_zone.values():
            if positions[(row + 1, column)].piece_color != self.piece_color:
                moves.append((row + 1, column))
        else:
            if row + 1 < 8 and (row + 1, column) not in self.danger_zone.values():
                moves.append((row + 1, column))

        if (row + 1, column + 1) in positions and (row + 1, column + 1) not in self.danger_zone.values():
            if positions[(row + 1, column + 1)].piece_color != self.piece_color:
                moves.append((row + 1, column + 1))
        else:
            if row + 1 < 8 and column + 1 < 8 and (row + 1, column + 1) not in self.danger_zone.values():
                moves.append((row + 1, column + 1))

        if (row, column + 1) in positions and (row, column + 1) not in self.danger_zone.values():
            if positions[(row, column + 1)].piece_color != self.piece_color:
                moves.append((row, column + 1))
        else:
            if column + 1 < 8 and (row, column + 1) not in self.danger_zone.values():
                moves.append((row, column + 1))
#
        if (row - 1, column + 1) in positions and (row - 1, column + 1) not in self.danger_zone.values():
            if positions[(row - 1, column + 1)].piece_color != self.piece_color:
                moves.append((row - 1, column + 1))
        else:
            if row - 1 > -1 and column + 1 < 8 and (row - 1, column + 1) not in self.danger_zone.values():
                moves.append((row - 1, column + 1))

        if (row + 1, column - 1) in positions and (row + 1, column - 1) not in self.danger_zone.values():
            if positions[(row + 1, column - 1)].piece_color != self.piece_color:
                moves.append((row + 1, column - 1))
        else:
            if row + 1 < 8 and column - 1 > -1 and (row + 1, column - 1) not in self.danger_zone.values():
                moves.append((row + 1, column - 1))

        if (row - 1, column) in positions and (row - 1, column) not in self.danger_zone.values():
            if positions[(row - 1, column)].piece_color != self.piece_color:
                moves.append((row, column + 1))
        else:
            if row - 1 > -1 and (row - 1, column) not in self.danger_zone.values():
                moves.append((row - 1, column))

        if (row, column - 1) in positions and (row, column - 1) not in self.danger_zone.values():
            if positions[(row, column - 1)].piece_color != self.piece_color:
                moves.append((row, column - 1))
        else:
            if column - 1 > -1 and (row, column - 1) not in self.danger_zone.values():
                moves.append((row, column - 1))

        if (row - 1, column - 1) in positions and (row - 1, column - 1) not in self.danger_zone.values():
            if positions[(row - 1, column - 1)].piece_color != self.piece_color:
                moves.append((row - 1, column - 1))
        else:
            if column - 1 > -1 and row - 1 > -1 and (row - 1, column - 1) not in self.danger_zone.values():
                moves.append((row - 1, column - 1))
        # Castling
        if (0, 7) in positions and (0,7) not in self.danger_zone.values():
            if type(positions[(0, 7)]) is Rook and positions[0, 7].piece_color == self.piece_color and positions[
                0, 7].MOVED == False and self.MOVED == False and self.IN_CHECK == False and (
                    0, 6) not in positions and (0, 5) not in positions:
                moves.append((0, 6))

        if (0, 0) in positions and (0,0) not in self.danger_zone.values():
            if type(positions[(0, 0)]) is Rook and positions[0, 0].piece_color == self.piece_color and positions[
                0, 0].MOVED == False and self.MOVED == False and self.IN_CHECK == False and (
                    0, 2) not in positions and (0, 3) not in positions and (0, 1) not in positions:
                moves.append((0, 1))
        return moves


class Queen(Piece):
    def __init__(self, row, column, image, piece_color, point_value):
        super().__init__(row, column, image, piece_color, point_value)

    def move_list(self, row, column, positions):
        moves = []
        for i in range(7):
            if (row + 1 + i, column + 1 + i) in positions.keys():
                if positions[(row + 1 + i, column + 1 + i)].piece_color != self.piece_color:
                    moves.append((row + 1 + i, column + i + 1))
                    break
                else:
                    break
            else:
                if column + i + 1 < 8 and row + i + 1 < 8:
                    moves.append((row + 1 + i, column + i + 1))

        for i in range(7):
            if (row + 1 + i, column - 1 - i) in positions.keys():
                if positions[(row + 1 + i, column - 1 - i)].piece_color != self.piece_color:
                    moves.append((row + 1 + i, column - i - 1))
                    break
                else:
                    break
            else:
                if column - i - 1 > -1 and row + i + 1 < 8:
                    moves.append((row + 1 + i, column - i - 1))

        for i in range(7):
            if (row - 1 - i, column - 1 - i) in positions.keys():
                if positions[(row - 1 - i, column - 1 - i)].piece_color != self.piece_color:
                    moves.append((row - 1 - i, column - i - 1))
                    break
                else:
                    break
            else:
                if column - i - 1 > -1 and row - i - 1 > -1:
                    moves.append((row - 1 - i, column - i - 1))

        for i in range(7):
            if (row - 1 - i, column + 1 + i) in positions.keys():
                if positions[(row - 1 - i, column + 1 + i)].piece_color != self.piece_color:
                    moves.append((row - 1 - i, column + i + 1))
                    break
                else:
                    break
            else:
                if column + i + 1 < 8 and row - i - 1 > -1:
                    moves.append((row - 1 - i, column + i + 1))

        for i in range(7):
            if (row + 1 + i, column) in positions.keys():
                if positions[(row + 1 + i, column)].piece_color == self.piece_color:
                    break
                else:
                    # print("Hi")
                    moves.append((row + 1 + i, column))
                    break
            else:
                if row + 1 + i < 8:
                    moves.append((row + 1 + i, column))

        for i in range(7):
            if (row, column + 1 + i) in positions.keys():
                if positions[(row, column + 1 + i)].piece_color == self.piece_color:
                    break
                else:
                    moves.append((row, column + 1 + i))
                    break
            else:
                if column + 1 + i < 8:
                    moves.append((row, column + 1 + i))

        for i in range(7):
            if (row - 1 - i, column) in positions.keys():
                if positions[(row - 1 - i, column)].piece_color == self.piece_color:
                    break
                else:
                    moves.append((row - 1 - i, column))
                    break
            else:
                if row - 1 - i > -1:
                    moves.append((row - 1 - i, column))

        for i in range(7):
            if (row, column - 1 - i) in positions.keys():
                if positions[(row, column - 1 - i)].piece_color == self.piece_color:
                    break
                else:
                    moves.append((row, column - 1 - i))
                    break
            else:
                if column - 1 - i > -1:
                    moves.append((row, column - 1 - i))
        return moves
