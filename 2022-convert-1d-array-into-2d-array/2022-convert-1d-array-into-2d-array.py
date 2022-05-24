class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        out = []
        if m * n == len(original):
            for i in range(0, len(original), n):
                out.append(original[i:i+n])
        
        return out