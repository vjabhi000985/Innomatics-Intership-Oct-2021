#Multiple Linear Regression

from sklearn.linear_model import LinearRegression
m,n = map(int,input().split())
x,y = [],[]
for i in range(n):
    vals=map(float,input().split())
    x.append(vals[:-1])
    y.append(vals[-1])

q = int(input())
test=[]
for i in range(q):
    vals=map(float,raw_input().split())
    test.append(vals)

reg = LinearRegression()
reg.fit(x,y)

pred = reg.predict(test)
for i in pred:
    print(i)
