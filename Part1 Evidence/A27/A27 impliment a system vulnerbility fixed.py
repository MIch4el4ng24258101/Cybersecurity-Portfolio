username = input("Enter username: ")
password = input("Enter password: ")

query = "SELECT * FROM users WHERE username = ? AND password = ?"