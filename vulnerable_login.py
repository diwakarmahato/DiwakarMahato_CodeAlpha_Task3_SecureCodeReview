import sqlite3

# Hardcoded credentials (vulnerability 1)
USERNAME = "admin"
PASSWORD = "1234"

def login(user_input, pass_input):
    # No input sanitization (vulnerability 2)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # SQL Injection risk (vulnerability 3)
    query = f"SELECT * FROM users WHERE username = '{user_input}' AND password = '{pass_input}'"
    
    # Debug line (optional - helps in report)
    print("Query being run:", query)

    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        print("Login successful!")
    else:
        print("Login failed.")

# Simulated user input
username = input("Username: ")
password = input("Password: ")

login(username, password)
