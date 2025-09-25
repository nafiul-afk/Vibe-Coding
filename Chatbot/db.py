import mysql.connector
from config import DB_CONFIG

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def create_user(username, hashed_pw):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_pw))
        conn.commit()
        return True
    except:
        return False
    finally:
        cur.close()
        conn.close()

def get_user(username):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM users WHERE username=%s", (username,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user

def save_message(user_id, sender, message):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO messages (user_id, sender, message) VALUES (%s, %s, %s)", (user_id, sender, message))
    conn.commit()
    cur.close()
    conn.close()

def get_history(user_id):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT sender, message, timestamp FROM messages WHERE user_id=%s ORDER BY timestamp", (user_id,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
