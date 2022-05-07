class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        out = []
        for i in rectangles:
            out.append(min(i))
        
        return(out.count(max(out)))