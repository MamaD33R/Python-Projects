import sqlite3
import os

conn = sqlite3.connect('project.db') # Setting up connection to sql server

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_feedback( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_comments STRING, \
        col_fname TEXT \
        )")
    conn.commit() # to commit our changes or additions
conn.close() # closing the connection

# now finding the directory where .py and files are stored and only displaying .txt files

for file in os.listdir('C:/Users/space/OneDrive/Documents/GitHub/Python-Projects/Database'):
    if file.endswith('.txt'):
        print(file)
# adding files into the database
with conn:
    cur = conn.cursor()
    cur.executemany("INSERT INTO tbl_feedback(col_fname) VALUES (?);", file)
    conn.commit()
conn.close()
