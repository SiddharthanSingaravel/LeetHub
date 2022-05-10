class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x = min(nums)
        y = max(nums)
        while (y - x) > 1 and x!=1 :
            y = y - x
            if y < x:
                temp = x
                x = y
                y = temp
                
        return x if y%x==0 else 1
            
    
        
            
        
        