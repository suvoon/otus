import binascii


class HashTable:
    def __init__(self, size=10, load_factor=0.75):
        self.size = size
        self.buckets = [None] * size
        self.count = 0
        self.load_factor = load_factor

    def _hash(self, key, size):
        crc = binascii.crc32(key.encode("utf-8")) & 0xFFFFFFFF
        return crc % size

    def _rehash(self):
        new_size = self.size * 2
        new_buckets = [None] * new_size
        for bucket in self.buckets:
            if bucket is None:
                continue
            for k, v in bucket:
                idx = self._hash(k, new_size)
                if new_buckets[idx] is None:
                    new_buckets[idx] = []
                new_buckets[idx].append((k, v))
        self.size = new_size
        self.buckets = new_buckets

    def put(self, key, value):
        idx = self._hash(key, self.size)
        bucket = self.buckets[idx]
        if bucket is not None:
            for i, (k, _) in enumerate(bucket):
                if k == key:
                    bucket[i] = (key, value)
                    return False
        else:
            bucket = []
            self.buckets[idx] = bucket

        bucket.append((key, value))
        self.count += 1

        if self.count / self.size > self.load_factor:
            self._rehash()
        return True

    def get(self, key, default=None):
        idx = self._hash(key, self.size)
        bucket = self.buckets[idx]
        if bucket is not None:
            for k, v in bucket:
                if k == key:
                    return v
        if default is not None:
            return default
        raise KeyError(key)

    def remove(self, key):
        idx = self._hash(key, self.size)
        bucket = self.buckets[idx]
        if bucket is not None:
            for i, (k, v) in enumerate(bucket):
                if k == key:
                    del bucket[i]
                    self.count -= 1
                    if not bucket:
                        self.buckets[idx] = None
                    return v
        raise KeyError(key)

    def display(self):
        for i in range(self.size):
            print(f"{i}: ", end="")
            if self.buckets[i] is not None:
                for k, v in self.buckets[i]:
                    print(f"{k} - {v}\t", end="")
            print()


if __name__ == "__main__":
    ht = HashTable(10)
    keys = ["cat", "dog", "pig", "cow", "fox", "owl"]
    values = ["orange", "brown", "pink", "white", "red", "grey"]

    for k, v in zip(keys, values):
        ht.put(k, v)

    print("=== После вставки ===")
    ht.display()

    print("\nget('cat') =", ht.get("cat"))
    print("get('owl') =", ht.get("owl"))

    is_new = ht.put("cat", "black")
    print(f"put('cat','black') -> новый ключ? {is_new}; значение: {ht.get('cat')}")

    ht.remove("pig")
    print("\n=== После remove('pig') ===")
    ht.display()

    for i in range(30):
        ht.put(f"key{i}", f"val{i}")
    print(f"\nПосле массовой вставки: size={ht.size}, count={ht.count}")