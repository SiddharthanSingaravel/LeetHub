class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        out = ''
        for i in words:
            if i == i[::-1]:
                out = i
                break
        
        return out
                
        