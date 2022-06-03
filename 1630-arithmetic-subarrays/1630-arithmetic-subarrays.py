import itertools
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        out = []
        for ind in range(len(l)):
            delta = True
            arr = nums[l[ind]:r[ind]+1]
            arr.sort()
            for ind in range(len(arr)-2):
                if arr[ind + 1] * 2 != arr[ind] + arr[ind+2]:
                    delta = False
                    break
            out.append(delta)
        
        return out

                
        