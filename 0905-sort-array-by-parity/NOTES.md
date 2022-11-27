ind = 0
even, odd = [], []
while ind < len(nums):
if nums[ind]%2:
odd.append(nums[ind])
else:
even.append(nums[ind])
return (even + odd)