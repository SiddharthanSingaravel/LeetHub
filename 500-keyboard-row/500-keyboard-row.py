class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        out = [0, 0, 0]
        arr, ctr = [], 0
        for i in words:
            for j in i:
                if j.lower() in "qwertyuiop": out[0] += 1
                elif j.lower() in "asdfghjkl": out[1] += 1
                else: out[2] += 1
            if out.count(0) == 2:
                arr.append(i)
            out = [0, 0 ,0]
        
        return arr