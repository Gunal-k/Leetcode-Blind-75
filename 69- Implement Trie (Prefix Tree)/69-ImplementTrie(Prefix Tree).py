class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

if __name__ == "__main__":
    # Your Trie object will be instantiated and called as such:
    obj = Trie()
    obj.insert("apple")
    print(obj.search("apple"))   # Returns True
    print(obj.search("app"))     # Returns False
    print(obj.startsWith("app")) # Returns True
    obj.insert("app")
    print(obj.search("app"))     # Returns True