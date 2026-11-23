# Student Grade Program

mark = float(input("Enter the student's mark: "))

if mark < 0 or mark > 100:
    print("Invalid mark")
else:
    if mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 50:
        grade = "D"
    else:
        grade = "F"

    if mark >= 50:
        status = "Pass"
    else:
        status = "Fail"

    print("Mark:", mark)
    print("Grade:", grade)
    print("Status:", status)