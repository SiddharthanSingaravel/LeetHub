class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def summer(text):
            out, i = 0, 0
            while i < len(text):
                out += (10 ** (len(text) - i - 1)) * (ord(text[i]) - 97) 
                print(out)
                i += 1
            return out
        
        return (summer(firstWord) + summer(secondWord)) == summer(targetWord)
        
        
        
            