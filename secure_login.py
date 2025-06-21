# secure_login.py

import sqlite3
import getpass
import os

def login(user_input, pass_input):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Parameterized query to prevent SQL injection
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (user_input, pass_input))
    result = cursor.fetchone()

    if result:
        print("Login successful!")
    else:
        print("Login failed.")

# Get credentials from environment or safe input
username = input("Username: ")
password = input("Password: ")

# password = getpass.getpass("Password: ")

login(username, password)
