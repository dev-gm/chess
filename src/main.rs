mod chessboard;
use chessboard::{Chessboard, Cell};
use chessboard::pieces::{Piece, Position};

fn main() {
    let mut default: [Cell; 7*7];
    for x in 0..7 {
        for y in 0..7 {
            let piece = get_piece_by_pos(x, y);
            default[x*y] = Cell::new(Position(x, y), Piece::new(piece))
        }
    }
    let chessboard = Chessboard::new(default);
}

fn get_piece_by_pos(x: i32, y: i32) -> Option<String> {
    match x {
        1 | 6 => Some(String::from("pawn")),
        0 | 7 => match y {
            0 | 7 => Some(String::from("rook")),
            1 | 6 => Some(String::from("knight")),
            2 | 5 => Some(String::from("bishop")),
            3 => Some(String::from("queen")),
            4 => Some(String::from("king"))
        },
        _ => None
    }
}
