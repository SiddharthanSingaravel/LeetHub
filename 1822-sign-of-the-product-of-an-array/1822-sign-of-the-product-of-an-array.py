class Solution:
    def arraySign(self, nums: List[int]) -> int:
        val = reduce(lambda x, y: x*y, nums)
        if val > 0: return 1
        elif val < 0: return -1
        else: return 0