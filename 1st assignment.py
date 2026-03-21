# Input
name = input("Enter Employee Name: ")
empID = int(input("Enter Employee ID: "))
department = input("Enter Department: ")
basic = float(input("Enter Basic Salary: "))

# Calculations
DA = 0.92 * basic
HRA = 0.58 * basic
TA = 0.30 * basic
LIC = 500

gross = basic + DA + HRA + TA
net = gross - LIC

# Output
print("\n----- Employee Details -----")
print("Name:", name)
print("Employee ID:", empID)
print("Department:", department)

print("\n----- Salary Details -----")
print("Basic Salary:", basic)
print("DA:", DA)
print("HRA:", HRA)
print("TA:", TA)
print("Gross Salary:", gross)
print("LIC Deduction:", LIC)
print("Net Salary:", net)