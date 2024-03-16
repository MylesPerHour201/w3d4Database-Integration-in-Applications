import sqlite3

db = sqlite3.connect("blog.db")
curr = db.cursor()

def create_user_table():
    curr.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTERGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    email TEXT,
                    password TEXT
                )''')
    db.commit()
    print("User table created successfully")

    create_user_table()

    db.close()