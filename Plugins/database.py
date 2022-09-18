# Import module
import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('../Data/chats.db')

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

def add_data(query):
    table = "INSERT INTO ASSISTANT(QUERY, DATE_TI