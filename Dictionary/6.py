marks = [88, 74, 93, -5, 61, 47, 105, 82, 59]

valid_marks = []
grades = {"A": 0, "B": 0, "C": 0, "F": 0}

for m in marks:
    if 0 <= m <= 100:
        valid_marks.append(m)
        if m >= 80:
            grades["A"] += 1
        elif m >= 70:
            grades["B"] += 1
        elif m >= 60:
            grades["C"] += 1
        else:
            grades["F"] += 1

average = sum(valid_marks) / len(valid_marks)

print("Valid marks:", valid_marks)
print("Grade counts:", grades)
print(f"Average: {average:.2f}")