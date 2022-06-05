class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, right, equal = [], [], []
        for ind in nums:
            if ind < pivot:
                left.append(ind)
            elif ind == pivot:
                equal.append(ind)
            else:
                right.append(ind)
        
        return left + equal + right