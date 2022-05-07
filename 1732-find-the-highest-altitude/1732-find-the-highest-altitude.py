class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        delta, out = 0, [0]
        for i in gain:
            delta += i
            out.append(delta)
        
        return (max(out))
        