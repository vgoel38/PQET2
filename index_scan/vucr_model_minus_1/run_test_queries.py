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

def find_card_diff(result):

	result = str(result)
	result = result.split('rows=')
	card1 = int(result[1].split(' ')[0])
	card2 = int(result[2].split(' ')[0])
	print(card1)
	print(card2)
	return abs(card1-card2)

if __name__ == "__main__":

	free_memory_command = "free && sync && sudo sh -c 'echo 3 >/proc/sys/vm/drop_caches' && free > /dev/null"
	stop_server = "./pg_ctl -D ../../postgres-11.4/data stop"
	start_server = "./pg_ctl -D ../../postgres-11.4/data start"

	startup_exec_time = []
	total_exec_time = []
	final_exec_time = []
	est_time = []
	max_card_diff = -1

	conn,cur = connect("localhost", 5432, "imdb_full", "dsladmin")
	ranges = np.loadtxt("/home/dsladmin/Documents/vishal/index_scan/vucr_model_minus_1/test_data.txt")

	for i in range(0,ranges.size,2):

		close_connection(conn)
		os.system(free_memory_command)
		os.system(stop_server)
		os.system(start_server)
		conn,cur = connect("localhost", 5432, "imdb_full", "dsladmin")
		result = run_query(cur,'cast_info_movie_id_sorted_desc',int(ranges[i]), int(ranges[i+1]))
		# close_connection(conn)

		print(result)

		startup_time, total_time, final_time = exec_times(result)
		startup_exec_time.append(startup_time)
		total_exec_time.append(total_time)
		final_exec_time.append(final_time)

		est_time.append(find_est_time(result))

		max_card_diff=max(max_card_diff,find_card_diff(result))

	close_connection(conn)

	print("max_card_diff = ")
	print(max_card_diff)

	total_minus_startup_exec_time = []
	for i in range(len(startup_exec_time)):
		total_minus_startup_exec_time.append(total_exec_time[i]-startup_exec_time[i])

	np.savetxt('/home/dsladmin/Documents/vishal/index_scan/vucr_model_minus_1/actual_times.txt',total_minus_startup_exec_time,delimiter=',');
	np.savetxt('/home/dsladmin/Documents/vishal/index_scan/vucr_model_minus_1/est_times.txt',est_time,delimiter=',');
