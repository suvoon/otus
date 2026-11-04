import random
import sys
import time
from collections import Counter

sys.setrecursionlimit(200000)

class TreeNode:
    def __init__(self, key):
        self._key = key
        self.left = None
        self.right = None

    @property
    def key(self):
        return self._key


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, key, curr=None):
        node = TreeNode(key)
        if self.root is None:
            self.root = node
            return
        if curr is None:
            curr = self.root
        if key < curr.key:
            if curr.left is None:
                curr.left = node
            else:
                self.insert(key, curr.left)
        else:
            if curr.right is None:
                curr.right = node
            else:
                self.insert(key, curr.right)

    def search(self, key, node=None):
        if self.root is None:
            return None
        if node is None:
            node = self.root
        if key == node.key:
            return node
        if key < node.key:
            if node.left is None:
                return None
            return self.search(key, node.left)
        if node.right is None:
            return None
        return self.search(key, node.right)

    def search_parent(self, node, search):
        if node is None:
            return None
        if search is None:
            return None
        if node.key == search.key:
            return None
        if search.left is not None:
            if node.key == search.left.key:
                return search
        if search.right is not None:
            if node.key == search.right.key:
                return search
        if node.key < search.key:
            return self.search_parent(node, search.left)
        return self.search_parent(node, search.right)

    def remove(self, key):
        if isinstance(key, TreeNode):
            self._remove_node(key)
            return
        node = self.search(key)
        if node is None:
            return
        self._remove_node(node)

    def _remove_node(self, node):
        parent = self.search_parent(node, self.root)
        if node.right is None:
            if parent is not None:
                if parent.left == node:
                    parent.left = node.left
                else:
                    parent.right = node.left
            else:
                self.root = node.left
            return
        min_node = node.right
        min_parent = node
        while min_node.left is not None:
            min_parent = min_node
            min_node = min_node.left
        if parent is not None:
            if parent.left == node:
                parent.left = min_node
            else:
                parent.right = min_node
        else:
            self.root = min_node
        if min_node != node.right:
            min_parent.left = min_node.right
            min_node.right = node.right
        min_node.left = node.left

    def print_tree(self, node=None):
        if node is None:
            return
        self.print_tree(node.left)
        print(str(node.key).rjust(3) + " ", end="")
        self.print_tree(node.right)

class Treap:
    def __init__(self, key, weight=1, left=None, right=None):
        self.key = key
        self.weight = weight
        self.left = left
        self.right = right

    def split(self, key):
        if self.key <= key:
            if self.right is None:
                new_tree, r = None, None
            else:
                new_tree, r = self.right.split(key)
            l = Treap(self.key, self.weight, self.left, new_tree)
        else:
            if self.left is None:
                l, new_tree = None, None
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

    def search_and_promote(self, key):
        if key == self.key:
            self.weight += 1
            return self, True
        if key < self.key:
            if self.left is None:
                return self, False
            self.left, found = self.left.search_and_promote(key)
            if found and self.left.weight > self.weight:
                new_root = self.left
                self.left = new_root.right
                new_root.right = self
                return new_root, True
            return self, found
        else:
            if self.right is None:
                return self, False
            self.right, found = self.right.search_and_promote(key)
            if found and self.right.weight > self.weight:
                new_root = self.right
                self.right = new_root.left
                new_root.left = self
                return new_root, True
            return self, found

def main():
    N = 30000

    datasets = {
        "случайный":    [random.randint(0, N * 10) for _ in range(N)],
        "возрастающий": list(range(1, N + 1)),
    }

    for name, keys in datasets.items():
        queries = [random.choice(keys) for _ in range(N // 10)]

        print(f"{name} датасет")

        t0 = time.perf_counter()
        bst = Tree()
        for k in keys:
            bst.insert(k)
        bst_build = time.perf_counter() - t0

        t0 = time.perf_counter()
        bst_found = 0
        for k in queries:
            if bst.search(k) is not None:
                bst_found += 1
        bst_search = time.perf_counter() - t0

        t0 = time.perf_counter()
        sorted_q = sorted(queries)
        freq = Counter(sorted_q)
        t_sort_q = time.perf_counter() - t0

        t0 = time.perf_counter()
        sorted_keys = sorted(keys)
        t_sort_k = time.perf_counter() - t0

        t0 = time.perf_counter()
        treap = None
        for k in sorted_keys:
            w = freq.get(k, 1)
            treap = treap.add(k, w) if treap else Treap(k, w)
        treap_build = time.perf_counter() - t0

        treap_sort = t_sort_q + t_sort_k
        treap_total = treap_sort + treap_build

        t0 = time.perf_counter()
        treap_found = 0
        for k in queries:
            if treap is None:
                break
            treap, ok = treap.search_and_promote(k)
            if ok:
                treap_found += 1
        treap_search = time.perf_counter() - t0

        print(f"  BST:")
        print(f"построение:{bst_build:.4f} с")
        print(f"поиск {N // 10} ключей:{bst_search:.4f} с "
              f"(найдено {bst_found}/{N // 10})")
        print(f"Treap (оптимальный):")
        print(f"построение с сортировкой:{treap_total:.4f} с")
        print(f"поиск {N // 10} ключей:{treap_search:.4f} с "
              f"(найдено {treap_found}/{N // 10})")
        print()

if __name__ == "__main__":
    main()