# Tuple of prices of sold items
prices = (120, 250, 80, 300, 150, 300, 90)

# a) Total number of items sold
print("Total number of items sold:", len(prices))

# b) Price of cheapest item
print("Cheapest item price:", min(prices))

# c) Price of costliest item
print("Costliest item price:", max(prices))

# d) Price list in ascending order
print("Prices in ascending order:", sorted(prices))

# e) Number of costliest items sold
costliest = max(prices)
count = prices.count(costliest)
print("Number of costliest items sold:", count)