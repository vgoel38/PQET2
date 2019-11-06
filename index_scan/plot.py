import matplotlib.pyplot as plt
import numpy as np

num_tuples = 36244344
N = 10000000

X=[]
for i in range(N):
	X.append(i)
X = np.array(X)
X=X.reshape(-1,1)

# Y=np.loadtxt('page_ids.csv')
with open('distancs.csv') as myfile:
    Y = [int(next(myfile)) for x in range(N)]

# print(Y)

plt.plot(X, Y) 
plt.show() 