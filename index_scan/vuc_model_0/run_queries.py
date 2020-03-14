import sys
import os
# from  data_gen import *
from main import *
# import matplotlib.pyplot as plt 

def exec_times(result):

	index_1 = (result[0][0]).find("actual")
	index_2 = (result[0][0][index_1:]).find("..")
	index_3 = (result[0][0][index_1+index_2:].find(" "))

	startup_time = result[0][0][index_1+12:index_1+index_2]
	total_time = result[0][0][index_1+index_2+2:index_1+index_2+index_3]

	index_4 = (result[4][0]).find(":")
	index_5 = (result[4][0]).find("ms")
	final_time = result[4][0][index_4+2:index_5-1]

	return float(startup_time), float(total_time), float(final_time)
	# return float(total_time) , float(startup_time)

def find_est_time(result):

	index_1 = (result[0][0]).find("cost=")
	index_2 = (result[0][0][index_1:]).find("..")
	index_3 = (result[0][0][index_1+index_2:].find(" "))

	startup_time = result[0][0][index_1+5:index_1+index_2]
	total_time = result[0][0][index_1+index_2+2:index_1+index_2+index_3]

	return float(total_time) - float(startup_time)



if __name__ == "__main__":

	free_memory_command = "free && sync && sudo sh -c 'echo 3 >/proc/sys/vm/drop_caches' && free > /dev/null"
	stop_server = "./pg_ctl -D ../../data stop"
	start_server = "./pg_ctl -D ../../data start"

	# file=open('/home/sahana/Documents/PQET/Prediction-of-Query-Execution-Time/index_scan/vuc_model_0/act_times.txt','a')
	# file.truncate()
	# file.close()

	# file=open('/home/sahana/Documents/PQET/Prediction-of-Query-Execution-Time/index_scan/vuc_model_0/times1.txt','a')
	# f.truncate()
	# f.close()

	# file=open('/home/sahana/Documents/PQET/Prediction-of-Query-Execution-Time/index_scan/vuc_model_0/times2.txt','a')
	# f.truncate()
	# f.close()

	# file=open('/home/sahana/Documents/PQET/Prediction-of-Query-Execution-Time/index_scan/vuc_model_0/est_times.txt','a')
	# file.truncate()
	# file.close()

	# file=open('/home/sahana/Documents/PQET/Prediction-of-Query-Execution-Time/index_scan/vuc_model_0/est_times1.txt','a')
	# f.truncate()
	# f.close()

	# file=open('/home/sahana/Documents/PQET/Prediction-of-Query-Execution-Time/index_scan/vuc_model_0/est_times2.txt','a')
	# f.truncate()
	# f.close()

	for j in range(0,1):

		conn,cur = connect("localhost", 5432, "imdb_full", "dsladmin")
		att_values = np.loadtxt("/home/sahana/Documents/PQET/Prediction-of-Query-Execution-Time/index_scan/vuc_model_0/att_values.txt")

		initial_point = 2066397
	
		for i in range(att_values.size):

			close_connection(conn)
			os.system(free_memory_command)
			os.system(stop_server)
			os.system(start_server)
			conn,cur = connect("localhost", 5432, "imdb_full", "dsladmin")
			result = run_query(cur,'movie_info',initial_point, int(att_values[i]))
			print(result)

			# startup_time, total_time, final_time = exec_times(result)

			print(result,file=open('/home/sahana/Documents/PQET/Prediction-of-Query-Execution-Time/index_scan/vuc_model_0/queries.txt','a'))
			# print(find_est_time(result),file=open('/home/sahana/Documents/PQET/Prediction-of-Query-Execution-Time/index_scan/vuc_model_0/est_times.txt','a'))
			# print(total_time[i]-startup_time[i], file=open('/home/sahana/Documents/PQET/Prediction-of-Query-Execution-Time/index_scan/vuc_model_0/act_times.txt','a'))

		close_connection(conn)