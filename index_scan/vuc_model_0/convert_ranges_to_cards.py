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

def find_card(result):

	result = str(result)
	result = result.split('rows=')
	card2 = int(result[2].split(' ')[0])
	print(card2)
	return card2

if __name__ == "__main__":

	cards = []

	conn,cur = connect("localhost", 5432, "imdb_full", "dsladmin")
	ranges = np.loadtxt("/home/dsladmin/Documents/vishal/index_scan/vuc_model_0/test_data.txt")

	for i in range(0,ranges.size):

		result = run_query(cur,'cast_info',int(ranges[i]))
		print(result)
		# close_connection(conn)

		cards.append(find_card(result))

	close_connection(conn)

	np.savetxt('/home/dsladmin/Documents/vishal/index_scan/vuc_model_0/test_data_cards.txt',cards,delimiter=',');
