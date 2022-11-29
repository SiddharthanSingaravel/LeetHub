class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        hashmap, out = {}, [0, 0]
        print(out)
        for i in list(set(nums)):
            hashmap[i] = nums.count(i)
        
        for j in hashmap.values():
            print(j/2, j%2, j//2)
            out[0] += j//2
            out[1] += j%2
       
        return out
            