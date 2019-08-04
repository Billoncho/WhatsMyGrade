# WhatsMyGrade.py
# Billy Ridgeway
# Practicing else if "El-If" statements by calculating grades.

# Creates the variable grade and ask the user to input their number grade between 0 and 100.
grade = eval(input("Enter your number grade (0-100): "))

if grade >= 90:                     # Evaluates the number contained in the grade variable and prints out the student's grade.
    print("You got an A! :) ")
elif grade >= 80:
    print("You got a B!")
elif grade >= 70:
    print("You got a C.")
elif grade >= 60:
    print("You got a D...")
else:
    print("You got an F. :( Your only future is as a paid protester for ANTIFA")
    
