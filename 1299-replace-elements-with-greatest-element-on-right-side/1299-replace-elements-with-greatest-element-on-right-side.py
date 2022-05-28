class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        out = []
        for ind in range(len(arr)-1):
            out.append(max(arr[ind+1:]))
        
        out.append(-1)
        return(out)
        