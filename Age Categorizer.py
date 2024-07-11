age_choice = float(input("Enter your age: "))
if age_choice <= 0:
    print("You ain't even born yet")
elif age_choice <= 7 and age_choice >= 8:
    print("You are a child")
elif age_choice <= 12 and age_choice >= 12:
    print("You are a kid")
elif age_choice <= 18 and age_choice >= 18:
    print("You are a teenager")
elif age_choice <= 25 and age_choice >= 25:
    print("You are a young adult")
elif age_choice <= 30 and age_choice >= 30:
    print("You are an adult")
