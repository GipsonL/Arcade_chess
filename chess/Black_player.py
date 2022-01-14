import math
import board
import main
import piece


class Player:

    def __init__(self, my_pieces, enemy_pieces):
        self.my_pieces = my_pieces
        self.enemy_pieces = enemy_pieces
        self.enemy_king = None
        for x in self.enemy_pieces:
            if type(x) is piece.King:
                self.enemy_king = x

    def find_takeable_pieces(self):
        takable_pieces = []
        for x in self.my_pieces:
            for y in x.move_list(x.get_row(), x.get_column(), board.Board.filled_spots):
                if y in board.Board.filled_spots and board.Board.filled_spots[y].piece_color != x.piece_color:
                    takable_pieces.append((x, board.Board.filled_spots[y]))
        return takable_pieces

    def find_shortest_paths(self):
        """Method for finding the move that moves one of the computer's pieces closest to the enemy king."""
        #print(str(self.my_pieces))
        distances = []
        for x in self.my_pieces:
            curr_move_set = x.move_list(x.get_row(), x.get_column(), board.Board.filled_spots)
            if curr_move_set:
                least = math.hypot(self.enemy_king.get_column() - curr_move_set[0][1], #[0][1]
                                   self.enemy_king.get_row() - curr_move_set[0][0])  #[0][1]
                spot = None
            else:
                continue
            for y in curr_move_set:
                if math.hypot(self.enemy_king.get_column() - y[1], self.enemy_king.get_row() - y[0]) <= least:
                    least = math.hypot(self.enemy_king.get_column() - y[1], self.enemy_king.get_row() - y[0])
                    spot = (y[0], y[1])
            distances.append((least, x, spot))
        print("Distances:")
        print(distances)
        return distances

    def find_move(self, chess_list):
        takeable_pieces = self.find_takeable_pieces()
        if takeable_pieces:
            print("HI")
            greatest = takeable_pieces[0]
            for x in takeable_pieces:
                if x[1].get_point_value() > greatest[1].get_point_value():
                    greatest = x
            self.make_move(greatest[0], greatest[1].get_chess_position(), chess_list)
            #print(str(greatest[0]))
            #print((greatest[1].get_chess_position()))
        else:
            print("Bye")
            paths = self.find_shortest_paths()
            print(paths)
            if paths:
                least = paths[0]
                for y in paths:
                    if y[0] < least[0]:
                        least = y
                print(least)
                self.make_move(least[1], least[2], chess_list)

    def sync_with_list(self, game_list):
        self.my_pieces.clear()
        for x in game_list:
            if x.piece_color != 'white':
                self.my_pieces.append(x)

    def make_move(self, move_piece, spot, chess_list):
        print(move_piece)
       # print(move_piece)
        #print(spot)
        if spot in board.Board.filled_spots:
            chess_list.remove(board.Board.filled_spots[spot])
            del board.Board.filled_spots[spot]
        del board.Board.filled_spots[move_piece.get_chess_position()]
        move_piece.set_chess_position(board.Board.grid.get(spot))
        move_piece.MOVED = True
        move_piece.set_row(spot[0])
        move_piece.set_column(spot[1])
        board.Board.filled_spots[move_piece.get_chess_position()] = move_piece

