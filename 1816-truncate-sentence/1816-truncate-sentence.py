class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        out = ''
        for i in s.split(' ')[:k]:
            out += i
            out += ' '
            
        return out[0: len(out)-1]