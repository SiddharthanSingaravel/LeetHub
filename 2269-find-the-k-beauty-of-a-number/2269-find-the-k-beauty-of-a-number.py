class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        string = str(num)
        ctr = 0
        for i in range(len(string)-k+1):
            if int(string[i:i+k])!=0 and num%int(string[i:i+k])==0:
                ctr += 1
        
        return ctr
        