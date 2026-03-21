# Base class
class Employee:
    def get_data(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.salary = float(input("Enter Salary: "))
        self.address = input("Enter Address: ")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


# Derived class
class Manager(Employee):
    def get_manager_data(self):
        self.department = input("Enter Department: ")

    def display_manager(self):
        self.display()  # call parent method
        print("Department:", self.department)
        print("-------------------------")


# Process 10 managers
managers = []

for i in range(10):
    print("\nEnter details of Manager", i+1)
    m = Manager()
    m.get_data()
    m.get_manager_data()
    managers.append(m)

print("\nManager Details:\n")

for m in managers:
    m.display_manager()