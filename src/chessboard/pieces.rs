use std::vec::Vec;

use crate::chessboard::*;

pub struct Position(pub i32, pub i32);

pub enum PieceColor {
    Black,
    White
}

pub struct Pawn;
pub struct Knight;
pub struct Bishop;
pub struct Rook;
pub struct Queen;
pub struct King;

pub enum Piece {
    Pawn(Pawn),
    Knight(Knight),
    Bishop(Bishop),
    Rook(Rook),
    Queen(Queen),
    King(King)
}

pub trait PieceLogic {
    fn new() -> Self;

    fn possible(&self, chessboard: &Chessboard) -> Vec<Action>;
}

impl PieceLogic for Pawn {
    fn new() -> Self { Self }

    fn possible(&self, chessboard: &Chessboard) -> Vec<Action> {
        let mut actions = Vec::new();
        let Position(x, y) = chessboard.get_cell_by_piece(self).position;
        for pos in [Position(x+1, y-1), Position(x+1, y+1)].iter() {
            if let Some(action) = Action::Take::new(self, chessboard.get(Position(x, y))) {
                actions.append(action);
            }
        }
        if let Some(action) = Action::Move::new(self, chessboard.get(Position(x+1, y))) {
            actions.append(action);
        }
        actions
    }
}

impl PieceLogic for Knight {
    fn new() -> Self { Self }

    fn possible(&self, chessboard: &Chessboard) -> Vec<Action> {
        let mut actions = Vec::new();
        let Position(x, y) = chessboard.get_cell_by_piece(self).position;
        for xfactor in [-2, -4, 2, 4].iter() {
            let yfactors = if xfactor.abs() == 4 { [-2, 2] } else { [-4, 4] };
            for yfactor in yfactors.iter() {
                let action = Action::new(chessboard.get([x+xfactor, y+yfactor]));
                actions.append(action);
            }
        }
        actions
    }
}

impl PieceLogic for Bishop {
    fn new() -> Self { Self }

    fn possible(&self, chessboard: &Chessboard) -> Vec<Action> {
        let mut actions = Vec::new();
        let cell = chessboard.get_cell_by_piece(self);
        let bounds = chessboard.bounds;
        let factors = [-1, 1];
        for xfactor in factors.iter() {
            for yfactor in factors.iter() {
                let mut Position(x, y) = cell.position;
                while chessboard.check_in_bounds(Position(x, y)) && action != Action::Action::Take {
                    x += xfactor;
                    y += yfactor;
                    let action = Action::new(chessboard.get(Position(x, y)));
                    actions.append(action);
                }
            }
        }
        actions
    }
}

impl PieceLogic for Rook {
    fn new() -> Self { Self }

    fn possible(&self, chessboard: &Chessboard) -> Vec<Action> {
        let mut actions = Vec::new();
        let pos = chessboard.get_cell_by_piece(self).position;
        let bounds = chessboard.bounds;
        for i in [1, -1].iter() {
            for add in [[0, i], [i, 0]] {
                let mut Position(x, y) = pos;
                while chessboard.check_in_bounds(Position(x, y)) {
                    x += add[0];
                    y += add[1];
                    let action = Action::new(chessboard.get(Position(x, y)));
                    if action == Action::Take {
                        break;
                    }
                }
            }
        }
        actions
    }
}

impl PieceLogic for Queen {
    fn new() -> Self { Self }

    fn possible(&self, chessboard: &Chessboard) -> Vec<Action> {
        let mut actions = Vec::new();
        let pos = chessboard.get_cell_by_piece(self).position;
        let bounds = chessboard.bounds;
        for i in [1, -1].iter() {
            'bishop: for add in [[0, *i], [*i, 0]].iter() {
                let Position(mut x, mut y) = pos;
                while (x > bounds[1].0 && y > bounds[0].1) && (x <= bounds[1].0 && y <= bounds[1].1) {
                    x += add[0];
                    y += add[1];
                    let action = Action::new(chessboard.get(Position(x, y)));
                    if action == Action::Take {
                        break 'bishop;
                    }
                }
            }
            let xfactor = i;
            'rook: for yfactor in [-1, 1].iter() {
                let Position(mut x, mut y) = pos;
                while (x > bounds[1].0 && y > bounds[0].1) && (x <= bounds[1].0 && y <= bounds[1].1) {
                    x += xfactor;
                    y += yfactor;
                    let action = Action::new(chessboard.get(Position(x, y)));
                    actions.append(action);
                    if action == Action::Take {
                        break 'rook;
                    }
                }
            }
        }
        actions
    }
}

impl PieceLogic for King {
    fn new() -> Self { Self }

    fn possible(&self, chessboard: &Chessboard) -> Vec<Action> {
        let mut actions = Vec::new();
        let pos = chessboard.get_cell_by_piece(self).position;
        let bounds = chessboard.bounds;
        let xfactors = [0, -1, 1];
        let yfactors = [-1, 1];
        'outer: for x in xfactors.iter() {
            for y in yfactors.iter() {
                if !chessboard.check_in_bounds(Position(*x, *y)) {
                    break 'outer;
                }
                actions.append(Action::new(chessboard.get(Position(*x, *y))));
            }
            let yfactors = [0, -1, 1];
        }
        actions
    }
}
