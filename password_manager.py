import hashlib
import os
import json
import pwinput

# File to store user data (always saved beside this script)
USER_FILE = "users.json"
print("DEBUG: users.json is stored at:", os.path.abspath(USER_FILE))

# Load users if file exists
def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}  # if file is empty or invalid
    return {}

# Save users to file
def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)  # formatted output with indentation

# Hash password with SHA-256 + salt
def hash_password(password: str, salt: str) -> str:
    return hashlib.sha256((password + salt).encode()).hexdigest()

# Register new user
def register_user(username: str, password: str, users: dict):
    if username in users:
        print("❌ Username already exists.")
        return users
    
    # Generate a random salt per user
    salt = os.urandom(16).hex()
    hashed = hash_password(password, salt)

    # Store salt + hash together
    users[username] = {"salt": salt, "hash": hashed}
    try:
        with open(USER_FILE, "w") as f:
            json.dump(users, f, indent=4)
        print(f"✅ User '{username}' registered successfully.")
    except Exception as e:
        print(f"❌ Error saving user: {e}")
    
    return users

# Authenticate user
def authenticate_user(username: str, password: str, users: dict):
    if username not in users:
        print("❌ User not found.")
        return False
    
    salt = users[username]["salt"]
    stored_hash = users[username]["hash"]
    entered_hash = hash_password(password, salt)

    if entered_hash == stored_hash:
        print("✅ Authentication successful!")
        return True
    else:
        print("❌ Incorrect password.")
        return False

# Delete a registered user
def delete_user(username: str, users: dict):
    if username not in users:
        print("❌ User not found.")
        return users
    
    confirm = input(f"Are you sure you want to delete '{username}'? (yes/no): ").strip().lower()
    if confirm == "yes":
        users.pop(username)
        # Save updated users
        with open(USER_FILE, "w") as f:
            json.dump(users, f, indent=4)
        print(f"✅ User '{username}' deleted successfully.")
    else:
        print("❌ Deletion cancelled.")
    
    return users

# Main program loop
if __name__ == "__main__":
    users = load_users()

    while True:
        print("\nOptions: register | login | delete | quit\n", flush=True)
        choice = input("Choose an option: ").strip().lower()

        if choice == "register":
            uname = input("Enter username: ")
            pwd = pwinput.pwinput(prompt="Enter password: ", mask="*")
            users = register_user(uname, pwd, users)

        elif choice == "login":
            uname = input("Enter username: ")
            pwd = pwinput.pwinput(prompt="Enter password: ", mask="*")
            authenticate_user(uname, pwd, users)

        elif choice == "delete":
            uname = input("Enter username to delete: ")
            users = delete_user(uname, users)

        elif choice == "quit":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
