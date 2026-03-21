# Input from user
V = float(input("Enter Voltage (V): "))
R = float(input("Enter Resistance (R): "))

# Calculation using Ohm's Law
I = V / R

# Display current
print("Current (I) =", I, "Ampere")

# Check nature of current
if I < 0.5:
       print("Low current")
elif I <= 2:
       print("Normal current")
else:
       print("High current")