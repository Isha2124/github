import matplotlib.pyplot as plt

# Data (manually given)
months = [1,2,3,4,5,6,7,8,9,10,11,12]

facecream = [2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900]
facewash = [1500,1200,1340,1130,1740,1550,1120,1400,1780,1890,2100,1760]
toothpaste = [5200,5100,4550,5870,6000,7000,7300,6100,8300,7300,7400,8000]
bathingsoap = [9200,6100,9550,8870,9960,8100,7800,9700,10000,8800,9800,10500]
shampoo = [1200,2100,3550,1870,1560,1890,1780,2100,2300,2400,1800,2100]
moisturizer = [1500,1200,1340,1130,1740,1550,1120,1400,1780,1890,2100,1760]

total_profit = [21100,18300,22400,53200,51200,31200,30000,42000,45000,39000,42000,48000]

# a) Line plot
plt.plot(months, total_profit, marker='o')
plt.title("Total Profit per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()

# b) Multiline plot
plt.plot(months, facecream, label="Face Cream")
plt.plot(months, facewash, label="Face Wash")
plt.plot(months, toothpaste, label="Toothpaste")
plt.plot(months, bathingsoap, label="Soap")
plt.plot(months, shampoo, label="Shampoo")
plt.plot(months, moisturizer, label="Moisturizer")

plt.title("Sales Data")
plt.legend()
plt.show()

# c) Bar chart
import numpy as np
x = np.arange(len(months))

plt.bar(x-0.2, facecream, width=0.4, label="Face Cream")
plt.bar(x+0.2, facewash, width=0.4, label="Face Wash")

plt.xticks(x, months)
plt.legend()
plt.title("Face Cream vs Face Wash")
plt.show()

# d) Pie chart
total_sales = [
    sum(facecream),
    sum(facewash),
    sum(toothpaste),
    sum(bathingsoap),
    sum(shampoo),
    sum(moisturizer)
]

labels = ["Face Cream","Face Wash","Toothpaste","Soap","Shampoo","Moisturizer"]

plt.pie(total_sales, labels=labels, autopct='%1.1f%%')
plt.title("Total Sales Distribution")
plt.show()