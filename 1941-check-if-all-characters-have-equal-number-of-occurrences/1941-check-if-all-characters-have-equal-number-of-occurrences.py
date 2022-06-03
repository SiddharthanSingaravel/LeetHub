class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        stringer, out = set(s), []
        for i in stringer:
            out.append(s.count(i))
        out = set(out)
        return len(out) == 1
        