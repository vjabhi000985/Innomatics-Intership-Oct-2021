#Normal Distribution 2

from math import sqrt,erf

mean,std = 70,10
#res = lambda x: 0.5 * (1 + math.erf(x-mean)/(std * (2 ** 0.5)))
def normal(x,m,s):
    z = (x-m)/(s*sqrt(2))
    return (1 + erf(z))/2

print(round(100-normal(80,mean,std)*100,2))
print(round(100-normal(60,mean,std)*100,2))
print(round(normal(60,mean,std)*100,2))

