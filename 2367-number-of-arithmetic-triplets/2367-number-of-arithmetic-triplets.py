class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ctr = 0
        for i in range(len(nums) - 1):
            if ((nums[i] + diff) in nums) & ((nums[i] - diff) in nums):
                ctr += 1
        return ctr
    