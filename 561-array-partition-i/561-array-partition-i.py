class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i, total = 0, 0
        while i < len(nums):
            total += nums[i]
            i += 2
        return total