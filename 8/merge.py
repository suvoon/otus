import random
import time


def merge_up(arr):
    step = 1
    n = len(arr)
    T = [None] * n

    while step < n:
        index = 0
        l = 0
        m = l + step
        r = l + step * 2

        while l < n:
            m = m if m < n else n
            r = r if r < n else n

            i1 = l
            i2 = m

            while i1 < m and i2 < r:
                if arr[i1] <= arr[i2]:
                    T[index] = arr[i1]
                    i1 += 1
                else:
                    T[index] = arr[i2]
                    i2 += 1
                index += 1

            while i1 < m:
                T[index] = arr[i1]
                i1 += 1
                index += 1

            while i2 < r:
                T[index] = arr[i2]
                i2 += 1
                index += 1

            l += step * 2
            m += step * 2
            r += step * 2

        for i in range(n):
            arr[i] = T[i]

        step *= 2

    return arr


def main():
    sizes = [10**2, 10**3, 10**4, 10**5, 10**6]
    for size in sizes:
        rand_arr = [random.randint(1, 10**6) for _ in range(size)]

        start_time = time.perf_counter()
        merge_up(rand_arr)
        elapsed_time = time.perf_counter() - start_time
        if elapsed_time > 120:
            print(f"Размер: {size}, Время: timeout (превышено 2 минуты)")
        else:
            print(f"Размер: {size}, Время: {elapsed_time:.6f} с.")

main()