# Fernandez,Girlly
correct_username_gmf = "admin"
correct_password_gmf = "1234"

attempts = 0

while attempts < 3:
    username_gmf = input("Enter username: ")
    password_gmf = input("Enter password: ")

    if username_gmf == correct_username_gmf and password_gmf == correct_password_gmf:
        print("Login successful")
        break
    else:
        print("Invalid Credentials")
        attempts += 1

if attempts == 3:
    print("Account Locked")