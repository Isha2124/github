import pandas as pd

# Create data for 5 states
data = {
    "State": ["Maharashtra", "Gujarat", "Rajasthan", "Karnataka", "Punjab"],
    "Area": [307713, 196024, 342239, 191791, 50362],          # in sq km
    "Population": [124000000, 70000000, 81000000, 68000000, 30000000]
}

# Create DataFrame
df = pd.DataFrame(data)

# a) Print complete information
print("Complete Information:\n")
print(df)

# b) State with largest area
max_area_state = df.loc[df["Area"].idxmax(), "State"]
print("\nState with largest Area:", max_area_state)

# c) State with largest population
max_pop_state = df.loc[df["Population"].idxmax(), "State"]
print("State with largest Population:", max_pop_state)

# d) Calculate population density
df["Density"] = df["Population"] / df["Area"]

print("\nPopulation Density:\n")
print(df[["State", "Density"]])

# e) State with highest population density
max_density_state = df.loc[df["Density"].idxmax(), "State"]
print("\nState with highest Population Density:", max_density_state)