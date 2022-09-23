# Import module
import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('../Data/chats.db')

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

def add_data(query):
    table = "INSERT INTO ASSISTANT(QUERY, DATE_TIME) VALUES (?, datetime('now', 'localtime'))"
    cursor.execute(table, (query,))
    conn.commit()
    return True

def get_data():
    data = cursor.execute('SELECT * FROM ASSISTANT')
    table_head = []
    for column in data