#Here is given a list of N natural numbers. The length of list i.e. N=10.
#The problem is to find out the missing and repeating number.

list = [ 1,2,3,3,4,5,6,7,8,10]
# list = [1,2,3,4,4] as test case
y = 0 # Base Value
z = 9 # Answer Value

repeat = 0 # Variable for computation of the repeating element.

# Function for finding out the missing number.
def missing(list,y,z):
   for x in list:
      if y+(x-1)==z:
         print("The missing no is:" + str(x-1))

# Function for finding out the repeatiing value.
def repeation(list):
   for i in range(1,len(list)):
      for j in range(1,i):
         if list[i]==list[j]:
            repeat = list[i]
            print("The repeating element is:",repeat)

missing(list,y,z)
repeation(list)

# The output is below.
# The missing mo is: 9
# The repeating element is: 3