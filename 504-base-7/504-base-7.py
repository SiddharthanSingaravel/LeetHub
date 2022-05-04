class Solution:
    def convertToBase7(self, num: int) -> str:
        out = ''
        neg = False
        store = num
        
        if num < 0:
            neg = True
        num = abs(num)
        
        while num >0:
            temp = num%7
            out += str(temp)
            num = num//7
        
        out = out[::-1]
        if neg == True:
            out = '-' + out
        
        if store != 0:
            return out
        else:
            return '0'
        