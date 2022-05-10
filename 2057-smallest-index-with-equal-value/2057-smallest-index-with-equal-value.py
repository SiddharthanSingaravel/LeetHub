class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        delta = -1
        for i in range(len(nums)):
            if i%10 == nums[i]:
                delta = i
                break
        
        return delta