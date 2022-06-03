class Solution:
def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
slope = (coordinates[0][1] - coordinates[1][1])/(coordinates[0][0] - coordinates[1][0])
status = True
for i in range(1, len(coordinates)-1):
delta = (coordinates[i][1] - coordinates[i+1][1])/(coordinates[i][0] - coordinates[i+1][0])
if delta!=slope:
status = False
break
return status