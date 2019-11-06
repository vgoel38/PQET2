import sys
import os
import psycopg2
import numpy as np



def execute_sql(cur, sql):
    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print(e.pgerror)

def connect(dbhost, dbport, dbname, username):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        #print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host = dbhost, port = dbport, database = dbname, user = username)
        conn.autocommit = True

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return conn,conn.cursor()



def close_connection(conn):
    if conn is not None:
        conn.close()
        #print('Database connection closed.')


def run_query(cur, table, x, y):
	sql = "EXPLAIN (ANALYSE,BUFFERS) SELECT * FROM " + table + " WHERE movie_id >" + str(x) + "AND movie_id<= "+ str(y) + ";"
	
	execute_sql(cur, sql)
	result = cur.fetchall()
	return result

def find_act_rel_pages(cur):
	sql = "select heap_blks_read from pg_statio_all_tables where relname='cast_info';"

	execute_sql(cur, sql)
	result = cur.fetchall()
	return result[0][0]

def find_act_idx_pages(cur):
	sql = "select idx_blks_read from pg_statio_all_tables where relname='cast_info';"

	execute_sql(cur, sql)
	result = cur.fetchall()
	return result[0][0]


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

	startup_exec_time = []
	total_exec_time = []
	final_exec_time = []

	est_time = []
	act_rel_pages = []
	act_index_pages = []

	conn,cur = connect("localhost", 5432, "imdb", "dsladmin")
	curr_rel_pages = find_act_rel_pages(cur)
	curr_index_pages = find_act_idx_pages(cur)

	#2331601
	#23000
	for i in range(0, 2331601, 23000):

		close_connection(conn)
		os.system(free_memory_command)
		os.system(stop_server)
		os.system(start_server)
		conn,cur = connect("localhost", 5432, "imdb", "dsladmin")
		result = run_query(cur,'cast_info',i,i+23000)
		# close_connection(conn)

		print(result)

		startup_time, total_time, final_time = exec_times(result)
		startup_exec_time.append(startup_time)
		total_exec_time.append(total_time)
		final_exec_time.append(final_time)

		est_time.append(find_est_time(result))
		temp=find_act_rel_pages(cur)
		act_rel_pages.append(temp-curr_rel_pages)
		temp=find_act_idx_pages(cur)
		act_index_pages.append(temp-curr_index_pages)


	close_connection(conn)

	total_minus_startup_exec_time = []
	for i in range(len(startup_exec_time)):
		total_minus_startup_exec_time.append(total_exec_time[i]-startup_exec_time[i])

	# print(total_minus_startup_exec_time)
	# print(est_time)
	# print(act_rel_pages)
	# print(act_index_pages)

	np.savetxt('/home/dsladmin/Documents/vishal/index_scan/temp/act_times.txt',total_minus_startup_exec_time,delimiter=',');
	np.savetxt('/home/dsladmin/Documents/vishal/index_scan/temp/est_times.txt',est_time,delimiter=',');
	np.savetxt('/home/dsladmin/Documents/vishal/index_scan/temp/act_rel_pages.txt',act_rel_pages,delimiter=',');
	np.savetxt('/home/dsladmin/Documents/vishal/index_scan/temp/est_rel_pages.txt',act_index_pages,delimiter=',');

	# # plt.scatter(num_rows, startup_exec_time,color='blue')
	# plt.plot(ranges, total_minus_startup_exec_time, color='green')
	# # plt.scatter(num_rows, total_minus_startup_exec_time,color='red')
	# # # plt.plot(num_rows, final_exec_time,color='yellow')

	# plt.xlabel('range')
	# plt.ylabel('execution time (ms)')
	# # plt.title('index scan [10 MB]')
	# plt.show()
