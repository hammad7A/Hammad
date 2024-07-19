questions = [
    ("What is 1+1 as strings? ", ["11", "2", "Vancouver"], "11"),
    ("Write the basic types of loops ", ["ForWhile", "For", "While"], "ForWhile"),
    ("What is 1+69 as integers", ["2", "70", "11"], "70"),
    ("What does (f) in f strings stand for?", ["formatted", "file", "force"], "formatted"),
    ("Can math be done on strings?", ["Yes", "No", "Idk"], "No")
]


for q in questions:
    question = q[0]
    options = q[1]
    answer = q[2]
    print(question)
    for i in range(len(options)):
        print(f"{i+1} - {options[i]}")
    answer_choice = input("Choose your answer: ").lower()
    if answer_choice == answer.lower():
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is: {answer}")


