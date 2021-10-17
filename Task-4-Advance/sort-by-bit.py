#Sort Integers by The Number of 1 Bits.

class Solution:
	def sortByBits(self, nums):
		key = {}
		for i in nums:
			c = bin(i).count('1')
			if c not in key:
				key[c]=[i]
			else:
				key[c].append(i)
		res = []
		for i in sorted(key.keys()):
			res.extend(key[i])
		return res

#Main 
nums = [2,3,5,7,11,13,17,19]
a = Solution()
res = a.sortByBits(nums)
print(res)