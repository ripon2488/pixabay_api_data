from psycopg2.pool import ThreadedConnectionPool
from contextlib import contextmanager

db_pool = ThreadedConnectionPool(
    minconn=1,
    maxconn=5,
    user='postgres',
    password='Ripon@123',
    database='pixabay_db',
    host='localhost',
    port=5432,
    options="-c search_path=" + 'public',
)

@contextmanager
def get_cursor():
    con = db_pool.getconn()
    cursor = con.cursor()
    try:
        yield con, cursor
    finally:
        cursor.close()
        db_pool.putconn(con)