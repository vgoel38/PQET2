import random
import numpy as np

max_range = 2331601
total_queries = 30

X = []
i = 0
for i in range(total_queries):
	length = random.randint(1,int(max_range/2))
	init_point = random.randint(1,max_range)
	X.append(init_point)
	X.append(min(max_range,init_point+length))

np.savetxt('/home/dsladmin/Documents/vishal/index_scan/vucr_model_0/test_data.txt',X,delimiter=',');
		
