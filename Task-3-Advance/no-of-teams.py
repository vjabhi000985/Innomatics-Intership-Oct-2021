#Count the Number of Teams.

class Solution:
	def numTeams(self,rating):
		res = 0
		for i in range(1,len(rating)-1):
			less,greater = [0]*2, [0]*2

			for j in range(len(rating)):
				if (rating[i] > rating[j]):
					less[i<j] += 1
				elif(rating[i] < rating[j]):
					greater[i<j] += 1
			res +=less[0]*greater[1] + greater[0]*less[1]
		return res
#Main
#rating = [2,5,3,4,1]
#rating = [2,1,3]
rating = [1,2,3,4]
n = Solution()
ans = n.numTeams(rating)
print(ans)