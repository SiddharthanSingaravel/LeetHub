class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        ctr = 0
        for i in range(len(arr) - 2):
            if arr[i]%2 != 0 and arr[i+1]%2 != 0 and arr[i+2]%2 != 0:
                ctr = 1
                break
            else:
                ctr = 0
        
        return True if ctr == 1 else False