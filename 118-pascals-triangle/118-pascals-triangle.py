class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        global output
        output = []
        out = 1
        
        def fact(n):
            res = 1
            for k in range(2, n + 1):
                res = res * k
            return int(res)

        def ncr(n, r):
            return int(fact(n) / (fact(r) * fact(n - r)))

        out=[]
        for i in range(1, numRows + 1):
            out1=[]
            for j in range(i):
                a = ncr(i - 1, j)
                out1.append(a)
            out.append(out1)

        return out
        