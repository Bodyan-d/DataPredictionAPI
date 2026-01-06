from database import get_connection

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    quantity INTEGER NOT NULL,
    price NUMERIC NOT NULL
);
"""

def init_db():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(CREATE_TABLE_SQL)
            conn.commit()

if __name__ == "__main__":
    init_db()