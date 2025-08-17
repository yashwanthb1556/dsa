class TrieNode:
    def __init__(self):
        self.children = {}
        self.flag = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.cnt = 0

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
                self.cnt += 1
            node = node.children[char]
        node.flag = True
        return self

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.flag

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    @property
    def length(self):
        return self.cnt


trie = Trie()
trie.insert("leetcode")
print(trie.search("code"))
