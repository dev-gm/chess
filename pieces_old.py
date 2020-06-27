class Piece:
    def __init__(self, cell):
        self.cell = cell
        self.cell.possible = self.calculate()


class Pawn(Piece):
    def calculate(self):
        position = self.cell.position
        color = self.cell.color
        x = position[0]
        y = position[1]
        possible = []
        forward = (x, y+1)
        # diagonal
        all_diagonal = [[x+1, y+1], [x-1, y+1]]
        for diag in all_diagonal:
            diag = tuple(diag)
            if self.cell.board.get(diag):
                if self.cell.board.get(diag).piece_name == "empty":
                    possible.append(diag)
                elif self.cell.board.get(diag).color != self.cell.color:
                    possible.append(diag)
        # forward
        if self.cell.board.get(forward):
          if self.cell.board.get(forward).piece_name == "empty":
              possible.append(forward)
        return possible


class Knight(Piece):
    def calculate(self):
        position = self.cell.position
        x = position[0]
        y = position[1]
        possible = []
        possibilities = [[x-2, y-1], [x-2, y+1], [x-1, y-2], [x-1, y+2], [x+1, y-2], [x+1, y+2], [x+2, y-1], [x+2, y+1]]
        for p in possibilities:
            p = tuple(p)
            if self.cell.board.get(p):
                if self.cell.board.get(p).piece_name == "empty":
                    possible.append(p)
                elif self.cell.board.get(p).color != self.cell.color:
                    possible.append(p)
        return possible


class Bishop(Piece):
    def calculate(self):
        position = self.cell.position
        x = position[0]
        y = position[1]
        possible = []
        # forward right
        while x < 7 and y < 7:
            x += 1
            y += 1
            p = tuple([x, y])
            if self.cell.board.get(p):
                if self.cell.board.get(p).piece_name == "empty":
                    possible.append(p)
                elif self.cell.board.get(p).color != self.cell.color:
                    possible.append(p)
                    break
        # forward left
        while x > 0 and y < 7:
            x -= 1
            y += 1
            p = tuple([x, y])
            if self.cell.board.get(p):
                if self.cell.board.get(p).piece_name == "empty":
                    possible.append(p)
                elif self.cell.board.get(p).color != self.cell.color:
                    possible.append(p)
                    break
        # backward right
        while x < 7 and y > 0:
            x += 1
            y -= 1
            p = tuple([x, y])
            if self.cell.board.get(p):
                if self.cell.board.get(p).piece_name == "empty":
                    possible.append(p)
                elif self.cell.board.get(p).color != self.cell.color:
                    possible.append(p)
                    break
        # backward left
        while x > 0 and y > 0:
            x -= 1
            y -= 1
            p = tuple([x, y])
            if self.cell.board.get(p):
              if self.cell.board.get(p).piece_name == "empty":
                  possible.append(p)
              elif self.cell.board.get(p).color != self.cell.color:
                  possible.append(p)
                  break
        return possible


class Rook(Piece):
    def calculate(self):
        position = self.cell.position
        x = position[0]
        y = position[1]
        possible = []
        # forward
        for f in range(y+1, 8):
          p = tuple([x, f])
          if self.cell.board.get(p):
              if self.cell.board.get(p).piece_name == "empty":
                  possible.append(p)
              elif self.cell.board.get(p).color != self.cell.color:
                  possible.append(p)
                  break
        # backwards
        for b in range(y-1, -1, -1):
          p = tuple([x, b])
          if self.cell.board.get(p):
            if self.cell.board.get(p).piece_name == "empty":
              possible.append(p)
            elif self.cell.board.get(p).color != self.cell.color:
              possible.append(p)
              break
        # right
        for r in range(x+1, 8):
          p = tuple([r, y])
          if self.cell.board.get(p):
            if self.cell.board.get(p).piece_name == "empty":
              possible.append(p)
            elif self.cell.board.get(p).color != self.cell.color:
              possible.append(p)
        # left
        for l in range(x-1, -1, -1):
          p = tuple([l, y])
          if self.cell.board.get(p):
            if self.cell.board.get(p).piece_name == "empty":
              possible.append(p)
            elif self.cell.board.get(p).color != self.cell.color:
              possible.append(p)
        return possible


class Queen(Piece):
    def calculate(self):
        position = self.cell.position
        x = position[0]
        y = position[1]
        possible = []
        # bishop movements
        # forward right
        while x < 7 and y < 7:
            x += 1
            y += 1
            p = tuple([x, y])
            if self.cell.board.get(p):
              if self.cell.board.get(p).piece_name == "empty":
                  possible.append(p)
              elif self.cell.board.get(p).color != self.cell.color:
                  possible.append(p)
                  break
        # forward left
        while x > 0 and y < 7:
            x -= 1
            y += 1
            p = tuple([x, y])
            if self.cell.board.get(p):
              if self.cell.board.get(p).piece_name == "empty":
                  possible.append(p)
              elif self.cell.board.get(p).color != self.cell.color:
                  possible.append(p)
                  break
        # backward right
        while x < 7 and y > 0:
            x += 1
            y -= 1
            p = tuple([x, y])
            if self.cell.board.get(p):
              if self.cell.board.get(p).piece_name == "empty":
                  possible.append(p)
              elif self.cell.board.get(p).color != self.cell.color:
                  possible.append(p)
                  break
        # backward left
        while x > 0 and y > 0:
            x -= 1
            y -= 1
            p = tuple([x, y])
            if self.cell.board.get(p):
              if self.cell.board.get(p).piece_name == "empty":
                  possible.append(p)
              elif self.cell.board.get(p).color != self.cell.color:
                  possible.append(p)
                  break
        # rook movements
        # forward
        for f in range(y+1, 8):
          p = tuple([x, f])
          if self.cell.board.get(p):
              if self.cell.board.get(p).piece_name == "empty":
                  possible.append(p)
              elif self.cell.board.get(p).color != self.cell.color:
                  possible.append(p)
                  break
        # backwards
        for b in range(y-1, -1, -1):
          p = tuple([x, p])
          if self.cell.board.get(p):
            if self.cell.board.get(p).piece_name == "empty":
              possible.append(p)
            elif self.cell.board.get(p).color != self.cell.color:
              possible.append(p)
              break
        # right
        for r in range(x+1, 8):
          p = tuple([r, y])
          if self.cell.board.get(p):
            if self.cell.board.get(p).piece_name == "empty":
              possible.append(p)
            elif self.cell.board.get(p).color != self.cell.color:
              possible.append(p)
        # left
        for l in range(x-1, -1, -1):
          p = tuple([l, y])
          if self.cell.board.get(p):
            if self.cell.board.get(p).piece_name == "empty":
              possible.append(p)
            elif self.cell.board.get(p).color != self.cell.color:
              possible.append(p)
        return possible


class King(Piece):
    def calculate(self):
        position = self.cell.position
        x = position[0]
        y = position[1]
        possible = []
        possibilities = [[x+1, y], [x+1, y+1], [x+1, y-1], [x-1, y], [x-1, y+1], [x-1, y-1], [x, y+1], [x, y-1]]
        for p in possibilities:
          p = tuple(p)
          if self.cell.board.get(p):
            if self.cell.board.get(p).piece_name == "empty":
              possible.append(p)
            elif self.cell.board.get(p).color != self.cell.color:
              possible.append(p)
        return possible


class Empty(Piece):
  def calculate(self):
    return []
