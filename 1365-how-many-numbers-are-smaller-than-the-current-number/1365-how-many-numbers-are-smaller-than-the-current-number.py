class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        out = []
        for i in nums:
            ctr = 0
            for j in nums:
                if j < i:
                    ctr +=1
            
            out.append(ctr)
        return out