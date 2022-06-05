def squarer(n):
out = 0
while n > 0:
temp = n%10
out += temp**2
n = n//10
if out != 1:
squarer(out)
return squarer(n)