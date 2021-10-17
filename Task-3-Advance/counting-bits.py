#Counting Bits.

class Solution:
	def countBits(self,n):
		ans = [0] * (n+1)
		off = 0
		for i in range(1,n+1):
			if i & i-1 == 0:
				ans[i] = 1
				off = 0
			else:
				off += 1
				ans[i] = 1 + ans[off]
		return ans
#Main
n = int(input())
a = Solution()
res = a.countBits(n)
print(res)