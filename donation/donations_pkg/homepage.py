def show_homepage():
    print("")
    print("           === DonateMe Homepage ===")
    print("-----------------------------------------------")
    print("|     1. Login        |      2. Register      |")
    print("-----------------------------------------------")
    print("|     3. Donate       |   4. Show Donations   |")
    print("-----------------------------------------------")
    print("|                 5. Exit                     |")
    print("-----------------------------------------------")

def donate(username,total):
    while True:
        donation_amt = input("Enter amount to donate: $")
        if len(donation_amt) < 1:
            print("Enter the amount you want to donate.\n")
            continue
        elif donation_amt.isdigit() == False:
            print("Enter only the digits!!\n")
            continue

        if float(donation_amt) < 0:
            print("Please enter the amount you want to donate.\n")
            continue
        elif float(donation_amt) == 0:
            print("Okay. Maybe next time..\n")
            donation_string = ""
            total += 0
            return donation_string, total
            break
        else:
            total = total + float(donation_amt)
            donation_string = (f"{username.capitalize()} donated " + "${:,.2f}".format(float(donation_amt)))
            print("")
            print(donation_string)
            print(f"Thank you so much {username}!!\n")
            return donation_string, total
            break


def show_donations(donations):
    if donations == []:
        print("Currently, there are no donations.")
    else:
        print("\n--- All Donations ---")
        for donation in donations:
            print(donation)
    print("")