import numpy as np
from sklearn.linear_model import LinearRegression

cards = np.loadtxt("cards.txt")
cards = cards.reshape(-1,1)
act = np.loadtxt("act.txt")

reg = LinearRegression().fit(cards,act)

predictions = reg.predict(cards)

print(reg.coef_, reg.intercept_)

for elem in predictions:
	print(elem)
