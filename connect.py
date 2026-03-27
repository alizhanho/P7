import psycopg2
from config import DB_CONFIG

def get_conn():
    return psycopg2.connect(**DB_CONFIG)

def init_db():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS pb (id SERIAL, name TEXT, phone TEXT UNIQUE)")
    print("DB Ready")

if __name__ == "__main__":
    init_db()