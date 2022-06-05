class Solution:
    def getLucky(self, s: str, k: int) -> int:
        out, j = '', 0
        for i in s: out += str(ord(i) - ord('a') + 1)
        out = int(out)
        while j < k:
            total = 0
            while out > 0:
                total += out%10
                out = out//10
            out = total
            j += 1
        
        return out
            
        