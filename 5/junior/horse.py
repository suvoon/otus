from bitcount import bitcount_v1

BB = (1 << 64) - 1

COL_A = 0xFEFEFEFEFEFEFEFE
COL_AB = 0xFCFCFCFCFCFCFCFC
COL_GH = 0x3F3F3F3F3F3F3F3F
COL_H = 0x7F7F7F7F7F7F7F7F

def square_to_index(square: str) -> int:
    file = ord(square[0].lower()) - ord('a')
    rank = int(square[1]) - 1
    return rank * 8 + file


def horse_moves(sq: int) -> int:
    bb = 1 << sq
    moves = 0

    moves = COL_GH & (bb << 6 | bb >> 10)
    moves |= COL_H & (bb << 15 | bb >> 17)
    moves |= COL_A & (bb << 17 | bb >> 15)
    moves |= COL_AB & (bb << 10 | bb >> 6)

    return moves & BB


def horse_move_count(square: str) -> int:
    sq = square_to_index(square)
    moves = horse_moves(sq)
    return bitcount_v1(moves)


def main():
    print("enter horse position:")
    square = input()
    print("moves from position:", horse_move_count(square))

main()