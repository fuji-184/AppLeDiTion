from psycopg2 import pool

class Database:
    def __init__(self, minconn=1, maxconn=5, dbname="skripsi", user="fuji", password="fuji123", host="localhost", port=5432):
        self.connection_pool = pool.SimpleConnectionPool(minconn=minconn, maxconn=maxconn, dbname=dbname, user=user, password=password, host=host, port=port)

    def query(self, query, params=None):
        conn = self.connection_pool.getconn()
        cursor = conn.cursor()
        cursor.execute(query, params)
        hasil = cursor.fetchall()
        cursor.close()
        self.connection_pool.putconn(conn)
        return hasil

db = Database()