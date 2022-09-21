print("Welcome to Grade Assignment")
input("Student Name \t")
input("Student SCID \t")
A = int(input("Enter your percentage on Assignment Component of Grade Evaluation \t "))
L = int(input("Enter your percentage on Lab Component of Grade Evaluation \t"))
R = int(input("Enter your percentage on Reading Component of Grade Evaluation \t"))
Q = int(input("Enter your percentage on Quizzes Component of Grade Evaluation \t"))
M = int(input("Enter your percentage on Midterm Component of Grade Evaluation \t"))
P = int(input("Enter your percentage on Project Component of Grade Evaluation \t"))
print("Total is", A+L+R+Q+M+P)
if A+L+R+Q+M+P >= 94:
    print("Letter Grade: A")
    print("Grade Point: 4.000")
    print("Excellent Performance")
elif A+L+R+Q+M+P >= 90:
    print("Letter Grade: A-")
    print("Grade Point: 3.667")
    print("Excellent Performance")
elif A+L+R+Q+M+P >= 87:
    print("Letter Grade: B+")
    print("Grade Point: 3.333")
    print("Good Performance")
elif A+L+R+Q+M+P >= 84:
    print("Letter Grade: B")
    print("Grade Point: 3.000")
    print("Good Performance")
elif A+L+R+Q+M+P >= 80:
    print("Letter Grade: B-")
    print("Grade Point: 2.667")
    print("Good Performance")
elif A+L+R+Q+M+P >= 77:
    print("Letter Grade: C+")
    print("Grade Point: 2.333")
    print("Average Performance")
elif A+L+R+Q+M+P >= 74:
    print("Letter Grade: C")
    print("Grade Point: 2.000")
    print("Average Performance")
elif A+L+R+Q+M+P >= 70:
    print("Letter Grade: C-")
    print("Grade Point: 1.667")
    print("Average Performance")
elif A+L+R+Q+M+P >= 65:
    print("Letter Grade: D+")
    print("Grade Point: 1.333")
    print("Unsatisfactory Performance")
elif A+L+R+Q+M+P >= 60:
    print("Letter Grade: D")
    print("Grade Point: 1.000")
    print("Unsatisfactory Performance")
elif A+L+R+Q+M+P >= 55:
    print("Letter Grade: D-")
    print("Grade Point: 0.667")
    print("Unsatisfactory Performance")
elif A+L+R+Q+M+P <= 54.99:
    print("Letter Grade: F")
    print("Grade Point: 0.000")
    print("Failing Performance")
