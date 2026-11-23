import pandas as pd

df = pd.read_excel("Lab_sample\employee_data.xlsx")
print("First five rows:")
print(df.head())

print("\nMissing values in each column:")
print(df.isnull().sum())

df["Department"] = df["Department"].fillna("Unknown")

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Experience"] = df["Experience"].fillna(df["Experience"].mean())

def get_level(salary):
    if salary >= 60000:
        return "High"
    elif salary >= 40000:
        return "Medium"
    else:
        return "Low"

df["Salary_Level"] = df["Salary"].apply(get_level)

df = df.drop_duplicates()

print("\nCleaned data:")
print(df)

df.to_excel("cleaned_employee_data.xlsx", index=False)
print("\nExported to cleaned_employee_data.xlsx")