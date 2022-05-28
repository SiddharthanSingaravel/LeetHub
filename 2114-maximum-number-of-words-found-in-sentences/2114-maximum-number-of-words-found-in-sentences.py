class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        out = 0
        for i in sentences:
            if len(i.split()) > out: out = len(i.split())
        return(out)
        