import sqlite3

conn = sqlite3.connect("info.db")
cur = conn.cursor()

# cur.execute("CREATE TABLE customers (name,city,phone);")

# cur.execute("INSERT INTO customers VALUES('ali','kerman','09399462420');")
# cur.execute("INSERT INTO customers VALUES('mahla','yazd','09308175331');")
# cur.execute("INSERT INTO customers VALUES('saeed','rasht','09193461660');")

cur.execute("SELECT * FROM customers;")
records = cur.fetchall()

for i in records:
    print(i[-1])

conn.commit()
conn.close()
