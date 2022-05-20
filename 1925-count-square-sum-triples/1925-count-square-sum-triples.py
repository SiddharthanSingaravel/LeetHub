class Solution:
    def countTriples(self, n: int) -> int:     
        ctr = 0
        for i in range(1,n):
            for j in range(i+1,n+1):
                x = sqrt(i**2 + j**2)
                if x <= n and int(x) == x:
                    ctr += 1

        
        return (ctr*2)
                
        