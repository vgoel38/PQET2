import sys
import os
# from  data_gen import *
from main import *
# import matplotlib.pyplot as plt 

def find_att_value(cur, table, attr, card):
    sql = "select max(" + attr + ") from (select " + attr + " from " + table + " where " + attr + " >0 limit " + str(card) + " ) as temp;"
    execute_sql(cur, sql)
    result = cur.fetchall()[0][0]
    return result

def find_card(cur, table, attr, att_value):
    sql = "select count(*) from " + table + " where " + attr + ">0 and " + attr + "<=" + str(att_value) + ";"
    execute_sql(cur, sql)
    result = cur.fetchall()[0][0]
    return result

if __name__ == "__main__":

	# free_memory_command = "free && sync && sudo sh -c 'echo 3 >/proc/sys/vm/drop_caches' && free > /dev/null"
	# stop_server = "./pg_ctl -D ../../data stop"
	# start_server = "./pg_ctl -D ../../data start"

	conn,cur = connect("localhost", 5432, "imdb_full", "sahana")
	#ranges = np.loadtxt("/home/dsladmin/Documents/vishal/index_scan/vuc_model_minus_1/ranges.txt")

	# os.system(start_server)
	att_values = []
	cards = []

	os.remove('/home/sahana/Documents/PQET/Prediction-of-Query-Execution-Time/index_scan/vuc_model_0/att_values.txt')
	os.remove('/home/sahana/Documents/PQET/Prediction-of-Query-Execution-Time/index_scan/vuc_model_0/cards.txt')

	for i in range(100000,14835720,100000):
		
		att_value = find_att_value(cur,'movie_info','movie_id',i)
		card = find_card(cur,'movie_info','movie_id',att_value)
		att_values.append(att_value)
		cards.append(card)
		print(att_value,file=open('/home/sahana/Documents/PQET/Prediction-of-Query-Execution-Time/index_scan/vuc_model_0/att_values.txt','a'))
		print(card, file=open('/home/sahana/Documents/PQET/Prediction-of-Query-Execution-Time/index_scan/vuc_model_0/cards.txt','a'))

	close_connection(conn)