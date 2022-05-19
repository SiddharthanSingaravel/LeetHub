class Solution:
    def toLowerCase(self, s: str) -> str:
        out = ''
        for i in s:
            if ord(i) >= 65 and ord(i) <= 90:
                out += chr(ord(i) + 32)
            else:
                out += i
        
        return out