import sqlite3

conn = sqlite3.connect("info.db")  # etesal be database
cur = conn.cursor()  # ijad cursor bar rooye shell

cur.execute("CREATE TABLE IF NOT EXISTS students (name,age,major);")  # ejraye dastoor sql

# cur.execute("INSERT INTO students VALUES('farzad','26','computer engineering');")
# cur.execute("INSERT INTO students VALUES('arian','19','math');")

# cur.execute("DELETE FROM students;") # hazf kole khotot table students
# cur.execute("DELETE FROM students WHERE name='farzad';")

# cur.execute("DROP TABLE students;")  # hazf table hamrah ba khototash

cur.execute("SELECT * FROM students;")
x = cur.fetchall()
print(x)

conn.commit()  # zakhire taghirat rooye database
conn.close()  # bastan database
