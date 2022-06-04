class Solution:
    def calPoints(self, ops: List[str]) -> int:
        out = []
        for i in ops:
            if i == 'C':
                out.pop()
            elif i == 'D':
                out.append(out[-1]*2)
            elif i == '+':
                out.append(out[-1] + out[-2])
            else:
                out.append(int(i))
        
        print(out)
        return sum(out)