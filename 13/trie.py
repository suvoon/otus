class TrieNode:
    __slots__ = ("children", "is_end")

    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self._traverse(word)
        return node is not None and node.is_end

    def startsWith(self, prefix):
        return self._traverse(prefix) is not None

    def _traverse(self, string):
        node = self.root
        for char in string:
            if char not in node.children:
                return None
            node = node.children[char]
        return node