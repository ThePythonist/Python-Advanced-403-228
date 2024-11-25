import sqlite3

students = [
    {"name": "Amirali", "code": 40211, "job": "Backend Developer"},
    {"name": "Parsa", "code": 40212, "job": "Frontend Developer"},
    {"name": "Mehrzad", "code": 40213, "job": "Security Engineer"},
    {"name": "Mohammad Mehdi", "code": 40214, "job": "DevOps Engineer"},
    {"name": "Bahar", "code": 40215, "job": "Civil Engineer"},
    {"name": "Farzad", "code": 40376, "job": "IT Man"},
]


def insert(item):
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()
    command = "SELECT * FROM employees;"
    cur.execute(command)
    records = cur.fetchall()
    records = [i[1:] for i in records]

    if not tuple(item.values()) in records:
        query = f"INSERT INTO employees(name,code,job) VALUES {(item['name'], item['code'], item['job'])};"
        cur.execute(query)
    else:
        print("Record already exists in DB")

    conn.commit()
    conn.close()


def select(table):
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    command = f"SELECT * FROM {table};"
    cur.execute(command)
    records = cur.fetchall()
    for i in records:
        print(i)

    conn.commit()
    conn.close()


# insert(students[-1])
select("employees")
