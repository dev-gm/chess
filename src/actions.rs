mod chessboard;
use chessboard::*;

pub enum Action {
    Move(&mut Cell),
    Take(&mut Cell),
    Castle(&mut Cell)
}

impl Action {
    pub fn new(cell: Option<&mut Cell>) -> Option<Self> {
        if let Some(target) = cell {
            if let Some(piece) = target.piece {
                return Some(Action::Take(target));
            } else {
                return Some(Action::Move(target));
            }
        }
        None
    }
}

trait ActionLogic {
    pub fn new(cell: Option<&mut Cell>) -> Option<Self>;

    pub fn do(&self, from: &mut Cell);
}

impl ActionLogic for Action::Move {
    pub fn new(cell: Option<&mut Cell>) -> Option<Self> {
        if let Some(target) = cell {
            if !(let Some(piece) = target.piece) {
                return Some(target);
            }
        }
        None
    }

    pub fn do(&self, from: &mut Cell) {}
}

impl ActionLogic for Action::Take {
    pub fn new(cell: Option<&mut Cell>) -> Option<Self> {
        if let Some(target) = cell {
            if let Some(piece) = target.piece {
                return Some(target);
            }
        }
        None
    }

    pub fn do(self, from: &mut Cell) {}
}