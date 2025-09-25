import bcrypt
from prettytable import PrettyTable

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

def print_history(history):
    table = PrettyTable()
    table.field_names = ["Sender", "Message", "Time"]
    for h in history:
        table.add_row([h['sender'], h['message'], str(h['timestamp'])])
    print(table)

def export_history(history, username):
    filename = f"examples/{username}_history.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for h in history:
            f.write(f"[{h['timestamp']}] {h['sender']}: {h['message']}\n")
    return filename
