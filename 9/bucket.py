import random
import time
import bisect
from multiprocessing import Process, Queue


def bucket_sort(arr, num_buckets=10):
    baskets = [[] for _ in range(num_buckets)]
    for x in arr:
        idx = x * num_buckets // 1000
        bisect.insort(baskets[idx], x)
    j = 0
    for b in baskets:
        for x in b:
            arr[j] = x
            j += 1
    return arr


def worker(arr, queue):
    bucket_sort(arr)
    queue.put(True)


def main():
    sizes = [10**2, 10**3, 10**4, 10**5, 10**6]
    for size in sizes:
        arr = [random.randint(0, 999) for _ in range(size)]
        q = Queue()
        p = Process(target=worker, args=(arr, q))
        start = time.perf_counter()
        p.start()
        p.join(120)
        elapsed = time.perf_counter() - start
        if p.is_alive():
            p.terminate()
            p.join()
            print(f"Размер: {size}, Время: timeout (превышено 2 минуты)")
        else:
            print(f"Размер: {size}, Время: {elapsed:.6f} с.")

if __name__ == "__main__":
    main()