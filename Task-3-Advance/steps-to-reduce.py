#Numbers of Steps to Reduce a Number to Zero.

class Solution:
	def numberOfSteps(self, num):
		n = num
		ans = 0
		while n > 0:
			if n % 2:
				n -= 1
			else:
				n /= 2
			ans += 1
		return ans

#Main
n1 = int(input())
a = Solution()
result = a.numberOfSteps(n1)
print(result)

