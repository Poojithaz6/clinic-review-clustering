import pandas as pd
import matplotlib.pyplot as plt

# Load the filtered CSV
df = pd.read_csv("filtered_bills.csv")

# Clean column names to avoid space issues
df.columns = df.columns.str.strip()

# Ensure Age is numeric
df["Age"] = pd.to_numeric(df["Age"], errors='coerce')

# Filter rows for patients aged 0
df_age_0 = df[df["Age"] == 2]

# Clean up any blank or empty service categories
df_age_0["ServiceCategory"] = df_age_0["ServiceCategory"].replace(r"^\s*$", pd.NA, regex=True)

# Drop rows where ServiceCategory is missing
df_age_0 = df_age_0.dropna(subset=["ServiceCategory"])

# Count how many times each service was used
service_usage = df_age_0["ServiceCategory"].value_counts().sort_values()

# Plotting
plt.figure(figsize=(10, 6))
service_usage.plot(kind='barh', color='lightcoral')
plt.xlabel("Number of Times Used")
plt.ylabel("Service Category")
plt.title("Services Used by Patients Aged 2")
plt.tight_layout()
plt.savefig("services_by_age_2_fixed.png")

print("✅ Graph saved as 'services_by_age_2_fixed.png'")
