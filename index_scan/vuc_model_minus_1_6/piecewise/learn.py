import numpy as np
from piecewise import piecewise

cards = np.loadtxt("cards.txt")
act = np.loadtxt("act.txt")

model = piecewise(cards, act)

for i in range(len(model.segments)):
	print(model.segments[i].coeffs)

test_cards = np.loadtxt("test_cards.txt")

np.savetxt("pred.txt",model.predict(test_cards))
