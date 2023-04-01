import psycopg2
import json
import os


# Connect to the database 
conn = psycopg2.connect(
    host="<host_name>",
    port=<port_number>,
    user="<user_name>",
    password="<user_password>",
    database="<database_name>",
    sslmode="require"
)



# Open a cursor to perform database operations
cur = conn.cursor()

# Define the table schema
cur.execute("""
CREATE TABLE IF NOT EXISTS my_table (
    id SERIAL PRIMARY KEY,
    data JSONB
)
""")

# Read the JSON file
with open("path/to/file.json") as f:
    data = json.load(f)

# Insert data into the table
cur.execute("INSERT INTO my_table (data) VALUES (%s)", (json.dumps(data),))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
