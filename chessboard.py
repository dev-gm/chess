from pieces import *


class Chessboard(dict):
    def __init__(self, default):
        super().__init__()
        x = 0
        y = 0
        for row in default:
            for item in row:
                color = list(item.keys())[0]
                piece = item[color][0].upper()+item[color][1:]
                cell = Cell(self, color, piece, x, y)
                self[cell.position] = cell
                x += 1
            x = 0
            y += 1

    def update(self):
        for cell in self.values():
            cell.possible = cell.piece.calculate()


class Cell:
    def __init__(self, board, color, piece, x, y):
        self.board = board
        self.position = (x, y)
        self.piece_name = piece
        exec(f"self.piece = {piece}(self, color)")
        self.board.update()
