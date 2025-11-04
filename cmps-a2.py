# cmps-a2.py
# CMPS-3000 Assignment 2


#Program Start

print("Welcome to the Notification System!")
print("Please fill in the following to log in:")
username = input("Username: ")
password = input("Password: ")

for user in users:
    if (username == user["username"] and password == user["password"]):
        userRole = user["role"]
        
        match userRole:
            case "Admin":
                pass
            case "editor":
                pass
            case _:
                pass
        break
else:
    print("Invalid username or password. Exiting program.")
