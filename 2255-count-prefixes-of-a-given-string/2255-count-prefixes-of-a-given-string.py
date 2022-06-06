class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        out = 0
        for word in words:
            if word == s[:len(word)]:
                out += 1
        return out
        