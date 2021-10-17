#How Many Numbers are Smaller than the Current Number ?

import collections

class Solution:
	def smallerNumbersThanCurrent(self, nums):
		c = collections.Counter(nums)
		for i in range(max(nums)+1):
			c[i] += c[i-1]
		return [c[i - 1] for i in nums]



#Main
# Test input:1 nums = [8,1,2,2,3]
nums = [6,5,4,8]
a = Solution()
res = a.smallerNumbersThanCurrent(nums)
print(res)