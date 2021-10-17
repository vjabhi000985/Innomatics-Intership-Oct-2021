#Problem: Running Sum of 1D array.

class Solution:
	def runningSum(self,nums):
		s = 0
		List = []
		for i in nums:
			s = i + s
			List.append(s)
		return List

#Main 
a = Solution()
nums = [1,3,4,6]
res=a.runningSum(nums)
print(res)