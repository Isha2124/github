try:
    f1 = open("input.txt", "r")
    data = f1.read()
    data_upper = data.upper()
    f2 = open("output.txt", "w")
    f2.write(data_upper)
    f1.close()
    f2.close()
    print("Content copied in uppercase successfully!")

except FileNotFoundError:
    print("Error: input.txt file not found.")

except IOError:
    print("Error: Problem in file handling.")