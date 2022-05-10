import math
class Solution:
    def isThree(self, x: int) -> bool:

        ctr = 0 
        for i in range(1, x + 1):
            if x % i == 0:
                ctr+=1
        
        return True if ctr==3 else False