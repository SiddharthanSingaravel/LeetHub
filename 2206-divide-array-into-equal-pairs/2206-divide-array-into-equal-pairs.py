class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        arr = set(nums)
        out, ctr = [], 0
        for i in arr:
            out.append(nums.count(i))
        for j in out:
            if j%2 == 0:
                ctr += 1
        
        return ctr == len(out)
        