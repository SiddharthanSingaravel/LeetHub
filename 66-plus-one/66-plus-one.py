class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ln = len(digits)
        total = 0
        
        for i in range(ln):
            total += digits[i] * (10 ** (ln - i - 1))
        total +=1
        
        out = [int(i) for i in str(total)]
            
        return (out)