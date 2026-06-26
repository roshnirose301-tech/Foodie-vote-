import sqlite3

# Connect to Database
conn = sqlite3.connect("foodievote.db")

cursor = conn.cursor()

# Create Users Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# Create Debates Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS debates (
    debate_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    category TEXT NOT NULL,
    context TEXT,
    option1 TEXT NOT NULL,
    option2 TEXT NOT NULL,
    created_by INTEGER,
    FOREIGN KEY(created_by) REFERENCES users(user_id)
)
""")

# Create Votes Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS votes (
    vote_id INTEGER PRIMARY KEY AUTOINCREMENT,
    debate_id INTEGER,
    user_id INTEGER,
    selected_option TEXT,
    FOREIGN KEY(debate_id) REFERENCES debates(debate_id),
    FOREIGN KEY(user_id) REFERENCES users(user_id)
)
""")

conn.commit()
conn.close()

print("FoodieVote Database Created Successfully!")
