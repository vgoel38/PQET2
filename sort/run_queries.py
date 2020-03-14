import sys, getopt
import os
from generate_nums import generate_nums
# from  data_gen import *
from main import *
# import matplotlib.pyplot as plt 

if __name__ == "__main__":

	free_memory_command = "free && sync && sudo sh -c 'echo 3 >/proc/sys/vm/drop_caches' && free > /dev/null"
	stop_server = "./pg_ctl -D ../../data stop"
	start_server = "./pg_ctl -D ../../data start"

	inputfile = ''
	outputfile = ''
	varchar_length = 1
	num_queries = 5
	num_loops = 1
	shuffle = 0

	try:
		opts, args = getopt.getopt(sys.argv[1:],"hi:o:v:q:l:s:",["ifile=","ofile=","varchar_length=","num_queries=","num_loops","shuffle="])
	except getopt.GetoptError:
		print('test.py -i <inputfile> -o <outputfile> -v <varcharlength> -q <num_queries> -l <num_loops> -s <shuffle>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('test.py -i <inputfile> -o <outputfile> -v <varcharlength> -q <num_queries> -l <num_loops> -s <shuffle>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
		elif opt in ("-v", "varchar_length"):
			varchar_length = int(arg)
		elif opt in ("-q", "num_queries"):
			num_queries = int(arg)
		elif opt in ("-l","num_loops"):
			num_loops = int(arg)
		elif opt in ("-s","shuffle"):
			shuffle = int(arg)

	for j in range(num_loops):
		for i in range(num_queries):

			conn,cur = connect("localhost", 5432, "imdb_full", "sahana")
			drop_table(cur,'sort_del')

			create_table(cur, 'sort_del', varchar_length)
			generate_nums(inputfile,(i+1)*10000000, varchar_length, shuffle)
			insert_data(cur, 'sort_del')
			vacuum_analyse(cur, 'sort_del')

			close_connection(conn)
			os.system(free_memory_command)
			os.system(stop_server)
			os.system(start_server)
			conn,cur = connect("localhost", 5432, "imdb_full", "sahana")
			
			result = run_query(cur,'sort_del','num')
			# close_connection(conn)

			print(result, file = open(outputfile, "a"))
			#print(result, file = open('/home/sahana/Documents/PQET/Prediction-of-Query-Execution-Time/sort/unsorted_plans.txt', "a"))
			print(find_correlation(cur,'sort_del','num'))

		close_connection(conn)
