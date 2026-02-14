from database_connection import get_db_conn


def create_invoice(user_id:int, amount:float,description):
    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
            INSERT INTO invoices user_id, amount, description
            VALUES (%s, %s, %s, %s)
            
            RETURNING id,user_id, amount, description, created_at
            """,
            (user_id,amount,description))

            return cursor.fetchone()

