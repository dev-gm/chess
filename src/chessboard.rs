use std::vec::Vec;

mod pieces;
use pieces::*;

pub struct Chessboard {
    pub bounds: [Position; 2],
    cells: [Cell; 7 * 7],
}

impl Chessboard {
    pub fn new(default: [Cell; 7 * 7]) -> Self {
        Self {
            bounds: [Position(0, 0), Position(default.len(), default.len())],
            cells: default,
        }
    }

    pub fn get(&self, pos: Position) -> Option<&Cell> {
        for cell in self.cells.iter() {
            if cell.position == pos {
                return Some(cell);
            }
        }
        None
    }

    pub fn get_cell_by_piece(&self, target: &Piece) -> &Cell {
        for cell in self.cells.iter() {
            if let Some(piece) = cell.piece {
                if piece == target {
                    return cell;
                }
            }
        }
        &self.cells[0]
    }
    pub fn out_of_bounds(&self, pos: Position) -> bool {
        (pos.0 > self.bounds[1].0 && pos.1 > self.bounds[0].1)
            && (pos.0 <= self.bounds[1].0 && pos.1 <= self.bounds[1].1)
    }
}

pub struct Cell {
    pub position: Position,
    pub piece: Option<Piece>,
}

impl Cell {
    pub fn new(pos: Position, piece: Option<Piece>) -> Self {
        Self {
            position: pos,
            piece,
        }
    }
}

pub struct Piece;

impl Piece {
    fn new(name: Option<&str>) -> fn() {
        match name {
            Some("pawn") => Pawn::new,
            Some("knight") => Knight::new,
            Some("bishop") => Bishop::new,
            Some("rook") => Rook::new,
            Some("queen") => Queen::new,
            Some("king") => King::new,
            _ => None
        }
    }
}