import math
class Solution:
    def isThree(self, x: int) -> bool:

        ctr = 1 
        for i in range(1, x//2 + 1):
            if x % i == 0:
                ctr+=1
        
        return ctr==3