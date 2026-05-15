# Role-Based Access Control System

roles = {
    "admin": ["read", "write", "delete"],
    "staff": ["read", "write"],
    "guest": ["read"]
}

users = {
    "michael": "admin",
    "john": "staff",
    "visitor": "guest"
}

def check_access(username, action):
    if username not in users:
        return "Access denied: User does not exist."

    role = users[username]
    permissions = roles[role]

    if action in permissions:
        return f"Access granted: {username} can {action}."
    else:
        return f"Access denied: {username} cannot {action}."

print(check_access("michael", "delete"))
print(check_access("john", "delete"))
print(check_access("visitor", "read"))
print(check_access("visitor", "write"))
print(check_access("unknown", "read"))