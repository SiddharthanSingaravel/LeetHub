class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 1
        if num < 2:
            return False
        
        for i in range(2,floor(num**0.5)+1):
            if num%i == 0:
                sum += i + num//i
        
        return sum==num
        