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



if __name__ == "__main__":

	free_memory_command = "free && sync && sudo sh -c 'echo 3 >/proc/sys/vm/drop_caches' && free > /dev/null"
	stop_server = "./pg_ctl -D ../../data stop"
	start_server = "./pg_ctl -D ../../data start"

	# size_in_gb = 1/1024
	# #constant
	# size_of_page_in_kb = 4
	# num_rows_per_page = 226

	# num_of_pages = int((size_in_gb*1024*1024)/size_of_page_in_kb)

	# i = 100

	for j in range(0,1):

		startup_exec_time = []
		total_exec_time = []
		final_exec_time = []

		conn,cur = connect("localhost", 5432, "imdb_full", "sahana")
		ranges = []

		base_size = 10000
		i=1000000

		drop_table(cur,'aka_name_temp')
		drop_table(cur,'name_temp')
	
		while i<=4000000:

			create_small_table(cur, 'aka_name', 'aka_name_temp', base_size)
			create_small_table(cur, 'name', 'name_temp', i)
			vacuum_analyse(cur, 'aka_name_temp')
			vacuum_analyse(cur, 'name_temp')
			close_connection(conn)
			os.system(free_memory_command)
			os.system(stop_server)
			os.system(start_server)
			conn,cur = connect("localhost", 5432, "imdb_full", "sahana")
			
			result = run_query(cur,'aka_name_temp','name_temp', 'aka_name_temp.person_id', 'name_temp.id')
			drop_table(cur,'aka_name_temp')
			drop_table(cur,'name_temp')
			# close_connection(conn)

			print(result, file = open('../../LOG/log8.txt', "a"))

			#startup_time, total_time, final_time = exec_times(result)
			#startup_exec_time.append(startup_time)
			#total_exec_time.append(total_time)
			#final_exec_time.append(final_time)
			#ranges.append(i)

			i=i+100000

		close_connection(conn)

		#full range query
		##os.system(stop_server)
		#os.system(start_server)
		#conn,cur = connect("localhost", 5432, "imdb_full", "sahana")
		#result = run_query(cur,'cast_info',2331601+1)
		# close_connection(conn)

		# print(result)

		# startup_time, total_time, final_time = exec_times(result)
		# startup_exec_time.append(startup_time)
		# total_exec_time.append(total_time)
		# final_exec_time.append(final_time)
		# ranges.append(2331601+1)

		# total_minus_startup_exec_time = []
		# for i in range(len(startup_exec_time)):
		# 	total_minus_startup_exec_time.append(total_exec_time[i]-startup_exec_time[i])

		# np.savetxt('/home/dsladmin/Documents/vishal/index_scan/vu_model_0/times'+str(j+1)+'.txt',total_minus_startup_exec_time,delimiter=',');
		# np.savetxt('/home/dsladmin/Documents/vishal/index_scan/vu_model_0/ranges.txt',ranges,delimiter=',');

	# # plt.scatter(num_rows, startup_exec_time,color='blue')
	# plt.plot(ranges, total_minus_startup_exec_time, color='green')
	# # plt.scatter(num_rows, total_minus_startup_exec_time,color='red')
	# # # plt.plot(num_rows, final_exec_time,color='yellow')

	# plt.xlabel('range')
	# plt.ylabel('execution time (ms)')
	# # plt.title('index scan [10 MB]')
	# plt.show()
