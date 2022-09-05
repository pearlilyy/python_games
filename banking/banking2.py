class User:
    def __init__(self, name, pin, password):
        self.name = name.replace(" ", "")    # remove spaces
        self.pin = pin
        self.password = password

    def change_name(self, name):
        if len(name) < 2 or len(name) > 10:
            print("The length of the username must be 2-10!\n")
            return False
        elif name == self.name:
            print("Enter a different user name!\n")
            return False
        else:
            self.name = name.replace(" ", "")    # remove spaces
            print("Your name is changed successfully!")

    def change_pin(self, pin):
        if len(str(pin)) != 4:
            print("The PIN must be 4 digits!\n")
            return False
        elif pin == self.pin:
            print("Enter a different PIN!\n")
            return False
        else:
            self.pin = pin
            print("Your PIN is changed successfully!")

    def change_password(self, password):
        if len(password) < 5:
            print("The length of new password must be at least 5!\n")
            return False
        elif password == self.password:
            print("Enter a different password!\n")
            return False
        else:
            self.password = password.replace(" ", "")
            print("Your password is changed successfully!")


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
        self.on_hold = False

    def toggle_hold(self):
        self.on_hold = not self.on_hold
        return self.on_hold

    def show_balance(self):
        # show 2자리 소수점
        print(self.name, "has an account balance of: ${:,.2f}".format(
            self.balance))

    def withdraw(self, amount):
        self.amount = amount
        if self.on_hold is True:
            print("Account Hold")
            return self.balance
        # elif amount.isdigit() == False:
        #     print("Enter only digits!")
        #     return self.on_hold
        elif amount > self.balance:
            print("You can NOT withdraw bigger amount than your current balance!\n")
            return self.on_hold
        else:
            self.balance -= amount

    def deposit(self, amount):
        self.amount = amount
        if amount < 0:
            print("Enter the positive amount you want to deposit!\n")
            return self.on_hold
        elif amount == 0:
            print("Okay. Maybe next time..\n")
            return self.on_hold
        else:
            self.balance += amount

    def transfer_money(self, amount, user):
        self.amount = amount
        self.user = user

        if amount > self.balance:
            print("You can NOT transfer bigger amount than your current balance!\n")
            return self.on_hold

        print(f"{self.name}, you are transferring ${amount} to {user.name}\n")
        print("Authentication Required")
        enter_pin = input("Enter your PIN: ")
        if int(enter_pin) == self.pin:
            print("Transfer Authorized")
            print(f"Transferring ${amount} to {user.name}\n")
            self.balance -= amount
            user.balance += amount
            return True
        else:
            print("Invalid PIN. Transaction canceled.\n")
            return self.on_hold

    def request_money(self, amount, user):
        self.amount = amount
        self.user = user
        print(f"{self.name}, you are requesting ${amount} from {user.name}")
        print("User authentication is required...")
        enter_pin = input(f"{self.name}, enter {user.name}'s PIN: ")
        if int(enter_pin) == user.pin:
            enter_pass = input("Enter your password: ")
            if enter_pass == self.password:
                if amount > user.balance:
                    print(
                        f"You can NOT request bigger amount than {user.name}'s balance!\n")
                    return self.on_hold
                print("Request Authorized\n")
                print(f"{user.name} sent ${amount}")
                self.balance += amount
                user.balance -= amount
                return True
            else:
                print("Invalid password. Transaction canceled.\n")
                return self.on_hold
        else:
            print("Invalid PIN. Transaction canceled.\n")
            return self.on_hold


""" Driver Code for Task 1 """
'''
user = User("Angel",1234,"password")
print(user.name, user.pin, user.password)
'''

""" Driver Code for Task 2 """
'''
user = User("Angel",1234,"password")
print(user.name, user.pin, user.password)
user.change_name("moon")
user.change_pin(4321)
user.change_password("passpass")
print(user.name, user.pin, user.password)
'''

""" Driver Code for Task 3"""
'''
bankuser = BankUser("knight", 1324, "passcode")
print(bankuser.name, bankuser.pin, bankuser.password, bankuser.balance)
'''

""" Driver Code for Task 4"""
# '''
bankuser = BankUser("moon", 1324, "password")
bankuser.show_balance()
bankuser.deposit(5000)
bankuser.show_balance()
bankuser.withdraw(1000)
bankuser.show_balance()
# '''

'''
bankuser1 = BankUser("Moon",1324,"password")
bankuser2 = BankUser("Pearl",1234,"password")
bankuser2.deposit(5000)
bankuser2.show_balance()
bankuser1.show_balance()
bankuser2.transfer_money(500, bankuser1)
bankuser2.show_balance()
bankuser1.show_balance()
bankuser2.request_money(1000, bankuser1)
bankuser2.show_balance()
bankuser1.show_balance()
'''
