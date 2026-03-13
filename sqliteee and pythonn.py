import sqlite3
import pandas as pd

database = "pythondatabase.db"

conn = sqlite3.connect(database)
print("Opened database successfully")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS STUNDENTS(
               ID INTEGER PRIMARY KEY,
               NAME TEXT,
               AGE INTEGER
               )""")

conn.commit()

tables = pd.read_sql(""" SELECT * FROM sqlite_master 
             WHERE type='table'""", conn)

print("Tables in database:")
print(tables)