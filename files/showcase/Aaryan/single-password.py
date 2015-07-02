import time

username = raw_input("username: ")
if username == "bob":
    print("Correct. Now type in your password.")
    password = raw_input("password: ")
    if password == "awesome":
        print("Correct. You may enter this computer.")
    else:
        print("Incorrect. Prepare for immediate destruction.")
else:
    print("Incorrect. Prepare for immediate destruction.")

time.sleep(5)