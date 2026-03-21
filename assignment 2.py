# Input Vendor Details
name = input("Enter Vendor Name: ")
year = int(input("Enter Year of Association: "))
contact = input("Enter Contact Number: ")
email = input("Enter Email ID: ")

# Input Monthly Purchases
monthly = []
print("\nEnter purchase amount for 12 months:")

for i in range(12):
    amt = float(input(f"Month {i+1}: "))
    monthly.append(amt)

# Calculation
annual_total = sum(monthly)
average = annual_total / 12

# Output
print("\n----- Vendor Details -----")
print("Name:", name)
print("Year of Association:", year)
print("Contact Number:", contact)
print("Email ID:", email)

print("\n----- Monthly Purchases -----")
for i in range(12):
    print(f"Month {i+1}: {monthly[i]}")

print("\n----- Annual Report -----")
print("Total Annual Purchase:", annual_total)
print("Average Monthly Purchase:", average)