username = input("Username: ")
password = input("Password: ")

i=1
while i<5:
        if username.strip() =="python" and password.strip() =="rules":
            print("Welcome")
            break

        print("please try again")
        i += 1
        username = input("Username: ")
        password = input("Password: ")
else:
    print("username or password are incorrect")
    print("Access Denied")




