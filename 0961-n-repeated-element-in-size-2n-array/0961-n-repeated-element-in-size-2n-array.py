class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        container = []
        for i in nums:
            if i not in container:
                container.append(i)
            else:
                return i
                break
        