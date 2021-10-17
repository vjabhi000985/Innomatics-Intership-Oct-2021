#Find Numbers with Even Number of Digits.

class Solution:
	def findNumber(self, nums):
		c = 0
		num = map(str,nums)
		for i in num:
			if len(i) % 2 == 0:
				c += 1
		return c

#Main

nums = [12,345,2,6,7896]
a = Solution()
res = a.findNumber(nums)
print(res)