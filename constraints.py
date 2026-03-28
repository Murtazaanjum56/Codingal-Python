import sqlite3
import pandas as pd

database = 'database.sqlite'

conn = sqlite3.connect(database)

print('Opened data successfully')

conn.execute('''CREATE TABLE CLASS_101(
    SNO INTEGER PRIMARY KEY,
    NAME VARCHAR(50) NOT NULL,
    AGE INTEGER DEFAULT(15),
    GENDER TEXT NOT NULL,
    EMAIL TEXT NOT NULL,
    CONTACT_NO REAL NOT NULL 
             );''')

print('Table created successfully')

conn.execute('''INSERT INTO CLASS_101(SNO, NAME, AGE, GENDER, EMAIL, CONTACT_NO)  VALUES
             (1, 'ALICE', 15, 'FEMALE', 'alice@example.com', 1234567890);''')

conn.execute('''INSERT INTO CLASS_101(SNO, NAME, AGE, GENDER, EMAIL, CONTACT_NO)  VALUES
             (2, 'BOB', 16, 'MALE', 'bob@example.com', 0987654321);''')

conn.execute('''INSERT INTO CLASS_101(SNO, NAME, AGE, GENDER, EMAIL, CONTACT_NO)  VALUES
             (3, 'CHARLIE', 17, 'MALE', 'charlie@example.com', 1111111111);''')

conn.commit()

tables = pd.read_sql("""SELECT * FROM sqlite_master
            WHERE type = 'table' """, conn)

tables.info()