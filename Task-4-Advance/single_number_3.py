#Leetcode's Single Number 3 Problem.

class Solution:
	def singleNumber(self, nums):
		xy = 0
		for i in nums: xy ^= i
		xy &= -xy

		res = [0]*2
		for i in nums:
			if (xy & i) == 0:
				res[0] ^= i
			else:
				res[1] ^= i
		return res
#Main
nums = [1,2,1,3,2,5]
a = Solution()
ans = a.singleNumber(nums)
print(ans)
