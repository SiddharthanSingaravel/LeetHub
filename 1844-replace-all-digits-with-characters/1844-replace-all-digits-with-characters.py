class Solution:
    def replaceDigits(self, s: str) -> str:
        out = ''
        for ind, i in enumerate(s):
            if ind%2:
                out += chr(ord(s[ind - 1]) + int(i))
            else:
                out += i
        
        return out