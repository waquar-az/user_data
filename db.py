import sqlite3
conn = sqlite3.connect("database1.db")

print("opened database1 successfully")

conn.execute("CREATE TABLE students (name TEXT,addr TEXT,city TEXT,pin TEXT)")

print("table created successfullyy")

conn.close()