class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ctr = 0
        for i in words:
            if i[:len(pref)] == pref:
                ctr += 1
        
        return ctr
        