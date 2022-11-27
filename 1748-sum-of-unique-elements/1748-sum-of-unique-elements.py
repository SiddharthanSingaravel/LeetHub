class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        container = {}
        out = 0
        
        for i in nums:
            if i not in container.keys():
                container[i] = 1
            else:
                container[i] += 1
        
        for i in container:
            if container[i] == 1:
                out += i
        
        return out
            
        