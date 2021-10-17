#Defanging an IP Address.

class Solution:
	def defangIPaddr(self,address):
		s = address
		s = s.split(".")
		return "[.]".join(s)

#Main
address = "198.168.4.1"
a = Solution()
res = a.defangIPaddr(address)
print(res)
