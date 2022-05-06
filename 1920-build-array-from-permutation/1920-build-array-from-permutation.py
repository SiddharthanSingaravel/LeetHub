class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        out = []
        for index, i in enumerate(nums):
            out.append(nums[nums[index]])
        
        return out