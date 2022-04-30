class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        out = []
        for i in arr1:
            ctr = 0
            for j in arr2:
                if abs(i-j) <= d:
                    ctr +=1
            out.append(ctr)
        
        return(out.count(0))
        
                