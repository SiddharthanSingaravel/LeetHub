class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ctr = 0
        for ind, i in enumerate(nums[:len(nums)-1]):
            for j in nums[ind+1:]:
                if i == j:
                    ctr += 1
        
        return ctr