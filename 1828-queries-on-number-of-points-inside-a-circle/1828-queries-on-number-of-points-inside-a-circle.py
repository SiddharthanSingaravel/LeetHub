class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        out = []
        for i in queries:
            temp = 0
            for j in points:
                if ((i[0] - j[0])**2 + (i[1] - j[1])**2) <= (i[2])**2:
                    temp += 1
            out.append(temp)
        
        return out