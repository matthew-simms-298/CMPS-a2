# cmps-a2.py
# CMPS-3000 Assignment 2

# User Dictionary
users = [
    {
        "username": "admin",
        "password": "admin123",
        "role": "admin"
    },
    {
        "username": "editor",
        "password": "editor123",
        "role": "editor"
    },
    {
        "username": "viewer",
        "password": "viewer123",
        "role": "viewer"
    }
]
# Note: If implemented properly, passwords would be properly hashed and encrypted.

#Program Start

print("Welcome to the Notification System!")
print("Please fill in the following to log in:")
username = input("Username: ")
password = input("Password: ")

for user in users:
    if (username == user["username"] and password == user["password"]):
        userRole = user["role"]
        
        match userRole:
            case "admin":
                pass
            case "editor":
                pass
            case _:
                pass
        break
else:
    print("Invalid username or password. Exiting program.")
