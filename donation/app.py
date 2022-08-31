from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {'admin':'password123'}
donations = []
authorized_user = ""
total = 0

show_homepage()

if authorized_user == "":
    print("You must be logged in to donate.")
else:
    print(f"Logged in as: {authorized_user}")

while True:
    options = input("Choose an option: ")
    if options == "1":
        username = input("Enter username: ")
        username = username.lower()
        password = input("Enter password: ")
        authorized_user = login(database,username,password)

        if authorized_user != "":
            print("You must be logged in to donate.")
        continue
    elif options == "2":
        username = input("Enter the username you want to use: ").lower()
        password = input("Enter the password you want to use: ")
        authorized_user = register(database, username, password)

        if authorized_user != "":
            database.update({username:password})
        continue
    elif options == "3":
        if authorized_user == "":
            print("You are not logged in.")
            continue
        else:
            donation_his = donate(authorized_user,total)
            donations.append(donation_his[0])
            total = donation_his[1]
        continue
    elif options == "4":
        show_donations(donations)
        print(f"Total : ${total}\n")
        continue
    elif options == "5":
        print(f"Leaving DonateMe... Goodbye {authorized_user.capitalize()}!")
        break