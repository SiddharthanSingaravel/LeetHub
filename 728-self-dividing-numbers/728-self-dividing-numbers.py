class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr = []
        
        for i in range(left, right+1):
            temp, out = i, 0
            
            while temp > 0:
                ind = temp%10
                if ind == 0 or i%ind != 0:
                    out += 1
                    break
                temp = temp//10
            
            if out == 0:
                arr.append(i)
        
        return arr
                    
                    