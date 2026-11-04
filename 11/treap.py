import random

class Treap:
    def __init__(self, key, weight=1, left=None, right=None):
        self.key = key
        self.weight = weight
        self.left = left
        self.right = right

    def split(self, key):
        if self.key <= key:
            if self.right is None:
                new_tree = None
                r = None
            else:
                new_tree, r = self.right.split(key)
            l = Treap(self.key, self.weight, self.left, new_tree)
        else:
            if self.left is None:
                l = None
                new_tree = None
            else:
                l, new_tree = self.left.split(key)
            r = Treap(self.key, self.weight, new_tree, self.right)
        return l, r

    @staticmethod
    def merge(l, r):
        if l is None:
            return r
        if r is None:
            return l
        if l.weight > r.weight:
            new_r = Treap.merge(l.right, r)
            return Treap(l.key, l.weight, l.left, new_r)
        else:
            new_l = Treap.merge(l, r.left)
            return Treap(r.key, r.weight, new_l, r.right)

    def add(self, key, weight=1):
        l, r = self.split(key)
        m = Treap(key, weight)
        return Treap.merge(Treap.merge(l, m), r)

    def remove(self, key):
        l, r = self.split(key - 1)
        m, r = r.split(key)
        return Treap.merge(l, r)

    def search_and_promote(self, key):
        if key == self.key:
            self.weight += 1
            return self
        if key < self.key:
            if self.left is None:
                return self
            self.left = self.left.search_and_promote(key)
            if self.left.weight > self.weight:
                new_root = self.left
                self.left = new_root.right
                new_root.right = self
                return new_root
            return self
        else:
            if self.right is None:
                return self
            self.right = self.right.search_and_promote(key)
            if self.right.weight > self.weight:
                new_root = self.right
                self.right = new_root.left
                new_root.left = self
                return new_root
            return self


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    treap = Treap(arr[0])
    for i in range(1, len(arr)):
        treap = treap.add(arr[i])
    treap = treap.remove(7)


if __name__ == "__main__":
    main()