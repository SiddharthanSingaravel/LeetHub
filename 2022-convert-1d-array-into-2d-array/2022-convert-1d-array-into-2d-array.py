class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        out = []
        if m * n == len(original):
            i = 0
            while len(out) < m:
                out.append(original[i:i+n])
                i += n
        
        return out