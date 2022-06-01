class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = [nums[0]]
        for i in nums[1:]:
            out.append(out[-1] + i)
        
        return out