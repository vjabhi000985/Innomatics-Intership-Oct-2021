#Substract the Product and Sum of Digits of an Integer.

class Solution:
	def subtractProductAndSum(self,n):
		x = n
		product = 1
		add = 0
		while x > 0:
			product *= (x % 10)
			add += (x % 10)
			x //= 10
		return product - add

#Main

n = int(input())
a = Solution()
res = a.subtractProductAndSum(n)
print(res)
