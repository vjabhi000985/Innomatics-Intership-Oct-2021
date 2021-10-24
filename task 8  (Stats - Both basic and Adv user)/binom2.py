#Binomial Distribution 2

def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def comb(n,r):
    return fact(n)/(fact(r) * fact(n-r))


n,p = list(map(float,input().split(" ")))

print(round(sum([comb(p,i)*(n / 100)**i *((100-n)/100)**(p-i)for i in range(0,3)]),3))
print(round(sum([comb(p,i)*(n / 100)**i *((100-n)/100)**(p-i)for i in range(2,11)]),3))
