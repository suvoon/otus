def bitcount_v1(n):
    count = 0
    while (n > 0):
        if (n & 0x01 > 0):
            count += 1
        n >>= 1
    return count

BB = (1 << 64) - 1

def square_to_index(square: str) -> int:
    file = ord(square[0].lower()) - ord('a')
    rank = int(square[1]) - 1
    return rank * 8 + file

def rook_moves(sq: int) -> int:
    bb = 1 << sq

    column = sq & 0b111
    row = sq >> 3

    column_mask = 0x0101010101010101 << column
    row_mask = 0xFF << (row << 3)

    moves = (column_mask | row_mask) & ~bb

    return moves & BB

def rook_move_count(square: str) -> int:
    sq = square_to_index(square)
    moves = rook_moves(sq)
    return bitcount_v1(moves)


def main():
    print("enter rook position:")
    square = input()
    print("moves from position:", rook_move_count(square))

main()