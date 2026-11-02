def bitcount_v1(n):
    count = 0
    while (n > 0):
        if (n & 0x01 > 0):
            count += 1
        n >>= 1
    return count

def bitcount_v2(n):
    count = 0
    while (n > 0):
        count += 1
        n &= n - 1
    return count

def main():
    print("bitcount_v1 n:")
    n1 = input()
    print("v1 result:", bitcount_v1(int(n1)))
    print("bitcount_v2 n:")
    n2 = input()
    print("v2 result:", bitcount_v2(int(n2)))