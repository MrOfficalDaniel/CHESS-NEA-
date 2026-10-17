from const import *
from Pieces import *
from square import Square

#class Square:
    #def __init__(self, row, col, piece=None):
     #   self.row = row
      #  self.col = col
       # self.piece = piece




class Board2:
    def __init__(self):
        self.square = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        self._create()
        self._add_pieces("white")
        self._add_pieces("black")

    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.square[row][col] = Square(row, col)

    def _add_pieces(self, color):
        row_pawn, row_other = (6, 7) if color == "white" else (1, 0)
#pawns
        for col in range(COLS):
            self.square[row_pawn][col] = Square(row_pawn, col, Pawn(color))

#knights
        self.square[row_other][1] = Square(row_other, 1, Knight(color))
        self.square[row_other][6] = Square(row_other, 6, Knight(color))

#bishops
        self.square[row_other][2] = Square(row_other, 2, Bishop(color))
        self.square[row_other][5] = Square(row_other, 5, Bishop(color))

#rooks
        self.square[row_other][0] = Square(row_other, 0, Rook(color))
        self.square[row_other][7] = Square(row_other, 7, Rook(color))

#queen
        self.square[row_other][3] = Square(row_other, 3, Queen(color))

#king
        self.square[row_other][4] = Square(row_other, 4, King(color))   
