#Leetcode's Subsets Problem.
#Given an integer array nums of unique elements, returns all possible subsets(the power set). 
class Solution:
	def subsets(self, nums):
		s = nums
		n = len(s)
		return[[s[j] for j in range(n) if i & 1 << j] for i in range(2**n)]
#Main
nums = [1,2,3]
a = Solution()
res = a.subsets(nums)
print(res)