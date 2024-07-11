marks = float(input("How many marks you got in your exams? "))
if marks >=90 and marks <= 100:
    print("Grade A")
elif marks >= 80 and marks <= 90:
    print("Grade B")
elif marks >= 70 and marks <= 80:
    print("Grade C")
elif marks >= 60 and marks <= 70:
    print("Grade D")
elif marks >= 50 and marks <= 60:
    print("Grade E")
else:
    print("You got an F")
