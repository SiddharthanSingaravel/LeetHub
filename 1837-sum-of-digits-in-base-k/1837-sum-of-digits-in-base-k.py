class Solution:
    def sumBase(self, n: int, k: int) -> int:
        out = 0
        while n > 0:
            out += (n%k)
            n = n//k
        return out