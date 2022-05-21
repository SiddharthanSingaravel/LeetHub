class Solution:
    def freqAlphabets(self, s: str) -> str:
        out = ''
        i = len(s)-1
        while i > -1:
            if s[i] == '#':
                temp = int(s[i-2] + s[i-1]) + 96
                i -= 3
            else:
                temp = int(s[i]) + 96
                i -= 1
            out += chr(temp)
        
        return out[::-1]