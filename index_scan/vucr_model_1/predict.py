import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

loaded_model = pickle.load(open('/home/dsladmin/Documents/vishal/index_scan/vucr_model_1/model.sav', 'rb'))

temp = np.loadtxt('/home/dsladmin/Documents/vishal/index_scan/vucr_model_1/test_data_cards.txt')

X = []

for i in range(temp.size):
	X.append([])
	X[i].append(temp[i]**0.5)
	X[i].append(temp[i])
	X[i].append(temp[i]**2)

np.savetxt('/home/dsladmin/Documents/vishal/index_scan/vucr_model_1/predictions.txt',loaded_model.predict(X))

# result = loaded_model.score(X_test, Y_test)
# print(result)
