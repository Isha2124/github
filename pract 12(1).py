import pandas as pd
import matplotlib.pyplot as plt

# Employee Table 1
data1 = {
    "EMPNO": ["E101", "E102", "E103", "E105", "E106"],
    "EMP_NAME": ["Vivek", "Vishal", "Priyal", "Shrushti", "Pranay"],
    "DEPT_NAME": ["R&D", "Marketing", "Product Dev", "Product Dev", "Product Dev"],
    "SALARY": [145000, 90000, 120000, 80000, 100000],
    "BRANCH": ["Nagpur", "Pune", "Bangalore", "Nagpur", "Mumbai"]
}

df1 = pd.DataFrame(data1)

# Employee Table 2 (Designation)
data2 = {
    "EMPNO": ["E101", "E102", "E103", "E105", "E106"],
    "DESIGNATION": ["Project Manager", "Sales Manager", "Design Architect",
                    "Software Developer", "Project Lead"]
}

df2 = pd.DataFrame(data2)

# 🔗 Merge both tables
df = pd.merge(df1, df2, on="EMPNO")

print("Merged Employee Table:")
print(df)

# 📊 Visualization (Salary Comparison)
plt.bar(df["EMP_NAME"], df["SALARY"])
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.title("Employee Salary Comparison")
plt.show()