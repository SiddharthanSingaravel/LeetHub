class Solution:
def countTriples(self, n: int) -> int:
out = []
ctr = 0
for i in range(1, n+1):
out.append(i**2)
for ind_i, i in enumerate(out[:len(out)-1]):
for ind_j, j in enumerate(out[ind_i+1:]):
if i +j in out:
ctr += 1
return (ctr*2)