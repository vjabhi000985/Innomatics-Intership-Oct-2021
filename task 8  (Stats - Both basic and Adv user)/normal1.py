#Normal Distribution 1

from math import sqrt,erf

def normal(x,m,s):
    z = (x-m)/(s*sqrt(2))
    return (1 + erf(z))/2

m = 20
s = 2
print(round(normal(19.5,m,s),3))
print(round(normal(22,m,s)-normal(20,m,s),3))
