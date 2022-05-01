class Solution:
    def fib(self, n: int) -> int:
        fibbie = [0,1]
        
        for i in range(2, n+1):
            fibbie.append(fibbie[i-1] + fibbie[i-2])
        
        if n == 0:
            return(0)
        else:
            return(fibbie[n-1] + fibbie[n-2])
       