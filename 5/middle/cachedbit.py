def bitcount_v1(n):
    count = 0
    while (n > 0):
        if (n & 0x01 > 0):
            count += 1
        n >>= 1
    return count

ones = [bitcount_v1(i) for i in range(16)]

def bitcount_v3(num: int) -> int:
    return ones[(num >> 4) & 0xF] + ones[num & 0xF]

def main():
    print("bitcount_v3 n:")
    n3 = input()
    print("v3 result:", bitcount_v3(int(n3)))

main()