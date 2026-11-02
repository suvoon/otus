from bitcount import bitcount_v1

BB = (1 << 64) - 1

COL_A = 0xFEFEFEFEFEFEFEFE
COL_H = 0x7F7F7F7F7F7F7F7F

def square_to_index(square: str) -> int:
    file = ord(square[0].lower()) - ord('a')
    rank = int(square[1]) - 1
    return rank * 8 + file


def king_moves(sq: int) -> int:
    bb = 1 << sq
    moves = 0

    moves |= (bb & COL_H) << 1
    moves |= (bb & COL_A) >> 1

    moves |= (bb << 8) & BB
    moves |= bb >> 8

    moves |= ((bb & COL_H) << 9) & BB
    moves |= ((bb & COL_A) << 7) & BB
    moves |= (bb & COL_H) >> 7
    moves |= (bb & COL_A) >> 9

    return moves & BB


def king_move_count(square: str) -> int:
    sq = square_to_index(square)
    moves = king_moves(sq)
    return bitcount_v1(moves)


def main():
    print("enter king position:")
    square = input()
    print("moves from position:", king_move_count(square))

main()