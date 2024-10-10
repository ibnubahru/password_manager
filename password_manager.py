"""

  Intermediate python project
  Password manager
  written by Mikyas Mulugeta

"""

master_pwd = input("What is the master password? ")


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"User: {user}")
            print(f"Password: {passw}")


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd)


while True:
    mode = input("Would you like to add new password or view existing ones(view, add), press q to Quit? ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
