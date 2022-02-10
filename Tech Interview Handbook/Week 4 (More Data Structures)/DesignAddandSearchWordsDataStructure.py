# Trie (Prefix Tree)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    # Time: O(M), where M is word length.
    # Space: O(M)
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    # Time: O(M) for words without dots, where M is word length.
    #       O(26^M) for dotted words, where M is word length, eg. ".....z"
    # Space: O(1) for words without dots, O(M) for words with dots bc of recursion stack
    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                c = word[i]

                if c == '.':
                    for child in curr.children.values():
                        if dfs(i + 1, child): return True
                    return False
                else:
                    if c not in curr.children: return False
                    else: curr = curr.children[c]
            return curr.word

        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)