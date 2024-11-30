import sqlite3


def create(table, fields):
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    command = f"CREATE TABLE IF NOT EXISTS {table} {tuple(fields)};"
    cur.execute(command)

    conn.commit()
    conn.close()


def insert():
    pass


def select(table):
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    command = f"SELECT * FROM {table};"
    try:
        cur.execute(command)
    except sqlite3.OperationalError:
        print(f"No such table {table}. Try again")
        main()

    records = cur.fetchall()

    print()

    for i in records:
        print(i)

    conn.commit()
    conn.close()


def main():
    action = input("""
1 : Create a table
2 : Insert into a table
3 : Display a table
Action : """)

    if action == "1":
        table = input("Table name :")
        columns = input("Table columns (separated by comma) : ").split(",")

        create(table, columns)
    elif action == "2":
        insert()
    elif action == "3":
        select(input("Table name : "))
    else:
        print("Invalid entry. Try again")
        main()


main()
