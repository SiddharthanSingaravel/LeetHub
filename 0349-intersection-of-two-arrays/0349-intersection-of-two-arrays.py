class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        for i in set(nums2):
            if i in nums1:
                out.append(i)
        return out