class Solution:
def rearrangeArray(self, nums: List[int]) -> List[int]:
pos, neg, out = [], [], []
for ind in nums:
if ind < 0:
neg.append(ind)
else:
pos.append(ind)
print(neg, pos)
i = 0
while i < len(neg):
out.append(pos[i])
out.append(neg[i])
i += 1
return(out)