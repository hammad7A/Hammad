def convert_bytes():
    bytes_choice = int(input("How many bytes do you have? "))
    convert_choice = input("What do you want to convert your bytes into? ").lower()
    if convert_choice == 'kb':
        conversion = bytes_choice/1000
        return f"{convert_choice} = {conversion}"

    if convert_choice == "mb":
        conversion = bytes_choice/1_048_576
        return f"{convert_choice} = {conversion}"
    if convert_choice == "gb":
        conversion = bytes_choice/1_000_000_000
        return f"{convert_choice} = {conversion}"


def convert_kb():
    kb_choice = int(input("How many kbs do you have? "))
    convert_choice_two = input("What do you want to convert your kbs to? ")
    if convert_choice_two == "b":
        conversion_two = kb_choice*1024
        return f"{convert_choice_two} = {conversion_two}"
    if convert_choice_two == "mb":
        conversion_two = kb_choice/1024
        return f"{convert_choice_two} = {conversion_two}"
    if convert_choice_two == "gb":
        conversion_two = kb_choice/1000000
        return f"{convert_choice_two} = {conversion_two}"


def convert_mb():
    mb_choice = int(input("Enter your mbs: "))
    convert_choice_three = input("What do you want to convert your mbs to? ")
    if convert_choice_three == "b":
        conversion_three = mb_choice*1_048_576
        return f"{convert_choice_three} = {conversion_three}"
    if convert_choice_three == "kb":
        conversion_three = mb_choice/1024
        return f"{convert_choice_three} = {conversion_three}"
    if convert_choice_three == "gb":
        conversion_three = mb_choice/1024
        return f"{convert_choice_three} = {conversion_three}"

def convert_gb():
    gb_choice = int(input("Enter your amount of gb: "))
    convert_choice_four = input("What do you want to convert your gbs to? ")
    if convert_choice_four == "b":
        conversion_four = gb_choice*1000000000
        return f"{convert_choice_four} = {conversion_four}"
    if convert_choice_four == "kb":
        conversion_four = gb_choice*1_024*1_024
        return f"{convert_choice_four} = {conversion_four}"
    if convert_choice_four == "mb":
        conversion_four = gb_choice*1024
        return f"{convert_choice_four} = {conversion_four}"
user_choice = input("Which function do you want to execute?convert_bytes , convert_kb , convert_mb , convert_gb ")
if user_choice == "convert_bytes":
    print(convert_bytes())
elif user_choice == "convert_kb":
    print(convert_kb())
elif user_choice == "convert_mb":
    print(convert_mb())
elif user_choice == "convert_gb":
    print(convert_gb())



