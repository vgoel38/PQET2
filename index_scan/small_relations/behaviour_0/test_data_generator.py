import random
import numpy as np

# max_range = 2331601
max_range = 233160
total_queries = 10

X = []
i = 0
for i in range(total_queries):
	X.append(random.randint(1,max_range))

np.savetxt('/home/dsladmin/Documents/vishal/index_scan/vu_model_0/test_data.txt',X,delimiter=',');
		