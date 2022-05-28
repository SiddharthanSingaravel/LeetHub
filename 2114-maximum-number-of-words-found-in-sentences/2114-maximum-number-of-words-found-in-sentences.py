class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        out = []
        for i in sentences:
            out.append(len(i.split()))
        return(max(out))
        