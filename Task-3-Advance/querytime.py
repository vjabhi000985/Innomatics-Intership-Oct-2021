#Number of Students Doing Homework at a Given Time.

class Solution:
	def busyStudent(self,startTime,endTime,queryTime):
		ans = 0
		for i in range(len(startTime)):
			if startTime[i] <= queryTime and queryTime <= endTime[i]:
				ans += 1
			else:
				ans = 0
		return ans

#Main
s = [1,2,3,4]
e = [2,4,5,7]
q = 9

a = Solution()
res = a.busyStudent(s,e,q)
print(res)
