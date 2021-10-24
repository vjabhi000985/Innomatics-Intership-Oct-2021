#Central Limit Theorem 3
from math import sqrt,erf

mu = 500
sigma = 80

mu_sum = mu
sigma_sum = sigma/(100**0.5)

res1 = mu_sum - (1.96*sigma_sum)
res2 = mu_sum + (1.96*sigma_sum)

print(round(res1,2))
print(round(res2,2))
