import sqlite3
import pandas as pd

database = "database.sqlite"

conn = sqlite3.connect(database)
print("Opened database successfully")
cursor = conn.cursor()

tables = pd.read_sql("""SELECT * FROM sqlite_master 
                WHERE type = 'table';""", conn)

tables.info()

matches = pd.read_sql("""SELECT * FROM MATCH;""",  conn)

matches.info()