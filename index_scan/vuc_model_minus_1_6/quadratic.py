import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# num_tuples = 36244344

data=np.loadtxt('cards.txt')
# for i in range(num_tuples):
# 	X.append(i)
# X = np.array(X)
# X=X.reshape(-1,1)

n = data.size

X = []

for i in range(n):
	X.append([])
	X[i].append(data[i]**0.5)
	X[i].append(data[i])
	X[i].append(data[i]**2)

Y1=np.loadtxt('times1.txt')
Y2=np.loadtxt('times2.txt')
Y = []

for i in range(n):
	Y.append((Y1[i]+Y2[i])/2)

reg = LinearRegression().fit(X, Y)
print(reg.score(X, Y))
print(reg.coef_)
print(reg.intercept_)

pickle.dump(reg, open('model.sav', 'wb'))