class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        inputs, ctr = heights, 0
        heights = sorted(heights)
        for ind in range(len(heights)):
            if inputs[ind] != heights[ind]:
                ctr += 1
        
        print(heights, inputs)
        return ctr

        
      