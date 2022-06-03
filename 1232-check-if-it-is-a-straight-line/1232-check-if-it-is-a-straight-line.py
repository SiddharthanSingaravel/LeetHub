class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        for ind in range(len(coordinates) - 2):
            # a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
            val = coordinates[ind:ind+3]
            det = val[0][0] * (val[1][1] - val[2][1]) + val[1][0] * (val[2][1] - val[0][1]) + val[2][0] * (val[0][1] - val[1][1])
            if det != 0:
                return False
                break
        
        return True