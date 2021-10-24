#Central Limit Theorem 1

from math import sqrt,erf

x = int(input())
n = int(input())
mu = int(input())
sigma = int(input())

mu_sum = n * mu
sigma_sum = sqrt(n) * sigma

def central_limit(x,mu,sigma):
    z = (x-mu)/sigma
    return 0.5*(1+erf(z/sqrt(2)))

print(round(central_limit(x,mu_sum,sigma_sum),4))
