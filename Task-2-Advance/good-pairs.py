#Number of Good Pairs.
#Given an array of integers nums, returns the number of good pairs.

class Solution:
	def numIdenticalPairs(self,nums):
		count = 0
		for i in range(len(nums)):
			for j in range(i+1,len(nums)):
				if nums[i]  == nums[j]:
					count += 1
		return count

#Main
nums = [1,2,3,1,1,3]
a = Solution()
res = a.numIdenticalPairs(nums)
print(res)