# 🤖 Chatbot with Database Memory

This is a **Python + MySQL chatbot** that remembers conversations.  
Every message (user + bot) is stored in a MySQL database, so you can fetch past chats and keep context.  

---

## 🚀 Features
- User registration & login  
- Stores chat history in MySQL  
- Retrieve old messages with `/history`  
- Export chats to `.txt`  
- Easy to extend with GPT APIs later  

---

## 🛠️ Tech Stack
- Python 3.10+  
- MySQL  
- Libraries: `mysql-connector-python`, `bcrypt`, `prettytable`  

---

## ⚙️ Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/nafiul-afk/Vibe-Coding.git
   cd Vibe-Coding/Chatbot

2. Install dependencies:

   ```bash
   pip install -r requirements.txt

3. Import the database schema:

   ```bash
   mysql -u root -p < schema.sql

4. Configure DB credentials in config.py.
5. Run the chatbot:
   
   ```bash
   python main.py

---

## Structure
```
Chatbot/
│── README.md
│── requirements.txt
│── config.py              # DB config
│── main.py                # entry point
│── db.py                  # database connection & queries
│── chatbot.py             # bot logic
│── utils.py               # helper functions
│── schema.sql             # MySQL schema

```















   
