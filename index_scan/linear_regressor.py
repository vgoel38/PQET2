import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# num_tuples = 36244344

X=np.loadtxt('ranges.txt')
# for i in range(num_tuples):
# 	X.append(i)
# X = np.array(X)
X=X.reshape(-1,1)

Y=np.loadtxt('times.txt')

reg = LinearRegression().fit(X, Y)
print(reg.score(X, Y))
print(reg.coef_)
print(reg.intercept_)

pickle.dump(reg, open('model.sav', 'wb'))