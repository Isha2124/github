import pandas as pd
import matplotlib.pyplot as plt

# Inventory Table
items = {
    "ITEM_ID": ["C101", "C102", "C103", "C104", "C105"],
    "ITEM_NAME": ["Denim Jeans", "Cotton Shirt", "Silk Saree", "Woolen Sweater", "Sports T-Shirt"],
    "CATEGORY": ["Bottomwear", "Topwear", "Ethnicwear", "Winterwear", "Active Wear"],
    "PRICE": [1500, 1200, 5000, 2000, 800],
    "STOCK": [30, 50, 20, 15, 60],
    "SUPPLIER": ["Levis", "Raymond", "Fabindia", "Spark", "Nike"]
}

df_items = pd.DataFrame(items)

# Supplier Table
suppliers = {
    "SUPPLIER_ID": ["S201", "S202", "S203", "S204", "S205"],
    "SUPPLIER_NAME": ["Levis", "Raymond", "Fabindia", "Monte Carlo", "Nike"],
    "LOCATION": ["Mumbai", "Delhi", "Bangalore", "Chandigarh", "Pune"]
}

df_suppliers = pd.DataFrame(suppliers)

# 📋 Display all items
print("Inventory Items:")
print(df_items)

# 📊 Visualization (Stock Comparison)
plt.bar(df_items["ITEM_NAME"], df_items["STOCK"])
plt.xlabel("Items")
plt.ylabel("Stock")
plt.title("Stock Available")
plt.xticks(rotation=30)
plt.show()