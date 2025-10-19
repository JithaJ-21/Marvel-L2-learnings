import hashlib
import os
import json
from datetime import datetime

USER_FILE = "users.json"

# Load existing users
def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

# Save users
def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

# Hash password + salt
def hash_password(password, salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()

# Auto-add demo user
def auto_add_user():
    users = load_users()
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    username = f"auto_user_{now}"

    salt = os.urandom(16).hex()
    hashed = hash_password("default_password", salt)

    users[username] = {"salt": salt, "hash": hashed}
    save_users(users)
    print(f"✅ Added {username}")

if __name__ == "__main__":
    print("Running auto-update script…")
    auto_add_user()
