class Solution:
    def isAnagram(self, s: str, t: str) -> str:
        wordmap = {'a': 2, 'b':3, 'c':5, 'd':7, 'e':11, 'f':13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k':31, 'l': 37, 'm': 41, 'n': 43, 'o': 47,
                  'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 77, 'w': 83, 'x': 97, 'y': 89, 'z': 79}
        out1 = out2 = 1
        for i in s:
            out1 *= wordmap[i]
        for j in t:
            out2 *= wordmap[j]
            
        return out1 == out2