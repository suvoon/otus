import random
import time


def radix_sort(arr):
    base = 10
    digits = 3
    n = len(arr)
    T = [0] * n
    r = 1
    for _ in range(digits):
        radix = [0] * base
        for i in range(n):
            dig = (arr[i] // r) % base
            radix[dig] += 1
        z = 0
        for i in range(base):
            z += radix[i]
            radix[i] = z
        for i in range(n - 1, -1, -1):
            dig = (arr[i] // r) % base
            radix[dig] -= 1
            T[radix[dig]] = arr[i]
        for i in range(n):
            arr[i] = T[i]
        r *= base
    return arr


def main():
    sizes = [10**2, 10**3, 10**4, 10**5, 10**6]
    for size in sizes:
        arr = [random.randint(0, 999) for _ in range(size)]
        start = time.perf_counter()
        radix_sort(arr)
        elapsed = time.perf_counter() - start
        print(f"Размер: {size}, Время: {elapsed:.6f} с.")

main()