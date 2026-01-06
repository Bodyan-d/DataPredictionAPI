from database import get_connection
from schemas.sales import SalesCreate

def create_sale(sale: SalesCreate):
    query = """
        INSERT INTO sales (date, quantity, price)
        VALUES (%s, %s, %s)
        RETURNING id, date, quantity, price;
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (sale.date, sale.quantity, sale.price))
            return cur.fetchone()

def get_all_sales():
    query = """
        SELECT id, date, quantity, price
        FROM sales
        ORDER BY date;
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()