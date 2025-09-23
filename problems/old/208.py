class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}


class Trie:

    def __init__(self):
        self.root = Node("")

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(0, len(word)):
            c = word[i]
            child = node.children.get(c)
            if child:
                node = child
                continue

            node.children[c] = Node(c)
            node = node.children[c]
        # Singal a word eneded here
        node.children["$"] = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            node = node.children.get(c)
            if not node:
                return False
        # find exact word ending
        return bool(node.children.get("$"))

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            node = node.children.get(c)
            if not node:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


trie = Trie()
print(trie.insert("apple"))
print(trie.search("apple"))  #  // return True
print(trie.search("app"))  #     // return False
print(trie.startsWith("app"))  # // return True
print(trie.insert("app"))  #
print(trie.search("app"))  #   // return True
