students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    # Add student
    if choice == '1':
        sid = input("Enter ID: ")
        name = input("Enter Name: ")
        students.append({"id": sid, "name": name})
        print("Student added")

    # View students
    elif choice == '2':
        for s in students:
            print(s)

    # Update student
    elif choice == '3':
        sid = input("Enter ID to update: ")
        for s in students:
            if s["id"] == sid:
                s["name"] = input("Enter new name: ")
                print("Updated")
                break

    # Delete student
    elif choice == '4':
        sid = input("Enter ID to delete: ")
        students = [s for s in students if s["id"] != sid]
        print("Deleted")

    # Search student
    elif choice == '5':
        key = input("Enter ID or Name to search: ")
        for s in students:
            if s["id"] == key or s["name"] == key:
                print("Found:", s)

    elif choice == '6':
        break

    else:
        print("Invalid choice")