class Solution:
    def minimumSum(self, num: int) -> int:
        res = list(map(int, str(num)))
        res.sort()
        total = res[0]*10 + res[2] + res[3] + res[1]*10
        return(total)