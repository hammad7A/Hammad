import sys


def balance(amount):
    print(f"Your current balance is {amount:.2f}")

def withdraw():
    withdraw_choice = float(input("Enter the amount you want to withdraw: "))
    return withdraw_choice
def deposit():
    deposit_choice = float(input("Enter the amount you want to deposit: "))
    return deposit_choice

def transfer(transfer):
    transfer_choice = int(input("Enter the amount you want to transfer: "))
    transfer_account["transfer"] = transfer_choice
    return transfer_account
transfer_account = {}
def view_transfer():
    view_transfer_choice = input("Do you want to view the transfered funds: y/n ")
    if view_transfer_choice == "y":
        print(transfer_account)

def emergency_cash(balance_total):
    cash_choice = float(input("Choose the amount of cash you want to withdraw!!!"))
    if cash_choice < balance_total:
        balance_total -= cash_choice
        print(balance_total)
    else:
        print("Insufficient funds! ")







balance_total = 1000


while True:
    user_choice = input("Choose (balance withdraw deposit transfer view emergency q for quit) ")
    if user_choice == "balance":
        current_balance = str(balance(balance_total))
    elif user_choice == "withdraw":
        withdraw_balance = withdraw()
        if withdraw_balance < balance_total:
            balance_total -= withdraw_balance
            print(balance_total)
    elif user_choice == "deposit":
        deposit_balance = deposit()
        balance_total += deposit_balance
        print(balance_total)
    elif user_choice == "transfer":
        transfer_output = transfer(transfer_account)
        print(transfer_output)
    elif user_choice == "view":
        view = view_transfer()
    elif user_choice == "emergency":
        emergency_output = emergency_cash(balance_total)
    elif user_choice == "q":
        sys.exit()
    else:
        print("Invalid call! ")




