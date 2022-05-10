class Solution:
    def countEven(self, num: int) -> int:
        returner = 0
        for i in range(2,num+1):
            out = 0
            temp = i
            while temp > 0:
                out += temp%10
                temp = temp//10
            if out%2==0: returner += 1
        
        return returner
        
            