import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

loaded_model = pickle.load(open('model.sav', 'rb'))

X_test = np.array([16965081]).reshape(-1,1)
print(loaded_model.predict(X_test))

# result = loaded_model.score(X_test, Y_test)
# print(result)