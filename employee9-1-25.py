import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob", "Diana"],
    "Age": [28, 34, 23, 29],
    "Department": ["HR", "IT", "Marketing", "Finance"],
    "Salary": [45000, 60000, 35000, 50000]
}

df = pd.DataFrame(data)

first_two_rows = df.head(2)
print("First 2 rows of the DataFrame:")
print(first_two_rows)

df['Bonus'] = df['Salary'] * 0.1
print("\nDataFrame with Bonus column added:")
print(df)

average_salary = df['Salary'].mean()
print(f"\nAverage Salary of employees: {average_salary}")

employees_older_than_25 = df[df['Age'] > 25]
print("\nEmployees older than 25:")
print(employees_older_than_25)
