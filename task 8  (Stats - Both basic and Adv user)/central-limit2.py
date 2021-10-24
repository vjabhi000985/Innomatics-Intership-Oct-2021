#Central Limit Distribution 2

from math import sqrt,erf

mu = 2.4 * 100
sigma = 2.0 * 10

def central_limit(x,mu,sigma):
    z = (x-mu)/sigma
    return 0.5*(1+erf(z/sqrt(2)))

print(round(central_limit(250,mu,sigma),4))
