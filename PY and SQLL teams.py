import sqlite3
import pandas as pd

database = "database.sqlite"

conn = sqlite3.connect(database)
print("Opened database successfully")

tables = pd.read_sql(""" SELECT * FROM sqlite_master
            WHERE type = "table";""",  conn)

print("Tables in database:")
tables.info()

teams = pd.read_sql("""SELECT * FROM Team
                    ;""", conn)

print("Teams in database:")
teams.info()

matches = pd.read_sql("""SELECT * FROM Match
            WHERE Match_winner = 7;""", conn)
print("Matches in database:")
matches.info()

MI_wins = pd.read_sql("""SELECT * FROM Match
                WHERE Match_winner = 7;""", conn)
print("MUMBAI INDIANS wins in database:")

MI_wins.info()

MI_58_59 = pd.read_sql("""SELECT * FROM Match
        WHERE Match_winner = 7 AND Season_Id IN (8,9);""", conn)
print("MUMBAI INDIANS wins in 2015 and 2016 seasons in database:")
MI_58_59.info()

new_teams = pd.read_sql("""SELECT * FROM Team
            WHERE Team_Name LIKE "%DE%";""", conn)
print("Teams with DE in their name in database:")
new_teams.info()

min_max_margin = pd.read_sql(""" SELECT MIN(Win_Margin), MAX(Win_Margin)
        From Match;""", conn)
print("Minimum and Maximum Win Margins in database:")
min_max_margin.info()

conn.close()