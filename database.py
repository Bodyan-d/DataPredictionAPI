import psycopg2
from psycopg2.extras import RealDictCursor

DB_CONFIG = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "egYi5@$DA&69n",
    "port": 5432,
}

def get_connection():
    return psycopg2.connect(
        cursor_factory=RealDictCursor,
        **DB_CONFIG
    )