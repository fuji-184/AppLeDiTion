from psycopg2 import pool
from psycopg2.extras import RealDictCursor
import traceback

class Database:
    def __init__(self, minconn=1, maxconn=5, dbname="fuji", user="postgres", password="fuji", host="localhost", port=5432):
        self.connection_pool = pool.SimpleConnectionPool(
            minconn=minconn,
            maxconn=maxconn,
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

    def query(self, query, params=None, fetch=True):
        conn = None
        cursor = None
        try:
            conn = self.connection_pool.getconn()
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute(query, params)
            
            query_type = query.strip().split()[0].upper()
            print(f"tipe query: {query_type}")
            if query_type in ['SELECT', 'SHOW']:
                result = cursor.fetchall()
            elif query_type in ['INSERT'] and fetch:
                result = cursor.fetchone()
            else:
                result = "Query executed successfully."
            
            if query_type in ['INSERT', 'UPDATE', 'DELETE']:
                conn.commit()
            
            return result
        except Exception as e:
            print(f'Error saat operasi database: {e}')
            traceback.print_exc()
            return None
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.connection_pool.putconn(conn)

db = Database()
