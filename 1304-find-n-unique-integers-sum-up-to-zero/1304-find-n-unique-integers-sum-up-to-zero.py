class Solution:
    def sumZero(self, n: int) -> List[int]:
        t = []
        for i in range(1,n):
            t.append(i)
        
        t.append(-1 * sum(t))
        return t