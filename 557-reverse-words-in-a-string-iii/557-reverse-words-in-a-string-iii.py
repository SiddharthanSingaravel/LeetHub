class Solution:
    def reverseWords(self, s: str) -> str:
        arr, out = list(s.split()), ''
        for ind, i in enumerate(arr):
            temp = i[::-1]
            if ind < len(arr) - 1:
                out += (temp + ' ')
            else:
                out += temp
        
        return out