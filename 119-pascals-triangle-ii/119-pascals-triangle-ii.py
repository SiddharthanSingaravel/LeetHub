class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def fact(n):
            res = 1
            for k in range(2, n+1):
                res *= k
            return res
        
        def ncr(n, r):
            return int(fact(n)/(fact(r)*fact(n-r)))
        
        out = []
        for j in range(rowIndex + 1):
            out.append(ncr(rowIndex + 1 - 1, j))
        
        return out