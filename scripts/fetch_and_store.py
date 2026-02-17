import requests
import sqlite3

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
users = response.json()

conn = sqlite3.connect("../data/crm_data.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    company TEXT
)
""")

for user in users:
    cursor.execute("""
    INSERT OR REPLACE INTO users (id, name, email, company)
    VALUES (?, ?, ?, ?)
    """, (
        user["id"],
        user["name"],
        user["email"],
        user["company"]["name"]
    ))

conn.commit()
conn.close()

print("Integration complete")