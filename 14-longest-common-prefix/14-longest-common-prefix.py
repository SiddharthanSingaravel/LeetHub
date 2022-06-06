class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = ''
        i, ln = 0, min([len(i) for i in strs])
        while i < ln:
            ctr = 0
            for ind in strs:
                if ind[:i+1] == strs[0][:i+1]:
                    ctr += 1
                else:
                    break
                    
            if ctr == len(strs):
                out = strs[0][:i+1]
                print(out)
            i += 1
        
        return out
        