import sys
import os
# from  data_gen import *
from main import *
# import matplotlib.pyplot as plt 

def find_range(cur, table, x):
    sql = "select max(movie_id) from (select movie_id from cast_info_movie_id_sorted_desc where movie_id>0 limit "+str(i)+") as temp;"
    execute_sql(cur, sql)
    result = cur.fetchall()[0][0]
    return result

def find_card(cur, table, x):
    sql = "select count(*) from cast_info_movie_id_sorted_desc where movie_id>0 and movie_id<=" + str(x);
    execute_sql(cur, sql)
    result = cur.fetchall()[0][0]
    return result

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
	stop_server = "./pg_ctl -D ../../postgres-11.4/data stop"
	start_server = "./pg_ctl -D ../../postgres-11.4/data start"

	conn,cur = connect("localhost", 5432, "imdb_full", "dsladmin")
	#ranges = np.loadtxt("/home/dsladmin/Documents/vishal/index_scan/vuc_model_minus_1/ranges.txt")

	os.system(start_server)
	ranges = []
	cards = []

	for i in range(30000001,37000001,1000000):
		
		rang = find_range(cur,'cast_info_movie_id_sorted_desc',i)
		card = find_card(cur,'cast_info_movie_id_sorted_desc',rang)
		ranges.append(rang)
		cards.append(card)
		print(rang, card)

	close_connection(conn)

	np.savetxt('/home/dsladmin/Documents/vishal/index_scan/vuc_model_minus_1/ranges.txt',ranges,delimiter=',');
	np.savetxt('/home/dsladmin/Documents/vishal/index_scan/vuc_model_minus_1/cards.txt',cards,delimiter=',');