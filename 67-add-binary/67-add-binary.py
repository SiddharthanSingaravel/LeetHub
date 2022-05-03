class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a), int(b)
        
        def b2d(n):
            sum, i = 0, 0
            while n>0:
                temp = n%10
                sum += (2**i)*temp
                i +=1
                n = n//10
            return int(sum)
        
        total = b2d(a) + b2d(b)
        
        def d2b(n):
            out = ''
            if n == 0:
                out = '0'
            while n>0:
                temp = n%2
                out += str(temp)
                n = n//2
            out = out[::-1]
            return out
        
        output = d2b(total)
        return output
        