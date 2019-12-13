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
	stop_server = "./pg_ctl -D ../../postgres-11.4/data stop"
	start_server = "./pg_ctl -D ../../postgres-11.4/data start"

	for j in range(0,2):

		startup_exec_time = []
		total_exec_time = []
		final_exec_time = []
		est_times = []

		conn,cur = connect("localhost", 5432, "imdb_full", "dsladmin")
		ranges = np.loadtxt("/home/dsladmin/Documents/vishal/index_scan/vuc_model_1/ranges.txt")
	
		for i in range(ranges.size):

			close_connection(conn)
			os.system(free_memory_command)
			os.system(stop_server)
			os.system(start_server)
			conn,cur = connect("localhost", 5432, "imdb_full", "dsladmin")
			result = run_query(cur,'cast_info_movie_id_sorted',int(ranges[i])+1)
			# close_connection(conn)

			print(result)

			startup_time, total_time, final_time = exec_times(result)
			startup_exec_time.append(startup_time)
			total_exec_time.append(total_time)
			final_exec_time.append(final_time)

			est_times.append(find_est_time(result))

		close_connection(conn)

		total_minus_startup_exec_time = []
		for i in range(len(startup_exec_time)):
			total_minus_startup_exec_time.append(total_exec_time[i]-startup_exec_time[i])

		np.savetxt('/home/dsladmin/Documents/vishal/index_scan/vuc_model_1/times'+str(j+1)+'.txt',total_minus_startup_exec_time,delimiter=',')
		np.savetxt('/home/dsladmin/Documents/vishal/index_scan/vuc_model_1/est_times'+str(j+1)+'.txt',est_times,delimiter=',')
