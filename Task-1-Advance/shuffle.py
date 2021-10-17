#Shuffle the Array Problem.

class Solution(object):
	def shuffle(self, nums, n):
		l = []

		for i in range(n):
			l.append(nums[i])
			l.append(nums[i+n])
		return l

#Main
nums = [2,5,1,3,4,7]
n = 3
a = Solution()
res = a.shuffle(nums,n)
print(res)