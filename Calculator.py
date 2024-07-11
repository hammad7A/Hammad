def add(n1,n2):
    result = n1 + n2
    return result
def multiply(n1,n2):
    result = n1 * n2
    return result
def subtract(n1,n2):
    result = n1 - n2
    return result
def divide(n1,n2):
    result = n1 / n2
    return result
user_choice = input("Do you want to add multiply subtract or divide? ").lower()
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
if user_choice == "add":
    print(add(num1,num2))
elif user_choice == "multiply":
    print(multiply(num1,num2))
elif user_choice == "subtract":
    print(subtract(num1,num2))
elif user_choice == "divide":
    print(divide(num1,num2))