def show_balance(balance):
    print("Current Balance: $", balance)

def deposit(balance):
    amount = input("Enter amount to deposit: ")
    balance = balance + float(amount)
    return balance

def withdraw(balance):
    while True:
        amount = float(input("\nEnter amount to withdraw: "))
        if amount > balance:
            print("You can't withdraw grater than the current money.")
            print("Enter the amount not grater than your current balance: $", balance)
            continue
        else:
            balance = balance - amount
            return balance


def logout(name):
    print("Goodbye " + name + "!")