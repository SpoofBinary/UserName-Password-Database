# random project // 7/2/22

def PasswordLogin():
    f = open("password.db", "r")
    PasswordList = (f.read())
    User = input('''Password => ''')
    if User == PasswordList:
        print('''Successful''')
    if User != PasswordList:
        print("Unsuccessful! Try Again")
        PasswordLogin()

def UsernameLogin():
    f = open("username.db", "r")
    UsernameList = (f.read())
    User = input('''Username => ''')
    if User == UsernameList:
        print('''Successful''')
        PasswordLogin()
    if User != UsernameList:
        print("Unsuccessful! Try Again")
        UsernameLogin()

def Database():
    f = open("database.db", "r")
    print(f.read())

def Start():
    UsernameLogin()
    Database()

Start()