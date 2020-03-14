import psycopg2
import numpy as np
#from config import config



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



def execute_sql(cur, sql):
    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print(e.pgerror)



def create_table(cur, table):
    sql = "CREATE TABLE " + table + "(num    INT     NOT NULL);"
    execute_sql(cur, sql)

def create_small_table(cur, original, new, num_tuples):
    sql = "CREATE TABLE " + new + " AS SELECT * FROM " + original + " LIMIT " + str(num_tuples);
    execute_sql(cur, sql)



def drop_table(cur, table):
    sql = "DROP TABLE " + table + ";"
    execute_sql(cur, sql)



def drop_index(cur, index):
    sql = "DROP INDEX " + index + ";"
    execute_sql(cur, sql)



def insert_data(cur, table):
    sql = "COPY " + table + " FROM '/home/dsladmin/Desktop/PQET/src/index_scan/data.csv' DELIMITERS " + "',' CSV;"
    execute_sql(cur, sql)



def create_index(cur, index, table, col):
    sql = "CREATE UNIQUE INDEX " + index + " ON " + table + " USING btree " + "(" + col + ");"
    execute_sql(cur, sql)



def run_query(cur, table1, table2, attr1, attr2):
    # sql = "EXPLAIN (ANALYZE,BUFFERS) SELECT * FROM " + table1 + ", " + table2 + " WHERE " + attr1 + " < " + str(x) + " AND " + attr2 + " < " + str(y) + " AND " + attr1 + " = " + attr2 + " ;"
    sql = "EXPLAIN (ANALYSE, BUFFERS) SELECT * FROM " + table1 + ", " + table2 + " WHERE " + attr1 + " = " + attr2 + " ;"
    execute_sql(cur, sql)

    # file = open('/home/dsladmin/Desktop/PQET/src/query.sql', 'w')
    # file.write(sql)
    # file.close()

    result = cur.fetchall()
    return result

def vacuum_analyse(cur, table):
    query = "VACUUM ANALYZE " + table + ";"
    execute_sql(cur, query)

def commit(cur):
    sql = "commit;"
    execute_sql(cur, sql)
    


def update_catalog(cur, table):
    sql = "analyze " + table + ";"
    execute_sql(cur, sql)



def size_of_table(cur, table):
    sql = "SELECT relpages FROM pg_class WHERE relname = " + "'" + table + "'" + " ;"
    execute_sql(cur, sql)

    result = cur.fetchall()
    return result[0][0]



if __name__ == "__main__":

    conn,cur = connect("localhost", 5432, "testdb", "postgres")

    insert_data(cur, 'test_scan_2')
    result = run_query(cur, 'test_scan_2')
    commit(cur)
    print(result)

    close_connection(conn)
