# 1. Take an input, test the type, apply break or continue to take input if it is not integer. test the Grade of the input.
# 2. write down the Grade from the list.

list_of_marks = [50, -100, -90, 200, 70, 99, 89, 80]
for item in list_of_marks:
    try:
        marks = float(item)
    except(ValueError):
        print("The marks isn't valid.")
        continue

    if not 0.0 <= marks <= 100.0:
        print(f"{item}: Marks must be between 0 to 100")
        continue
    if 97.0 <= marks <= 100.0:
        print(f"Marks: {item} Grade : A+")
    elif 93.0 <= marks < 97.0:
        print(f"Marks: {item} Grade : A")
    elif 90.0 <= marks < 93.0:
        print(f"Marks: {item} Grade : A-")
    elif 87.0 <= marks < 90.0:
        print(f"Marks: {item} Grade : B+")
    elif 83.0 <= marks < 87.0:
        print(f"Marks: {item} Grade : B")
    elif 80.0 <= marks < 83.0:
        print(f"Marks: {item} Grade : B-")
    elif 77.0 <= marks < 80.0:
        print(f"Marks: {item} Grade : C+")
    else:
        print(f"Marks: {item} Grade : D+")
    

