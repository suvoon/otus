import random
import sys
import time

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

def main():
    sys.setrecursionlimit(200000)

    N = 30000

    random_keys = [random.randint(0, N * 10) for _ in range(N)]
    ascending_keys = list(range(1, N + 1))

    tree_random = Tree()
    tree_ascending = Tree()

    t0 = time.perf_counter()
    for k in random_keys:
        tree_random.insert(k)
    t1 = time.perf_counter()
    print(f"Вставка {N} случайных ключей:{t1 - t0:.4f} с")

    t0 = time.perf_counter()
    for k in ascending_keys:
        tree_ascending.insert(k)
    t1 = time.perf_counter()
    print(f"Вставка {N} возрастающих ключей:{t1 - t0:.4f} с")
    print()

    search_keys = [random.choice(random_keys) for _ in range(N // 10)]
    t0 = time.perf_counter()
    found_random = sum(1 for k in search_keys if tree_random.search(k) is not None)
    t1 = time.perf_counter()
    print(f"Поиск {N // 10} ключей в случайном дереве:"
          f"{t1 - t0:.4f} с, найдено {found_random}/{N // 10}")

    search_keys_asc = [random.choice(ascending_keys) for _ in range(N // 10)]
    t0 = time.perf_counter()
    found_asc = sum(1 for k in search_keys_asc if tree_ascending.search(k) is not None)
    t1 = time.perf_counter()
    print(f"Поиск {N // 10} ключей в возрастающем дереве: "
          f"{t1 - t0:.4f} с, найдено {found_asc}/{N // 10}")
    print()

    remove_keys_random = random.sample(random_keys, N // 10)
    t0 = time.perf_counter()
    for k in remove_keys_random:
        tree_random.remove(k)
    t1 = time.perf_counter()
    print(f"Удаление {N // 10} ключей в случайном дереве:{t1 - t0:.4f} с")

    remove_keys_asc = random.sample(ascending_keys, N // 10)
    t0 = time.perf_counter()
    for k in remove_keys_asc:
        tree_ascending.remove(k)
    t1 = time.perf_counter()
    print(f"Удаление {N // 10} ключей в возрастающем дереве:{t1 - t0:.4f} с")

if __name__ == "__main__":
    main()