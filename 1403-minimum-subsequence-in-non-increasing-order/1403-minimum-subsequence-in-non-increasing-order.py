class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse = True)
        for i in range(len(nums[:-1])):
            print(nums[: i + 1], nums[i + 1:])
            if sum(nums[:i+1]) > sum(nums[i + 1:]):
                return nums[:i+1]
        return nums
        