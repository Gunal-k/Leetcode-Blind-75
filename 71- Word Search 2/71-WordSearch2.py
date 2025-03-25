from typing import List

class TrieNode:
    def __init__(self):
        self.Children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.Children:
                cur.Children[c] = TrieNode()
            cur = cur.Children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        rows, cols = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visit or board[r][c] not in node.Children:
                return
            visit.add((r, c))
            node = node.Children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)
            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        return list(res)

if __name__ == "__main__":
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    words = ["oath", "pea", "eat", "rain"]
    solution = Solution()
    print(solution.findWords(board, words))