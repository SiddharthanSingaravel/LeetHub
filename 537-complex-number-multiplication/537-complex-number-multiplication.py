class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.replace('i','')
        num2 = num2.replace('i','')
        n1, n2 = num1.split('+'), num2.split('+')
        real = int(n1[0]) * int(n2[0]) - int(n1[1]) * int(n2[1])
        img = int(n1[1])*int(n2[0]) + int(n1[0])*int(n2[1])
        return (str(real) + '+' + str(img) + 'i')