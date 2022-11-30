class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashmap = []
        for i in arr:
            if arr.count(i) < 2 and i not in hashmap:
                hashmap.append(i)
        
        if k <= len(hashmap):
            return hashmap[k - 1]
        else:
            return ""
            