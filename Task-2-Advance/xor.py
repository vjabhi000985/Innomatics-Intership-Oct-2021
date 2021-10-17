#XOR Operation in an Array.

class Solution:
	def xorOperation(self,n,start):
		res = 0

		for i in range(n):
			res ^= start + 2 * i
		return res

#Main
n = int(input())
start = int(input())

a = Solution()
ans = a.xorOperation(n,start)
print(ans)