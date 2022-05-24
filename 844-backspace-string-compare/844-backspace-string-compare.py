class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def compare(s):
            out = []
            for ind, i in enumerate(s):
                if i != '#':
                    out.append(i)
                elif len(out) > 0 and i == '#':
                    out.pop()
            return out
        
        a, b = compare(s), compare(t)
        print(a,b)
        return a == b
        