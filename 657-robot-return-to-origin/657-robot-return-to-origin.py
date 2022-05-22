class Solution:
    def judgeCircle(self, moves: str) -> bool:
        directions = {'R': 0, 'L': 0, 'U': 0, 'D': 0}
        for i in moves:
            directions[i] += 1
        
        out = list(directions.values())
        return (out[0] - out[1] == 0 and out[2] - out[3] == 0)