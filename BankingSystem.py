def createAccount():
    person_user = input("Make a username: ")
    person_pass = input("Make a password: ")
    print("Your account has been created successfully! ")
    return {"username":person_user,"password":person_pass
    ,"balance":0}



def depositMoney(account_call):
    deposit_choice = int(input("Enter the amount of money you want to deposit: "))
    account_call["balance"] += deposit_choice
    print(f"${deposit_choice} have been deposited to your account")
    return account_call

def withdrawMoney(account_withdraw):
    withdraw_choice = int(input("Enter the amount of money you want to withdraw: "))
    account_withdraw["balance"] -= withdraw_choice
    print(f"$ {withdraw_choice} have been withdrawn from your account! ")
    return account_withdraw
def checkAccount(account_check):
    check_choice = input("Do you want to check the balance in your account?y/n ")
    if check_choice == "y":
        print(f"Your account balance is: ${account_check['balance']}")
        return account_check


account_create = createAccount()
account_deposit = depositMoney(account_create)
account_withdraw = withdrawMoney(account_create)
account_check = checkAccount(account_create)