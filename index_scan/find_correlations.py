import sys
import os


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
	sql = "SELECT corr((ctid::text::point)[0]::bigint,movie_id) FROM " + table + " WHERE movie_id >" + str(x) + "AND movie_id<= "+ str(y) + ";"
	
	execute_sql(cur, sql)
	result = cur.fetchall()
	return result


if __name__ == "__main__":

	conn,cur = connect("localhost", 5432, "imdb", "dsladmin")
	
	for i in range(0, 2331601, 23000):

		result = run_query(cur,'cast_info',i,i+23000)
		print(result)

	close_connection(conn)