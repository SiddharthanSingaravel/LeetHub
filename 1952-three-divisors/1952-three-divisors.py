import math
class Solution:
    def isThree(self, x: int) -> bool:

        listx = []
        for i in range(1, x + 1):
            if x % i == 0:
                listx.append(i)
        
        return True if len(listx)==3 else False