try:
    source = input("Enter source file name: ")
    destination = input("Enter destination file name: ")

    f1 = open(source, "r")
    lines = f1.readlines()

    f2 = open(destination, "w")

    for line in lines:
        if not line.strip().startswith("#"):
            f2.write(line)

    f1.close()
    f2.close()

    print("\nSource File Content:")
    f1 = open(source, "r")
    print(f1.read())
    f1.close()

    print("\nDestination File Content (without comments):")
    f2 = open(destination, "r")
    print(f2.read())
    f2.close()

except FileNotFoundError:
    print("Error: Source file not found.")

except IOError:
    print("Error: File handling problem.")