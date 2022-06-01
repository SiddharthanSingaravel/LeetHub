class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        i = min(len(str1), len(str2))
        out = ''
        logic = len(str1) < len(str2)
        
        if logic:
            temp = str1
            str1 = str2
            str2 = temp
        
        del logic
        
        while i > 0 and str1[0] == str2[0]:
            if str1 == str2[:i] * int(len(str1)/len(str2[:i])) and str2 == str2[:i] * int(len(str2)/len(str2[:i])):
                out = str2[:i]
                break
            i -= 1
        
        return out
            
            