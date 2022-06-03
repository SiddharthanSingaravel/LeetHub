class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        out = word
        for ind, i in enumerate(word):
            if i == ch:
                out = word[:ind+1]
                out = out[::-1]
                out += word[ind+1:]
                break
        return out