class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num))>1:
            total = 0
            while num > 0:
                total += num%10
                num = num//10
            num = total
        
        return num