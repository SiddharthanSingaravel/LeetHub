class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        minner = nums[0]
        for i in nums[1:]:
            if minner > i:
                minner = i
        
        dsum = 0
        while minner > 0:
            dsum += minner%10
            minner = minner//10
        
        if dsum%2:
            return 0
        else:
            return 1
            
            
            