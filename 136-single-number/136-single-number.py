class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for index, i in enumerate(nums):
            if nums.count(i) == 1:
                return i
                break
        