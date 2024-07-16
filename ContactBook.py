print("Your contact book currently has 0 members! ")


def addMembers():
    person_name = input("Please enter the name of the person you wish to add to your contacts.")
    person_number = int(input("Please enter the password of that person. "))
    print(f"{person_name} has been added to your contact book! ")
    return {person_name:person_number}


def updateMembers(update_members):
    new_update = input("Enter the name of the person you want to update to your contact book ")
    new_update_pass = int(input("Enter the password of that person "))
    update_members[new_update] = new_update
    update_members[new_update] = new_update_pass
    print(f"{new_update}  has been added to your contact book")

def deleteMembers(delete_accounts):
    delete_members = input("Enter in the account you want to delete: ")
    del delete_accounts[delete_members]
    print(f"{delete_members}'s account has been deleted from your contact book")

def viewMembers(view_members):
    view_choice = input("Do you want to view your current contacts? ")
    if view_choice:
        print(view_members)


members = addMembers()
members_update = updateMembers(members)
members_delete = deleteMembers(members)
members_view = viewMembers(members)