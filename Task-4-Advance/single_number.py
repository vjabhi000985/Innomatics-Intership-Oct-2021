#Leetcode's Single Number Problem.

class Solution:
	def singleNumber(self, nums):
		ans = 0
		for i in range(len(nums)):
			ans ^= nums[i]
		return ans

#Main
nums = [4,1,2,1,2]
a = Solution()
res = a.singleNumber(nums)
print(res)
