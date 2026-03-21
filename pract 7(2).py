# Initial balance
balance = 0.0

# Function to display balance
def display_balance():
    print("Current Balance:", balance)

# Function to deposit amount
def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Amount deposited successfully!")

# Function to withdraw amount
def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print("Amount withdrawn successfully!")

# Menu-driven program
while True:
    print("\n--- BANK MENU ---")
    print("1. Display Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        display_balance()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        print("Thank you for using the bank system!")
        break
    else:
        print("Invalid choice! Try again.")