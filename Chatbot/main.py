from db import create_user, get_user, save_message, get_history
from utils import hash_password, check_password, print_history, export_history
from chatbot import bot_reply

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed = hash_password(password)
    if create_user(username, hashed):
        print("✅ Registered successfully!")
    else:
        print("❌ Username already exists!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = get_user(username)
    if user and check_password(password, user['password']):
        print(f"✅ Welcome back, {username}!")
        chat(user)
    else:
        print("❌ Invalid credentials.")

def chat(user):
    print("\n[Chat Started] Type '/exit' to quit, '/history' to view chat history, '/export' to save it.\n")
    while True:
        msg = input("You: ")
        if msg == "/exit":
            print("👋 Bye!")
            break
        elif msg == "/history":
            history = get_history(user['id'])
            print_history(history)
        elif msg == "/export":
            history = get_history(user['id'])
            filename = export_history(history, user['username'])
            print(f"✅ Exported to {filename}")
        else:
            save_message(user['id'], "user", msg)
            reply = bot_reply(msg)
            print("Bot:", reply)
            save_message(user['id'], "bot", reply)

def main():
    print("Welcome to VibeChat!")
    print("1. Login")
    print("2. Register")
    choice = input("> ")
    if choice == "1":
        login()
    elif choice == "2":
        register()
        login()
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
