import numpy as np
import pwlf

cards = np.loadtxt("cards.txt")
act = np.loadtxt("act.txt")

my_pwlf = pwlf.PiecewiseLinFit(cards, act)
breaks = my_pwlf.fit(2)
print(breaks)

test_cards = np.loadtxt("test_cards.txt")
predictions = my_pwlf.predict(test_cards)

np.savetxt("pred.txt",predictions)
