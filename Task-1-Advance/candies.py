#Kids with the Greatest number of Candies Problem.

class Solution:
	def kidsWithCandies(self, candies, extraCandies):
		ans = []
		for i in range(len(candies)):
			if candies[i] >= max(candies) - extraCandies:
				ans.append(True)
			else:
				ans.append(False)
		return ans

#Main
candies = [2,3,5,1,3]
extraCandies = 3

a = Solution()
res = a.kidsWithCandies(candies,extraCandies)
print(res)
