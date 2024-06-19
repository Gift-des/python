import sqlite3
conn = sqlite3.connect("example.db")
print("successfully connected")

conn.execute("INSERT INTO Employee VALUES(1, 'Mark','Mugo',45,120000.00,'Manager')")
conn.execute("INSERT INTO Employee VALUES(2, 'Jane','Njoroge',28,280000.00,'Admin')")
conn.execute("INSERT INTO Employee VALUES(3, 'Martha','Mugo',45,120000.00,'HR')")
conn.execute("INSERT INTO Employee VALUES(4, 'Marcus','Hunter',30,150000.00,'CEO')")
conn.execute("INSERT INTO Employee VALUES(5, 'Austin','Stein',45,120000.00,'Receptionist')")
conn.execute("INSERT INTO Employee VALUES(6, 'Ali','Hassan',45,120000.00,'Marketing Director')")

conn.commit()
print("successfully inserted values into Employee table")
