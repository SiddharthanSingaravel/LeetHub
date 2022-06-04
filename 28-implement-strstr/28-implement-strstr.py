class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        out = -1
        for ind in range(len(haystack)-len(needle) + 1):
            if haystack[ind:ind+len(needle)] == needle:
                out = ind
                break
        
        return out
            
            