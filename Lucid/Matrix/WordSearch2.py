# recursive DFS + Trie
# time: O(m * n * 4^w), m = length, n = width, w = number of words
# space: O(n), n = number of keys in trie

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words: root.add_word(w)

        num_rows, num_cols = len(board), len(board[0])
        res = set()
        VISITED = '-1'

        def dfs(r, c, node, word):
            if not 0 <= r < num_rows or not 0 <= c < num_cols: return
            if board[r][c] == VISITED: return
            if board[r][c] not in node.children: return

            og_val = board[r][c]
            board[r][c] = VISITED
            node = node.children[og_val]
            word += og_val
            if node.is_word:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            board[r][c] = og_val

        for r in range(num_rows):
            for c in range(num_cols):
                dfs(r, c, root, "")

        return list(res)



