# Adding Password Protection

import getpass

def authenticate():
    correct_password = "mypassword" # set your password here
    password = getpass.getpass("Enter your password: ")
    if password == correct_password:
        print("Access Granted!")
        return True
    else:
        print("Access Denied!")
        return False