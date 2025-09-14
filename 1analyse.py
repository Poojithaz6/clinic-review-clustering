import pandas as pd
import matplotlib.pyplot as plt

# Load the filtered data
df = pd.read_csv("filtered_bills.csv")

# Ensure 'Age' column is numeric
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

# Filter for patients of age 0
df_age_0 = df[df["Age"] == 0]

# Count how many unique patients used each item
item_usage = df_age_0.groupby("Item")["Patient Unique ID"].nunique().sort_values()

# Plot: Horizontal Bar Chart
plt.figure(figsize=(10, 6))
item_usage.plot(kind='barh', color='skyblue')
plt.xlabel("Number of Patients (Age 0)")
plt.ylabel("Item Name")
plt.title("Usage of Items by Patients Aged 0")
plt.tight_layout()
plt.savefig("item_usage_by_age_0.png")

