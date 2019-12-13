import random
import numpy as np

max_range = 2331601
total_queries = 30

X = []
i = 0
for i in range(total_queries):
	X.append(random.randint(1,max_range))

np.savetxt('/home/dsladmin/Documents/vishal/index_scan/vuc_model_minus_1/test_data.txt',X,delimiter=',');
		
