class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ctr = 0
        for ind, i in enumerate(nums):
            for j in nums[ind+1:]:
                if abs(i - j) == k:
                    ctr += 1
        
        return ctr
                    