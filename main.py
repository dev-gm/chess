from chessboard import *
from pieces import *

default = [[{'white': 'rook'}, {'white': 'knight'}, {'white': 'bishop'}, {'white': 'queen'}, {'white': 'king'}, {'white': 'bishop'}, {'white': 'knight'}, {'white': 'rook'}],
[{'white': 'pawn'}, {'white': 'pawn'}, {'white': 'pawn'}, {'white': 'pawn'}, {'white': 'pawn'}, {'white': 'pawn'}, {'white': 'pawn'}, {'white': 'pawn'}],
[{'empty': 'empty'}, {'empty': 'empty'}, {'empty': 'empty'}, {'empty': 'empty'}, {'empty': 'empty'}, {'empty': 'empty'}, {'empty': 'empty'}, {'empty': 'empty'}],
[{'empty': 'empty'}, {'empty': 'empty'}, {'empty': 'empty'}, {'empty': 'empty'}, {'empty': 'empty'}, {'empty': 'empty'}, {'empty': 'empty'}, {'empty': 'empty'}],
[{'empty': 'empty'}, {'empty': 'empty'}, {'empty': 'empty'}, {'empty': 'empty'}, {'empty': 'empty'}, {'empty': 'empty'}, {'empty': 'empty'}, {'empty': 'empty'}],
[{'empty': 'empty'}, {'empty': 'empty'}, {'empty': 'empty'}, {'empty': 'empty'}, {'empty': 'empty'}, {'empty': 'empty'}, {'empty': 'empty'}, {'empty': 'empty'}],
[{'black': 'pawn'}, {'black': 'pawn'}, {'black': 'pawn'}, {'black': 'pawn'}, {'black': 'pawn'}, {'black': 'pawn'}, {'black': 'pawn'}, {'black': 'pawn'}],
[{'black': 'rook'}, {'black': 'knight'}, {'black': 'bishop'}, {'black': 'queen'}, {'black': 'king'}, {'black': 'bishop'}, {'black': 'knight'}, {'black': 'rook'}]]

if __name__ == "__main__":
  chessboard = Chessboard(default)
  for position in list(chessboard.keys()):
      item = chessboard.get(position)
      print(position, item.piece.color, item.piece_name, item.piece.calculate())

