#Pearson Correlation Coefficient I

n = int(input())
x = list(map(float,input().strip().split()))
y = list(map(float,input().strip().split()))

mu_x = sum(x) / n
mu_y = sum(y) / n

std_x = (sum([(i - mu_x)**2 for i in x])/n)**0.5
std_y = (sum([(i - mu_y)**2 for i in y])/n)**0.5

covariance = (sum([(x[i] - mu_x)*(y[i] - mu_y)for i in range(n)]))

correlation_coefficient = covariance / (n * std_x * std_y)

print(round(correlation_coefficient,3))
