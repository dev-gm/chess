class Piece:
    def __init__(self, cell, color):
        self.color = color
        self.cell = cell
        self.board = self.cell.board
        self.position = self.cell.position
        self.possible = self.calculate()


class Pawn(Piece):
    def calculate(self):
        x = self.position[0]
        y = self.position[1]
        possible = []
        if self.color == "white":
            forward = (x, y+1)
            diagonals = [(x+1, y+1), (x-1, y+1)]
            for p in diagonals:
                if self.board.get(p) != None:
                    if self.board.get(p).piece.color == "black":
                        possible.append(p)
            if self.board.get(forward) != None:
                if self.board.get(forward).piece_name == "Empty":
                    possible.append(forward)
        elif self.color == "black":
            forward = (x, y-1)
            diagonals = [(x+1, y-1), (x-1, y-1)]
            for p in diagonals:
                if self.board.get(p) != None:
                    if self.board.get(p).piece.color == "white":
                        possible.append(p)
            if self.board.get(forward) != None:
                if self.board.get(forward).piece_name == "Empty":
                    possible.append(forward)
        return possible


class Knight(Piece):
    def calculate(self):
        x = self.position[0]
        y = self.position[1]
        all = [(x-2, y-1), (x-2, y+1), (x-1, y-2), (x-1, y+2), (x+1, y-2), (x+1, y+2), (x+2, y-1), (x+2, y+1)]
        possible = []
        for p in all:
            if self.board.get(p) != None:
                if self.board.get(p).piece_name == "Empty":
                    possible.append(p)
                elif self.board.get(p).piece.color != self.color and self.board.get(p).piece.color != "empty":
                    possible.append(p)
        return possible


class Bishop(Piece):
    def calculate(self):
        print(self.position)
        x = self.position[0]
        y = self.position[1]
        possible = []
        # forward right
        px = x
        py = y
        while px < 7 and py < 7:
            px += 1
            py += 1
            p = (px, py)
            if self.board.get(p) != None:
                if self.board.get(p).piece_name == "Empty":
                    possible.append(p)
                elif self.board.get(p).piece.color != self.color and self.board.get(p).piece.color != "empty":
                    possible.append(p)
                    break
        # forward left
        px = x
        py = y
        while px > 0 and py < 7:
            px -= 1
            py += 1
            p = (px, py)
            if self.board.get(p) != None:
                if self.board.get(p).piece_name == "Empty":
                    possible.append(p)
                elif self.board.get(p).piece.color != self.color and self.board.get(p).piece.color != "empty":
                    possible.append(p)
                    break
        # backwards right
        px = x
        py = y
        while px < 7 and py > 0:
            px += 1
            py -= 1
            p = (px, py)
            if self.board.get(p) != None:
                if self.board.get(p).piece_name == "Empty":
                    possible.append(p)
                elif self.board.get(p).piece.color != self.color and self.board.get(p).piece.color != "empty":
                    possible.append(p)
                    break
        # backwards right
        px = x
        py = y
        while px > 0 and py > 0:
            px -= 1
            py -= 1
            p = (px, py)
            if self.board.get(p) != None:
                if self.board.get(p).piece_name == "Empty":
                    possible.append(p)
                elif self.board.get(p).piece.color != self.color and self.board.get(p).piece.color != "empty":
                    possible.append(p)
                    break
        return possible


class Rook(Piece):
    def calculate(self):
        x = self.position[0]
        y = self.position[1]
        possible = []
        # forward
        for y in range(y+1, 8):
            p = (x, y)
            if self.board.get(p) != None:
                if self.board.get(p).piece_name == "Empty":
                    possible.append(p)
                elif self.board.get(p).piece.color != self.color and self.board.get(p).piece.color != "empty":
                    possible.append(p)
                    break
        # backwards
        for y in range(-1, y, -1):
            p = (x, y)
            if self.board.get(p) != None:
                if self.board.get(p).piece_name == "Empty":
                    possible.append(p)
                elif self.board.get(p).piece.color != self.color and self.board.get(p).piece.color != "empty":
                    possible.append(p)
                    break
        # right
        for x in range(x+1, 8):
            p = (x, y)
            if self.board.get(p) != None:
                if self.board.get(p).piece_name == "Empty":
                    possible.append(p)
                elif self.board.get(p).piece.color != self.color and self.board.get(p).piece.color != "empty":
                    possible.append(p)
                    break
        # left
        for x in range(-1, x, -1):
            p = (x, y)
            if self.board.get(p) != None:
                if self.board.get(p).piece_name == "Empty":
                    possible.append(p)
                elif self.board.get(p).piece.color != self.color and self.board.get(p).piece.color != "empty":
                    possible.append(p)
                    break
        return possible


class Queen(Piece):
    def calculate(self):
        x = self.position[0]
        y = self.position[1]
        possible = []
        return possible

class King(Piece):
    def calculate(self):
        x = self.position[0]
        y = self.position[1]
        all = [(x+1,y+1), (x+1,y-1), (x+1,y), (x-1,y+1), (x-1,y-1), (x-1,y), (x,y+1), (x,y-1)]
        possible = []
        for p in all:
            if self.board.get(p) != None:
                if self.board.get(p).piece_name == "Empty":
                    possible.append(p)
                elif self.board.get(p).piece.color != self.color and self.board.get(p).piece.color != "empty":
                    possible.append(p)
        return possible


class Empty(Piece):
    def calculate(self):
        return []
