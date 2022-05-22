class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxc, out = max(candies), []
        for i in candies:
            out.append(i + extraCandies >= maxc)
            
        return out
                
        