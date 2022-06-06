class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        delta = releaseTimes[0]
        out = [releaseTimes[0]]
        for i in releaseTimes[1:]:
            out.append(i - delta)
            delta = i
        print(out)
        largest_index = [ind for ind, i in enumerate(out) if i == max(out)]
        print(largest_index)
        start = 'a'
        for i in largest_index:
            print(ord(keysPressed[i]), i, start)
            if ord(keysPressed[i]) >= ord(start):
                start = keysPressed[i]
        
        return start