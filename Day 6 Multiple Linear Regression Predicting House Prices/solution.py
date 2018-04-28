import pandas as pd
from sklearn.linear_model import LinearRegression


F_N = input().split(" ")
F = int(F_N[0])
N = int(F_N[1])

data = []
for i in range(0, N):
    line = input().split(" ")
    data.append(tuple(map(float, line)))
   
labels = ["feature_{}".format(f) for f in range(0, F)]
labels.append("price")
df = pd.DataFrame.from_records(data, columns=labels)

Y_train = df['price']
X_train = df
del X_train['price']

model = LinearRegression()
model.fit(X_train, Y_train)


T = int(input())
data_test = []
for i in range(0, T):
    line = input().split(" ")
    data_test.append(tuple(map(float, line))) 
    
X_test = pd.DataFrame.from_records(data_test, columns=labels[:-1])

Y = model.predict(X_test)

for y in Y:
    print(y)   