import csv, psycopg2
from connect import get_conn

def run_sql(query, params=None, fetch=False):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
            return cur.fetchall() if fetch else None

def import_csv():
    with open('contacts.csv', 'r') as f:
        for row in csv.DictReader(f):
            run_sql("INSERT INTO pb (name, phone) VALUES (%s, %s) ON CONFLICT DO NOTHING", (row['name'], row['phone']))
    print("Imported")

def menu():
    while True:
        cmd = input("\n1:Import, 2:Add, 3:Upd, 4:Find, 5:Del, 0:Exit\n> ")
        if cmd == '1': import_csv()
        elif cmd == '2': run_sql("INSERT INTO pb(name, phone) VALUES (%s, %s)", (input("Name: "), input("Phone: ")))
        elif cmd == '3': run_sql("UPDATE pb SET phone=%s WHERE name=%s", (input("New Phone: "), input("Name: ")))
        elif cmd == '4': 
            res = run_sql("SELECT * FROM pb WHERE name LIKE %s", (f"%{input('Search: ')}%",), True)
            for r in res: print(r)
        elif cmd == '5': run_sql("DELETE FROM pb WHERE name=%s OR phone=%s", (input("Target: "), input("Target: ")))
        elif cmd == '0': break

if __name__ == "__main__":
    menu()