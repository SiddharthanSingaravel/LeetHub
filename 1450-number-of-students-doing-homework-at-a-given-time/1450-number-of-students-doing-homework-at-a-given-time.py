class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ctr = 0
        for ind in range(len(endTime)):
            if queryTime >= startTime[ind] and queryTime <= endTime[ind]:
                ctr += 1
        
        return ctr
        