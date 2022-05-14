class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ln, total = len(num), 0
        for i in range(ln):
            total += (10**(ln - i - 1))*num[i]
        total += k
        
        out = []
        while total > 0:
            out.append(total%10)
            total = total//10
        
        return out[::-1]