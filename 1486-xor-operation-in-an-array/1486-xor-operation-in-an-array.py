import functools
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = list(range(start,start + 2* n,2))
        return (functools.reduce(lambda a, b: a ^ b, nums))
        