#Maximum Product of Two Elements in an Array.

class Solution:
	def maxProduct(self,nums,l):
		n = nums
		n.sort()
		num1=num2 = 0
		sum1 = n[0]*n[1]
		sum2 = n[l-1] * n[l-2]

		if sum1 > sum2:
			num1 = n[0]
			num2 = n[1]
		else:
			num1 = n[l-2]
			num2 = n[l-1]
		print('{',num1,',',num2,'}')    #Finding out the no. of pairs for maximum product problem.
		res = (num1-1) * (num2-1)
		return res
#Main
call = Solution()
n = [1,5,4,5]
ans = call.maxProduct(n,len(n))
print(ans)