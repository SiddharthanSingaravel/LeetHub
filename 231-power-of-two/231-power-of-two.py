class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        status = True
        while n > 1:
            if n%2 != 0:
                status = False
                break
            else:
                n = n//2
        
        return status if n>=1 else False
            