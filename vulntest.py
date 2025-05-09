import sqlite3
import random
import os

# Vulnerability 1: Hardcoded credentials
USERNAME = "admin"
PASSWORD = "admin123"  # This should be considered a security flaw

# Vulnerability 2: SQL Injection
user_input = input("Enter username: ")
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
query = f"SELECT * FROM users WHERE username = '{user_input}'"
cursor.execute(query)
data = cursor.fetchall()

# Vulnerability 3: Insecure Randomness
otp = random.randint(1000, 9999)
print(f"Generated OTP: {otp}")

# Vulnerability 4: Command Injection
filename = input("Enter filename to delete: ")
os.system(f"rm {filename}")  # Dangerous: unsanitized user input

# Vulnerability 5: Missing SSL Verification
import requests
resp = requests.get("https://example.com", verify=False)  # Insecure: SSL not verified

print("Done")
