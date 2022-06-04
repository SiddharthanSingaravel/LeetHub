class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def str2num(num):
            i, out = 0, 0
            while i < len(num):
                out += (10 ** (len(num) - i - 1))*(ord(num[i]) - 48)
                i += 1
            print (out)
            return out
                
        return str(str2num(num1) * str2num(num2))
        