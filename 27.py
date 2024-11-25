import sqlite3

students = [
    {"name": "leila", "major": "memari", "grade": "16.5"},
    {"name": "taha", "major": "bargh", "grade": "19.5"},
    {"name": "keyvan", "major": "shimi", "grade": "14.75"},
    {"name": "sheyda", "major": "computer", "grade": "18.32"},
]


def create():
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS students ('name','major','grade');")
    conn.commit()
    conn.close()


def insert(student):
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    query = f"INSERT INTO students VALUES {(student['name'], student['major'], student['grade'])};"

    cur.execute(query)

    conn.commit()
    conn.close()


def select():
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students;")
    lines = cur.fetchall()

    for i in lines:
        if i[-1] >= "17":
            print(i)

    conn.commit()
    conn.close()


# create()
#
# for i in students:
#     insert(i)

select()
