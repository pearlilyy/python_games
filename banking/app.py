from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("          === Automated Teller Machine ===          ")

while True:
    name = input("Enter name to register: ")
    print(len(name))
    if len(name) > 10:
        print("The maximun name length is 10 characters.")
        continue
    elif len(name) <= 0:
        print("You must enter a name.")
        continue
    else:
        break

while True:
    pin = input("Enter PIN: ")
    if len(pin) != 4:
        print("PIN must contain 4 numbers")
        continue
    else:
        break
    
balance = 0
balance = float(balance)

# print(name + " has been registered with a starting balance of", "${:,.2f}".format(balance))
print(name + " has been registered with a starting balance of $" + str(balance))

while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")

    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!\n")
        break
    else:
        print("Invalid credentials!\n")
        continue

while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option == "4":
        account.logout(name)
        break