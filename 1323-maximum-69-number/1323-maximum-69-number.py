class Solution:
    def maximum69Number (self, num: int) -> int:
        res = list(map(int, str(num)))
        for ind, i in enumerate(res):
            if i == 6:
                res[ind] = 9
                break
        print(res)
        
        s = [str(i) for i in res]
        res = int("".join(s))
        
        return(res)