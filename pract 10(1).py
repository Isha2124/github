import pandas as pd

try:
    # Read file
    df = pd.read_csv("books.csv")

    # a) Print full data
    print("All Books:\n")
    print(df)

    # b) Books by author
    author = input("Enter author name: ")
    print(df[df["author"] == author])

    # c) Books by publishing house
    pub = input("Enter publishing house: ")
    print(df[df["publishing_house"] == pub])

    # d) Cheapest and costliest book
    print("Cheapest Book:")
    print(df[df["price"] == df["price"].min()]["title"])

    print("Costliest Book:")
    print(df[df["price"] == df["price"].max()]["title"])

    # e) Sort by year
    print("Sorted by Year:")
    print(df.sort_values("publication_year"))

except FileNotFoundError:
    print("Error: books.csv file not found")

except KeyError:
    print("Error: Column name is wrong (check CSV headings)")

except Exception as e:
    print("Some error occurred:", e)