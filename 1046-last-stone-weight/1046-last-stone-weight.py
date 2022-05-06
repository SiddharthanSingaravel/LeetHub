class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            m1 = max(stones)
            stones.remove(m1)
            
            m2 = max(stones)
            stones.remove(m2)
            
            if abs(m1 - m2) > 0:
                stones.append(abs(m1-m2))
        
        return sum(stones)
            