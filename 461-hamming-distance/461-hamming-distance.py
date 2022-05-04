class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        sum = 0
        def d2b(n):
            return str(format(n,"031b"))
        
        x,y = d2b(x), d2b(y)
        
        for i in range(0,31):
            if x[i] != y[i]:
                sum += 1
        
        return sum
            
            
        
        