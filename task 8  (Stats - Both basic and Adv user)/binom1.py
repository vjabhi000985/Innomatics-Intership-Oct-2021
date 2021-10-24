#Binomial Distribution 1

def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def combination(n,r):
    return fact(n)/(fact(r) * fact(n-r))

def binom(r,n,p):
    return combination(n,r) * p**r * (1-p)**(n-r)

l,r = list(map(float,input().split(" ")))
p = l/r

print(round(sum([binom(i,6,p/(1+p))for i in range(3,7)]),3))
