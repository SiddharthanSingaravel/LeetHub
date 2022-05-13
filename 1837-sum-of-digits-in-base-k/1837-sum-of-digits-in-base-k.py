class Solution:
    def sumBase(self, n: int, k: int) -> int:
        out = []
        while n > 0:
            out.append(n%k)
            n = n//k
        return sum(out)