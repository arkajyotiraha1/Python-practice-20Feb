# simulate a login system with 3 attempts
username_login = 'Arkajyoti'
passwd_login = 713365
attempts = 3
username = str(input("Enter your username:"))
if(username == username_login):
    passwd = int(input("Enter your password:"))
    if(passwd == passwd_login):
        print("Login Successful")
    else:
        while(attempts >= 1):
            passwd = int(input("Enter your password:"))
            if(passwd == passwd_login):
                print("Login Successful")
            attempts -=1
            print("3 tries done! Login Unsuccessful!")
else:
    print("Wrong Username!")