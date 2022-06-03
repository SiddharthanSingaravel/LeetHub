class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        status = True
        delta = arr[1] - arr[0]
        for ind in range(len(arr)-1):
            if delta != arr[ind + 1] - arr[ind]:
                status = False
                break
        return status