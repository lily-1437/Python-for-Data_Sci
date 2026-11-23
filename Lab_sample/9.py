import pandas as pd

data = {
    "Name": ["Amina", "Maya", "Lina", "Nora", "Sara"],
    "Quiz": [18, 12, 16, 9, 15],
    "Midterm": [25, 19, 28, 15, 22],
    "Final": [45, 31, 40, 25, 38]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

df["Total"] = df["Quiz"] + df["Midterm"] + df["Final"]

df["Average"] = df["Total"] / 3

df["Status"] = df["Total"].apply(lambda t: "Pass" if t >= 50 else "Fail")

print("\nDataFrame with Total, Average and Status:")
print(df)

passed = df[df["Status"] == "Pass"]
print("\nStudents who passed:")
print(passed)

df = df.sort_values(by="Total", ascending=False)
print("\nSorted by Total (descending):")
print(df)

df.to_excel("student_results.xlsx", index=False)
print("\nExported to student_results.xlsx")