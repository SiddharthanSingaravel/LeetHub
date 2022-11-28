class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap = {}
        for i in range(len(heights)):
            hashmap[heights[i]] = names[i]
        
        sorted = list(hashmap.keys())
        sorted.sort(reverse = True)
        out = []
        for i in sorted:
            out.append(hashmap[i])
        return out