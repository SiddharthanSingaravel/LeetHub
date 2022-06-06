class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ctr = 0
        jewel = list(set(jewels))
        for i in stones:
            if i in jewel:
                ctr += 1
        return ctr